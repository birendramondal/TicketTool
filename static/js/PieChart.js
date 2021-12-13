var xValues = ["Resolve", "Pending", "Closed"];
var yValues = [55, 49, 44];
var barColors = [
    "#b91d47",
    "#00aba9",
    "#2b5797",
];

new Chart("myPieChart", {
    type: "pie",
    data: {
        labels: xValues,
        datasets: [{
            backgroundColor: barColors,
            data: yValues
        }]
    },
    options: {
        title: {
            display: true,
            text: "Resolver Rate"
        }
    }
});