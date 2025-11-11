// Simple website code for Arduino data

// Update the badges at the top
function updateBadges(data) {
    if (!data) {
        document.getElementById('temp-value').textContent = '—';
        document.getElementById('humidity-value').textContent = '—';
        document.getElementById('last-update').textContent = '—';
        return;
    }
    
    // Show temperature and humidity
    document.getElementById('temp-value').textContent = data.tempC.toFixed(1);
    document.getElementById('humidity-value').textContent = data.humidity.toFixed(1);
    
    // Show time
    const time = new Date(data.ts).toLocaleTimeString();
    document.getElementById('last-update').textContent = time;
}

// Update the charts
function updateCharts(data) {
    if (!data || data.ts.length === 0) {
        return;
    }
    
    // Temperature chart
    const tempChart = {
        x: data.ts,
        y: data.tempC,
        type: 'scatter',
        mode: 'lines+markers',
        line: { color: 'red' },
        name: 'Temperature'
    };
    
    // Humidity chart
    const humidityChart = {
        x: data.ts,
        y: data.humidity,
        type: 'scatter',
        mode: 'lines+markers',
        line: { color: 'blue' },
        name: 'Humidity'
    };
    
    // Basic chart settings
    const layout = {
        margin: { t: 20, r: 20, b: 40, l: 50 },
        showlegend: false,
        xaxis: { type: 'date' }
    };
    
    const config = { responsive: true, displayModeBar: false };
    
    // Draw the charts
    Plotly.react('temp-chart', [tempChart], layout, config);
    Plotly.react('humidity-chart', [humidityChart], layout, config);
}

// Get data from the server and update everything
async function refreshData() {
    try {
        // Get latest reading
        const latestResponse = await fetch('/api/latest');
        const latestData = await latestResponse.json();
        updateBadges(latestData.data);
        
        // Get all data for charts
        const seriesResponse = await fetch('/api/series');
        const seriesData = await seriesResponse.json();
        updateCharts(seriesData.data);
        
    } catch (error) {
        console.log('Error getting data:', error);
    }
}

// Start everything when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Initialize empty charts
    Plotly.newPlot('temp-chart', [], {margin: {t: 20, r: 20, b: 40, l: 50}});
    Plotly.newPlot('humidity-chart', [], {margin: {t: 20, r: 20, b: 40, l: 50}});
    
    // Get data now and every 2 seconds
    refreshData();
    setInterval(refreshData, 2000);
});