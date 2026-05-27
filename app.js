// Diverse HRMS - Dashboard Chart Logic

document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Attendance Chart (Bar Chart)
    const ctxAttendance = document.getElementById('attendanceChart');
    if (ctxAttendance) {
        new Chart(ctxAttendance, {
            type: 'bar',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [
                    {
                        label: 'Present',
                        data: [142, 145, 140, 143, 138, 0, 0],
                        backgroundColor: '#246dec',
                        borderRadius: 4
                    },
                    {
                        label: 'Absent/Leave',
                        data: [8, 5, 10, 7, 12, 150, 150],
                        backgroundColor: '#e2e8f0',
                        borderRadius: 4
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: { boxWidth: 12, usePointStyle: true }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        stacked: true,
                        grid: { borderDash: [4, 4], display: true }
                    },
                    x: {
                        stacked: true,
                        grid: { display: false }
                    }
                }
            }
        });
    }

    // 2. Department Chart (Doughnut)
    const ctxDepartment = document.getElementById('departmentChart');
    if (ctxDepartment) {
        new Chart(ctxDepartment, {
            type: 'doughnut',
            data: {
                labels: ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance'],
                datasets: [{
                    data: [65, 35, 25, 10, 15],
                    backgroundColor: [
                        '#246dec', // primary
                        '#6f42c1', // purple
                        '#10b981', // green
                        '#f59e0b', // yellow
                        '#0ea5e9'  // light blue
                    ],
                    borderWidth: 0,
                    hoverOffset: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '75%',
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { boxWidth: 10, usePointStyle: true, padding: 20 }
                    }
                }
            }
        });
    }
});
