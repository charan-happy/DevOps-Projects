let chart;

async function updateDashboard() {
    try {
        const response = await fetch('/api/weather');
        const data = await response.json();
        
        Object.entries(data).forEach(([city, info]) => {
            const card = document.getElementById(city);
            if (card) {
                card.querySelector('.temperature').textContent = `${info.temp}°C`;
                card.querySelector('.condition').textContent = info.condition;
                card.querySelector('.humidity').textContent = `Humidity: ${info.humidity}%`;
                card.querySelector('.wind').textContent = `Wind: ${info.wind} m/s`;
            }
        });

        updateChart(data);
    } catch (error) {
        console.error('Error updating dashboard:', error);
    }
}

function updateChart(data) {
    const cities = Object.keys(data);
    const temperatures = cities.map(city => data[city].temp);

    if (!chart) {
        const ctx = document.getElementById('temperatureChart').getContext('2d');
        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: cities,
                datasets: [{
                    label: 'Temperature (°C)',
                    data: temperatures,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            }
        });
    } else {
        chart.data.datasets[0].data = temperatures;
        chart.update();
    }
}

// Update every 5 minutes
setInterval(updateDashboard, 300000);
updateDashboard();