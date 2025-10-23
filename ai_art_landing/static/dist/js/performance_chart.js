document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('performanceChart');

    // Generate labels for all months
    function generateMonthlyLabels() {
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        const years = ['18', '19', '20', '21', '22', '23', '24'];
        const labels = [];
        
        years.forEach(year => {
            months.forEach(month => {
                labels.push(`${month} '${year}`);
            });
        });
        return labels;
    }

    const chartConfig = {
        type: 'line',
        data: {
            labels: generateMonthlyLabels(),
            datasets: [{
                label: 'TradingBot v1',
                data: window.chartData?.dataset1 || [],
                borderColor: 'rgb(0, 153, 255)',
                backgroundColor: 'rgba(0, 153, 255, 0.1)',
                borderWidth: 2,
                fill: true,
                tension: 0.4,
                pointRadius: 0,
                pointHoverRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            height: 400,
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                    align: 'start',
                    onClick: null,
                    onHover: null,
                    labels: {
                        usePointStyle: false,
                        boxWidth: 30,
                        padding: 20,
                        generateLabels: function(chart) {
                            const datasets = chart.data.datasets;
                            return datasets.map((dataset, i) => ({
                                text: dataset.label,
                                fillStyle: dataset.borderColor,
                                strokeStyle: dataset.borderColor,
                                lineWidth: 2,
                                hidden: false,
                                index: i,
                                fontColor: '#666'
                            }));
                        }
                    }
                },
                tooltip: {
                    mode: 'index',
                    intersect: false,
                    backgroundColor: 'white',
                    titleColor: '#000',
                    bodyColor: '#666',
                    borderColor: '#ddd',
                    borderWidth: 1,
                    padding: 10,
                    callbacks: {
                        label: function(context) {
                            return `${context.dataset.label}: ${context.parsed.y.toFixed(2)}%`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: {
                        display: true,
                        color: 'rgba(99, 102, 241, 0.1)'
                    },
                    ticks: {
                        maxRotation: 45,
                        minRotation: 45,
                        autoSkip: true,
                        maxTicksLimit: 12,
                        callback: function(val, index) {
                            // Show only quarterly labels
                            const label = this.getLabelForValue(val);
                            if (label.includes('Jan') || label.includes('Apr') || 
                                label.includes('Jul') || label.includes('Oct')) {
                                return label;
                            }
                            return '';
                        },
                        font: {
                            size: 11
                        }
                    }
                },
                y: {
                    grid: {
                        display: true,
                        color: 'rgba(99, 102, 241, 0.1)'
                    },
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        },
                        font: {
                            size: 11
                        }
                    },
                    min: 0,
                    max: 900
                }
            }
        }
    };
    new Chart(ctx, chartConfig);
});
