const ctx = document.getElementById('trafficChart').getContext('2d');

const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Packets per Time',
            data: [],
            borderWidth: 2,
            fill: false
        }]
    }
});

function loadData(){
    fetch("/api/traffic")
        .then(res => res.json())
        .then(data => {
            chart.data.labels = data.labels;
            chart.data.datasets[0].data = data.data;
            chart.update();
        });
}

setInterval(loadData, 2000);
