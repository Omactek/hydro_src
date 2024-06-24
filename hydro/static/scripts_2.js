document.addEventListener("DOMContentLoaded", function() {
    const stationDropdown = document.getElementById("stationDropdown");
    const valueDropdown = document.getElementById("valueDropdown");
    const yearDropdown = document.getElementById("yearDropdown");
    const dateInput = document.getElementById("dateInput");
    const chartDiv = document.getElementById("chartDiv");
    const lineButton = document.getElementById("lineButton");
    const histogramButton = document.getElementById("histogramButton");
    const boxPlotButton = document.getElementById("boxPlotButton");

    let stationsData = {};

    var map = L.map('map').setView([49.8175, 15.4730], 7); // centered on the Czech Republic
    flatpickr('#dateRangePicker', {
        mode: "range",
        dateFormat: "Y-m-d",
        defaultDate: ["2016-10-10", "2016-10-20"]
    });

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
                fetchDataAndRenderChart();  // update the chart after updating the dropdown
                fetchDataAndRenderSeriesChart();
            })
            .catch(error => console.error('Error fetching years:', error));
    }

    function fetchDataAndRenderChart() {
        const stationId = stationDropdown.value;
        const valueField = valueDropdown.value;
        const year = yearDropdown.value;
        const parLabel = valueDropdown.options[valueDropdown.selectedIndex].textContent;
        const parUnit = valueDropdown.options[valueDropdown.selectedIndex].getAttribute('unit');

        // check if dropdowns have valid selections
        if (!stationId || !valueField || !year) return;

        fetch(`/api/${stationId}/${valueField}/${year}/data`)
            .then(response => response.json())
            .then(data => {
                const hourlyDates = data.map(item => item.date);
                const hourlyValues = data.map(item => item.value);

                fetch(`/api/${stationId}/${valueField}/percentiles`)
                    .then(response => response.json())
                    .then(percentiles => {
                        var currentYear = new Date(hourlyDates[0]).getFullYear();
                        const months = percentiles.map(item => item.month);
                        var firstDayOfMonths = percentiles.map(d => `${currentYear}-${d.month}-01T00:00:00`);
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
                            x: firstDayOfMonths,
                            y:q50,
                            fill: 'None',
                            mode: 'lines',
                            line: {color: 'transparent'},
                            showlegend: false,
                            name: 'controll line',
                            hoverinfo: 'none'
                        }
                        var conTrace2 = {
                            x: firstDayOfMonths,
                            y:q30,
                            fill: 'None',
                            mode: 'lines',
                            line: {color: 'transparent'},
                            showlegend: false,
                            name: 'controll line',
                            hoverinfo: 'none'
                        }
                        var q10 = {
                            x: firstDayOfMonths,
                            y: q10,
                            line: {color: 'transparent'},
                            mode: "lines",
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,100,80,0.2)', 
                            name: 'Q10',
                            type: 'scatter',
                            hoverinfo: 'y'
                        }
                        var q30 = {
                            x: firstDayOfMonths,
                            y: q30,
                            line: {color: 'transparent'},
                            mode: "lines",
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,176,246,0.2)', 
                            name: 'Q30',
                            type: 'scatter',
                            hoverinfo: 'y'
                        }
                        var q70 = {
                            x: firstDayOfMonths,
                            y: q70,
                            line: {color: 'transparent'},
                            mode: "lines",
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,176,246,0.2)', 
                            name: 'Q70',
                            type: 'scatter',
                            hoverinfo: 'y'
                        }
                        var q90 = {
                            x: firstDayOfMonths,
                            y: q90,
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,100,80,0.2)', 
                            line: {color: 'transparent'},
                            mode: "lines",
                            name: 'Q90',
                            type: 'scatter',
                            hoverinfo: 'y'
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
                            x: firstDayOfMonths,
                            y: q50,
                            mode: 'lines',
                            name: 'Median',
                            line: {color: 'red'},
                            hoverinfo: 'y'
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
                        Plotly.newPlot(chartDiv, allTraces, layout);
                })
            }
        )
        .catch(error => console.error('Error fetching chart data:', error));
    }

    function fetchDataAndRenderSeriesChart() {
        const stationId = stationDropdown.value;
        const valueField = valueDropdown.value;
        const year = yearDropdown.value;
        const parLabel = valueDropdown.options[valueDropdown.selectedIndex].textContent;
        const parUnit = valueDropdown.options[valueDropdown.selectedIndex].getAttribute('unit');

        if (!stationId || !valueField || !year) return;

        fetch(`/api/${stationId}/${valueField}/${year}/data`)
            .then(response => response.json())
            .then(data => {
                const hourlyDates = data.map(item => item.date);
                const hourlyValues = data.map(item => item.value);

                fetch(`/api/${stationId}/${valueField}/percentiles`)
                    .then(response => response.json())
                    .then(percentiles => {
                        var currentYear = new Date(hourlyDates[0]).getFullYear();
                        const months = percentiles.map(item => item.month);
                        var firstDayOfMonths = percentiles.map(d => `${currentYear}-${d.month}-01T00:00:00`);
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
                            x: firstDayOfMonths,
                            y:q50,
                            fill: 'None',
                            mode: 'lines',
                            line: {color: 'transparent'},
                            showlegend: false,
                            name: 'controll line',
                            hoverinfo: 'none'
                        }
                        var conTrace2 = {
                            x: firstDayOfMonths,
                            y:q30,
                            fill: 'None',
                            mode: 'lines',
                            line: {color: 'transparent'},
                            showlegend: false,
                            name: 'controll line',
                            hoverinfo: 'none'
                        }
                        var q10 = {
                            x: firstDayOfMonths,
                            y: q10,
                            line: {color: 'transparent'},
                            mode: "lines",
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,100,80,0.2)', 
                            name: 'Q10',
                            type: 'scatter',
                            hoverinfo: 'y'
                        }
                        var q30 = {
                            x: firstDayOfMonths,
                            y: q30,
                            line: {color: 'transparent'},
                            mode: "lines",
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,176,246,0.2)', 
                            name: 'Q30',
                            type: 'scatter',
                            hoverinfo: 'y'
                        }
                        var q70 = {
                            x: firstDayOfMonths,
                            y: q70,
                            line: {color: 'transparent'},
                            mode: "lines",
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,176,246,0.2)', 
                            name: 'Q70',
                            type: 'scatter',
                            hoverinfo: 'y'
                        }
                        var q90 = {
                            x: firstDayOfMonths,
                            y: q90,
                            fill: 'tonexty',
                            fillcolor: 'rgba(0,100,80,0.2)', 
                            line: {color: 'transparent'},
                            mode: "lines",
                            name: 'Q90',
                            type: 'scatter',
                            hoverinfo: 'y'
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
                            x: firstDayOfMonths,
                            y: q50,
                            mode: 'lines',
                            name: 'Median',
                            line: {color: 'red'},
                            hoverinfo: 'y'
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
                        Plotly.newPlot(chart2Div, allTraces, layout);
                })
            }
        )
        .catch(error => console.error('Error fetching chart data:', error));
    }

    stationDropdown.addEventListener("change", function() {
        fetchValues();
        zoomToStation(stationDropdown.value);
    });

    function fetchDataAndRenderBothCharts() {
        fetchDataAndRenderChart();
        fetchDataAndRenderSeriesChart();
    }

    valueDropdown.addEventListener("change", fetchDataAndRenderBothCharts);
    yearDropdown.addEventListener("change", fetchDataAndRenderChart, fetchDataAndRenderSeriesChart);

    lineButton.addEventListener("click", function() {
        currentChartType = 'line';
        fetchDataAndRenderChart();
        fetchDataAndRenderSeriesChart();
    });

    histogramButton.addEventListener("click", function() {
        currentChartType = 'histogram';
        fetchDataAndRenderChart();
        fetchDataAndRenderSeriesChart();
    });

    boxPlotButton.addEventListener("click", function() {
        currentChartType = 'box';
        fetchDataAndRenderChart();
        fetchDataAndRenderSeriesChart();
    });

    fetchStations();
});