import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Diverse HRMS - Dashboard</title>
  
  <!-- Bootstrap 5 CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Ionicons -->
  <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
  <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <!-- Chart.js -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <!-- Custom Overrides -->
  <link rel="stylesheet" href="style.css">
  
  <style>
    /* Dashboard specific overrides */
    .stat-card {
      border: none;
      border-radius: 8px;
      transition: transform 0.2s;
    }
    .stat-card:hover {
      transform: translateY(-3px);
    }
    .stat-icon {
      width: 45px;
      height: 45px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
    }
    .chart-container {
      position: relative;
      height: 300px;
      width: 100%;
    }
  </style>
</head>
<body>

<div class="d-flex" style="height: 100vh;">
  <!-- Sidebar -->
  <div class="d-flex flex-column flex-shrink-0 text-white sidebar-bg" style="width: 260px;">
    <a href="/" class="d-flex align-items-center p-3 mb-3 text-white text-decoration-none border-bottom border-secondary">
      <div class="logo-box bg-primary text-white d-flex align-items-center justify-content-center rounded me-2" style="width:30px; height:30px; font-weight:bold;">D</div>
      <span class="fs-5 fw-semibold">Diverse</span>
    </a>
    <ul class="nav nav-pills flex-column mb-auto px-2">
      <li class="nav-item mb-1">
        <a href="#" class="nav-link active sidebar-link"><ion-icon name="home-outline" class="me-2"></ion-icon> Dashboard</a>
      </li>
      <li class="nav-item mb-1">
        <a href="#" class="nav-link text-white sidebar-link"><ion-icon name="people-outline" class="me-2"></ion-icon> Employees</a>
      </li>
      <li class="nav-item mb-1">
        <a href="#" class="nav-link text-white sidebar-link"><ion-icon name="briefcase-outline" class="me-2"></ion-icon> Recruitment</a>
      </li>
      <li class="nav-item mb-1">
        <a href="#" class="nav-link text-white sidebar-link"><ion-icon name="time-outline" class="me-2"></ion-icon> Attendance</a>
      </li>
      <li class="nav-item mb-1">
        <a href="#" class="nav-link text-white sidebar-link"><ion-icon name="calendar-outline" class="me-2"></ion-icon> Leave</a>
      </li>
      <li class="nav-item mb-1">
        <a href="#" class="nav-link text-white sidebar-link"><ion-icon name="cash-outline" class="me-2"></ion-icon> Payroll</a>
      </li>
    </ul>
  </div>

  <!-- Main Content -->
  <div class="d-flex flex-column flex-grow-1 overflow-hidden bg-light">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white border-bottom px-4 shadow-sm" style="height: 70px;">
      <div class="container-fluid p-0">
        <div class="d-flex align-items-center">
          <button class="btn btn-link text-dark p-0 me-3"><ion-icon name="menu-outline" class="fs-4"></ion-icon></button>
          <div class="input-group search-bar rounded bg-light border">
            <span class="input-group-text bg-transparent border-0"><ion-icon name="search-outline"></ion-icon></span>
            <input type="text" class="form-control bg-transparent border-0 shadow-none" placeholder="Search...">
          </div>
        </div>
        
        <div class="d-flex align-items-center">
          <button class="btn btn-link text-dark fs-5 p-1 me-3"><ion-icon name="notifications-outline"></ion-icon></button>
          
          <div class="dropdown">
            <a href="#" class="d-flex align-items-center text-dark text-decoration-none dropdown-toggle" data-bs-toggle="dropdown">
              <div class="bg-primary text-white rounded d-flex align-items-center justify-content-center fw-bold me-2" style="width:35px;height:35px;">A</div>
              <span class="fw-semibold">Admin</span>
            </a>
          </div>
        </div>
      </div>
    </nav>

    <!-- Page Content (Dashboard View) -->
    <div class="p-4 overflow-auto flex-grow-1">
      <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h4 class="mb-0 fw-bold">Dashboard</h4>
          <span class="text-muted small">Welcome back to Diverse HRMS</span>
        </div>
      </div>

      <!-- KPI Cards Row -->
      <div class="row g-4 mb-4">
        
        <div class="col-12 col-sm-6 col-lg-3">
          <div class="card shadow-sm stat-card h-100">
            <div class="card-body d-flex align-items-center">
              <div class="stat-icon bg-primary bg-opacity-10 text-primary me-3">
                <ion-icon name="people"></ion-icon>
              </div>
              <div>
                <h6 class="text-muted text-uppercase fw-bold mb-1" style="font-size:0.75rem;">Total Employees</h6>
                <h3 class="fw-bold mb-0">150</h3>
              </div>
            </div>
          </div>
        </div>

        <div class="col-12 col-sm-6 col-lg-3">
          <div class="card shadow-sm stat-card h-100">
            <div class="card-body d-flex align-items-center">
              <div class="stat-icon bg-success bg-opacity-10 text-success me-3">
                <ion-icon name="checkmark-circle"></ion-icon>
              </div>
              <div>
                <h6 class="text-muted text-uppercase fw-bold mb-1" style="font-size:0.75rem;">Today's Attendance</h6>
                <h3 class="fw-bold mb-0">142</h3>
              </div>
            </div>
          </div>
        </div>

        <div class="col-12 col-sm-6 col-lg-3">
          <div class="card shadow-sm stat-card h-100">
            <div class="card-body d-flex align-items-center">
              <div class="stat-icon bg-warning bg-opacity-10 text-warning me-3">
                <ion-icon name="calendar"></ion-icon>
              </div>
              <div>
                <h6 class="text-muted text-uppercase fw-bold mb-1" style="font-size:0.75rem;">Total Leaves (Today)</h6>
                <h3 class="fw-bold mb-0">5</h3>
              </div>
            </div>
          </div>
        </div>

        <div class="col-12 col-sm-6 col-lg-3">
          <div class="card shadow-sm stat-card h-100">
            <div class="card-body d-flex align-items-center">
              <div class="stat-icon bg-info bg-opacity-10 text-info me-3">
                <ion-icon name="cash"></ion-icon>
              </div>
              <div>
                <h6 class="text-muted text-uppercase fw-bold mb-1" style="font-size:0.75rem;">Total Payroll (MTD)</h6>
                <h3 class="fw-bold mb-0">$52,400</h3>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Charts Row -->
      <div class="row g-4 mb-4">
        <div class="col-12 col-lg-8">
          <div class="card shadow-sm border-0 h-100">
            <div class="card-header bg-white border-bottom-0 pt-4 pb-0">
              <h6 class="fw-bold mb-0">Attendance Overview</h6>
            </div>
            <div class="card-body">
              <div class="chart-container">
                <canvas id="attendanceChart"></canvas>
              </div>
            </div>
          </div>
        </div>
        
        <div class="col-12 col-lg-4">
          <div class="card shadow-sm border-0 h-100">
            <div class="card-header bg-white border-bottom-0 pt-4 pb-0">
              <h6 class="fw-bold mb-0">Employees by Department</h6>
            </div>
            <div class="card-body d-flex align-items-center justify-content-center">
              <div class="chart-container" style="height: 250px;">
                <canvas id="departmentChart"></canvas>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Recent Activity Row -->
      <div class="row g-4">
        <div class="col-12">
          <div class="card shadow-sm border-0">
            <div class="card-header bg-white pt-3 pb-3 d-flex justify-content-between align-items-center">
              <h6 class="fw-bold mb-0">Recent Leave Requests</h6>
              <button class="btn btn-sm btn-outline-primary">View All</button>
            </div>
            <div class="card-body p-0">
              <div class="table-responsive">
                <table class="table table-hover align-middle mb-0">
                  <thead class="table-light text-muted">
                    <tr>
                      <th class="ps-4 fw-medium small text-uppercase">Employee</th>
                      <th class="fw-medium small text-uppercase">Leave Type</th>
                      <th class="fw-medium small text-uppercase">Duration</th>
                      <th class="fw-medium small text-uppercase">Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td class="ps-4 py-3">
                        <div class="d-flex align-items-center">
                          <div class="bg-secondary text-white rounded-circle d-flex align-items-center justify-content-center me-3" style="width:35px;height:35px;font-size:0.8rem;">JD</div>
                          <div>
                            <div class="fw-bold text-dark">John Doe</div>
                            <div class="small text-muted">Engineering</div>
                          </div>
                        </div>
                      </td>
                      <td>Sick Leave</td>
                      <td>May 26 - May 27 (2 Days)</td>
                      <td><span class="badge bg-warning text-dark">Pending</span></td>
                    </tr>
                    <tr>
                      <td class="ps-4 py-3">
                        <div class="d-flex align-items-center">
                          <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center me-3" style="width:35px;height:35px;font-size:0.8rem;">AS</div>
                          <div>
                            <div class="fw-bold text-dark">Alice Smith</div>
                            <div class="small text-muted">Marketing</div>
                          </div>
                        </div>
                      </td>
                      <td>Casual Leave</td>
                      <td>May 20 (1 Day)</td>
                      <td><span class="badge bg-success">Approved</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="app.js"></script>
</body>
</html>
"""

js_content = """// Diverse HRMS - Dashboard Chart Logic

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
"""

html_path = "c:\\Users\\yukes\\Documents\\Agentic AI CRM\\index.html"
js_path = "c:\\Users\\yukes\\Documents\\Agentic AI CRM\\app.js"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)
