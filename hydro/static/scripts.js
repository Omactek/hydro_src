document.addEventListener("DOMContentLoaded", function() {
    const stationDropdown = document.getElementById("stationDropdown");
    const valueDropdown = document.getElementById("valueDropdown");
    const yearDropdown = document.getElementById("yearDropdown");
    const yearlyChart = document.getElementById("yearlyChart");
    const seriesChart = document.getElementById("seriesChart");
    const startPicker = flatpickr('#startPicker', {
        dateFormat: 'd-m-Y',
        minDate: '',
        maxDate: '',
        disable: [],
        defaultDate: [],
    }); 
    const endPicker = flatpickr('#endPicker', {
        dateFormat: 'd-m-Y',
        minDate: '',
        maxDate: '',
        disable: [],
        defaultDate: [],
    });
    function updateDatePicker(startWidget, endWidget, startDate, endDate, disableDates, defaultDate) {
        startWidget.set('minDate', startDate);
        startWidget.set('maxDate', endDate);
        startWidget.set('disable', disableDates);
        //startWidget.set('defaultDate', defaultDates);
        endWidget.set('minDate', startDate);
        endWidget.set('maxDate', endDate);
        endWidget.set('disable', disableDates);
        //endWidget.set('defaultDate', defaultDates);
    } 

    let stationsData = {};

    var map = L.map('map').setView([49.8175, 15.4730], 7); // centered on the Czech Republic

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);

    fetch('/api/stations/geo/')
        .then(response => response.json())
        .then(data => {
            L.geoJSON(data, {
                onEachFeature: function (feature, layer) {
                    if (feature.properties) {
                        layer.bindPopup(`<b>${feature.properties.st_label}</b>`);
                    }
                    layer.on('click', function () {
                        stationDropdown.value = feature.id;
                        fetchValues();
                        zoomToStation(feature.id);
                    });
                }
            }).addTo(map);

            // store station data for later use
            data.features.forEach(feature => {
                stationsData[feature.id] = feature.geometry.coordinates;
            });
        })
        .catch(error => console.error('Error fetching GeoJSON data:', error));

    function formatDateForBackend(date) {
        if (date) {
            const formattedDate = new Date(date);
            const year = formattedDate.getFullYear();
            const month = String(formattedDate.getMonth() + 1).padStart(2, '0'); // month is zero-based
            const day = String(formattedDate.getDate()).padStart(2, '0');
            return `${year}-${month}-${day}`;
        }
        else {
            return '';
        }
    }

    function zoomToStation(stationId) {
        const coordinates = stationsData[stationId];
        if (coordinates) {
            map.setView([coordinates[1], coordinates[0]], 13); // leaflet uses [lat, lng]
        }
    }

    function fetchStations() {
        fetch('/api/stations/')
            .then(response => response.json())
            .then(data => {
                stationDropdown.innerHTML = "";  // clear previous options
                data.forEach(station => {
                    const option = document.createElement("option");
                    option.value = station.st_name;
                    option.textContent = station.st_label;
                    stationDropdown.appendChild(option);
                });
                fetchValues();
            })
            .catch(error => console.error('Error fetching stations:', error));
    }

    function fetchValues() {
        const stationId = stationDropdown.value;
        fetch(`/api/stations/${stationId}/values/`)
            .then(response => response.json())
            .then(data => {
                valueDropdown.innerHTML = "";  // clear previous options
                data.forEach(value => {
                    const option = document.createElement("option");
                    option.value = value.django_field_name;
                    option.textContent = value.parameter;
                    option.setAttribute('unit', value.unit); // store unit in data attribute
                    valueDropdown.appendChild(option);
                });
                if (valueDropdown.options.length > 0) valueDropdown.selectedIndex = 0;
                fetchYears();
            })
            .catch(error => console.error('Error fetching values:', error));
    }

    function fetchYears() {
        const stationId = stationDropdown.value;
        fetch(`/api/stations/${stationId}/years/`)
            .then(response => response.json())
            .then(data => {
                yearDropdown.innerHTML = "";  // clear previous options
                data.forEach(year => {
                    const option = document.createElement("option");
                    option.value = year;
                    option.textContent = year;
                    yearDropdown.appendChild(option);
                });
                if (yearDropdown.options.length > 0) yearDropdown.selectedIndex = 0;
                fetchDataAndRenderYearlyChart();
                fetchDataAndRenderSeriesChart();
            })
            .catch(error => console.error('Error fetching years:', error));
    }

    function fetchDataAndRenderYearlyChart() {
        const stationId = stationDropdown.value;
        const valueField = valueDropdown.value;
        const year = yearDropdown.value;
        const parLabel = valueDropdown.options[valueDropdown.selectedIndex].textContent;
        const parUnit = valueDropdown.options[valueDropdown.selectedIndex].getAttribute('unit');

        // check if dropdowns have valid selections
        if (!stationId || !valueField || !year) return;

        fetch(`/api/stations/${stationId}/${valueField}/${year}/data/`)
            .then(response => response.json())
            .then(data => {
                const hourlyDates = data.map(item => item.date);
                const hourlyValues = data.map(item => item.value);

                fetch(`/api/stations/${stationId}/${valueField}/percentiles/`, {
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest' // Custom header
                    }
                })
                    .then(response => response.json())
                    .then(percentiles => {
                        var currentYear = new Date(hourlyDates[0]).getFullYear();
                        var percDate = percentiles.map(d => `${currentYear}-${d.string_date_without_year}`);
                        var q10 = percentiles.map(d => d.q10);
                        var q20 = percentiles.map(d => d.q20);
                        var q30 = percentiles.map(d => d.q30);
                        var q40 = percentiles.map(d => d.q40);
                        var q50 = percentiles.map(d => d.q50);
                        var q60 = percentiles.map(d => d.q60);
                        var q70 = percentiles.map(d => d.q70);
                        var q80 = percentiles.map(d => d.q80);
                        var q90 = percentiles.map(d => d.q90);
                        var conTrace = {
                            x: percDate,
                            y:q50,
                            fill: 'None',
                            mode: 'lines',
                            line: {color: 'transparent'},
                            showlegend: false,
                            name: 'controll line',
                            hoverinfo: 'none',
                            connectgaps: true
                        }
                        var conTrace2 = {
                            x: percDate,
                            y:q30,
                            fill: 'None',
                            mode: 'lines',
                            line: {color: 'transparent'},
                            showlegend: false,
                            name: 'controll line',
                            hoverinfo: 'none',
                            connectgaps: true
                        }
                        var q10 = {
                            x: percDate,
                            y: q10,
                            line: {color: 'transparent'},
                            mode: "lines",
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,100,80,0.2)', 
                            name: 'Q10',
                            type: 'scatter',
                            hoverinfo: 'y',
                            legendgroup: 'Q10 to Q90'
                        }
                        var q30 = {
                            x: percDate,
                            y: q30,
                            line: {color: 'transparent'},
                            mode: "lines",
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,176,246,0.2)', 
                            name: 'Q30',
                            type: 'scatter',
                            hoverinfo: 'y',
                            legendgroup: 'Q30 to Q70'
                        }
                        var q70 = {
                            x: percDate,
                            y: q70,
                            line: {color: 'transparent'},
                            mode: "lines",
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,176,246,0.2)', 
                            name: 'Q70',
                            type: 'scatter',
                            hoverinfo: 'y',
                            legendgroup: 'Q30 to Q70'
                        }
                        var q90 = {
                            x: percDate,
                            y: q90,
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,100,80,0.2)', 
                            line: {color: 'transparent'},
                            mode: "lines",
                            name: 'Q90',
                            type: 'scatter',
                            hoverinfo: 'y',
                            legendgroup: 'Q10 to Q90'
                        }
                        var hourlyTrace = {
                            x: hourlyDates,
                            y: hourlyValues,
                            mode: 'lines',
                            name: 'Hourly Values',
                            line: {color: 'blue'},
                            type: 'scatter'
                        };

                        var median = {
                            x: percDate,
                            y: q50,
                            mode: 'lines',
                            name: 'Median',
                            line: {color: 'red'},
                            hoverinfo: 'y',
                            connectgaps: true
                        };

                        var allTraces = [conTrace2, q10, conTrace, q30, median, q70, q90, hourlyTrace];
                        var layout = {
                            title: `Hourly data and monthly percentiles (all measured years)`,
                            xaxis: {
                                title: `date (${year})`,
                                type: 'date',
                                range: [`${currentYear}-01-01`, `${currentYear}-12-31`],
                            },
                            yaxis: {
                                title: `${parLabel} [${parUnit}]`
                            }
                        };
                        Plotly.newPlot(yearlyChart, allTraces, layout);
                })
            }
        )
        .catch(error => console.error('Error fetching chart data:', error));
    }

    function fetchDataAndRenderSeriesChart() {
        const stationId = stationDropdown.value;
        const valueField = valueDropdown.value;
        const startDate = startPicker.selectedDates[0];
        const endDate = endPicker.selectedDates[0];
        const parLabel = valueDropdown.options[valueDropdown.selectedIndex].textContent;
        const parUnit = valueDropdown.options[valueDropdown.selectedIndex].getAttribute('unit');

        const formattedStartDate = formatDateForBackend(startDate);
        const formattedEndDate = formatDateForBackend(endDate);
        const dateRange = [startDate, endDate];

        if (!stationId || !valueField) return;
        fetch(`/api/stations/${stationId}/${valueField}/dataseries/?start=${formattedStartDate}&end=${formattedEndDate}`)
            .then(response => response.json())
            .then(responseData => {
                const minDate = responseData.min_date;
                const maxDate = responseData.max_date;
                const disable = responseData.disable_dates;
                const data = responseData.data;
                const hourlyDates = data.map(item => item.date);
                const hourlyValues = data.map(item => item.value);
                console.log(hourlyDates);

                var hourlyTrace = {
                    x: hourlyDates,
                    y: hourlyValues,
                    mode: 'lines',
                    name: 'Hourly Values',
                    line: {color: 'blue'},
                    type: 'scatter'
                };

                var layout = {
                    title: `Time series`,
                    xaxis: {
                        title: `date`,
                        type: 'date',
                        range: hourlyDates,
                    },
                    yaxis: {
                        title: `${parLabel} [${parUnit}]`
                    }
                };
                Plotly.newPlot(seriesChart, [hourlyTrace], layout);
                updateDatePicker(startPicker, endPicker, minDate, maxDate, disable, dateRange);
            }
        ).catch(error => console.error('Error fetching chart data:', error)); 
    }

    stationDropdown.addEventListener("change", function() {
        fetchValues();
        zoomToStation(stationDropdown.value);
    });

    function fetchDataAndRenderBothCharts() {
        fetchDataAndRenderYearlyChart();
        fetchDataAndRenderSeriesChart();
    }

    valueDropdown.addEventListener("change", fetchDataAndRenderBothCharts);
    yearDropdown.addEventListener("change", fetchDataAndRenderYearlyChart);
    fetchStations();
});