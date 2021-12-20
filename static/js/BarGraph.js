var xValues = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
// var yValues = [55, 49, 44, 34, 23, 38, 41];

var data = $.get('/weekdata');
data.done(function (resp) {
    console.log("JSON Data", resp.weekdata)

    var barColors = [
        'rgba(255, 99, 132, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(255, 205, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(201, 203, 207, 0.2)'
    ];

    new Chart("myBarChart", {
        type: "bar",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: barColors,
                data: resp.weekdata
            }]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: "Weekly Ticket Data"
            },
            scales: {
                yAxes: [{ ticks: { min: 10, max: 70 } }],
            }
        }
    });
})


