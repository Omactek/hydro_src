document.addEventListener("DOMContentLoaded", function() {
    flatpickr('#datePicker', {
        "minDate": new Date().fp_incr(1),
        mode: 'range',
        dateFormat: "Y-m-d",
        minDate: '2024-05-15',
        maxDate: '2024-07-26'
    }); 
});
