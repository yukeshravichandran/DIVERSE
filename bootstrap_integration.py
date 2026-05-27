import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Diverse HRMS</title>
  
  <!-- Bootstrap 5 CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Ionicons -->
  <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
  <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <!-- Custom Overrides -->
  <link rel="stylesheet" href="style.css">
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
        <a href="#" class="nav-link text-white sidebar-link"><ion-icon name="home-outline" class="me-2"></ion-icon> Dashboard</a>
      </li>
      <li class="nav-item mb-1">
        <a href="#" class="nav-link text-white sidebar-link"><ion-icon name="people-outline" class="me-2"></ion-icon> Employees</a>
      </li>
      <li class="nav-item mb-1">
        <a href="#" class="nav-link active sidebar-link"><ion-icon name="briefcase-outline" class="me-2"></ion-icon> Recruitment</a>
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
          <!-- KPIs in Header -->
          <div class="d-flex border-end pe-3 me-3 d-none d-lg-flex">
            <div class="mx-3 text-center">
              <div class="text-muted text-uppercase" style="font-size:0.65rem; font-weight:600;">Active Candidates</div>
              <div class="fw-bold" id="activeDealsCount">0</div>
            </div>
            <div class="mx-3 text-center">
              <div class="text-muted text-uppercase" style="font-size:0.65rem; font-weight:600;">Avg Expected</div>
              <div class="fw-bold" id="totalPipelineValue">$0</div>
            </div>
            <div class="mx-3 text-center">
              <div class="text-muted text-uppercase" style="font-size:0.65rem; font-weight:600;">Hires This Month</div>
              <div class="fw-bold" id="closedWonValue">0</div>
            </div>
          </div>
          
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

    <!-- Page Content -->
    <div class="p-4 overflow-auto flex-grow-1">
      <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h4 class="mb-0 fw-bold">Recruitment Pipeline</h4>
          <span class="text-muted small">Manage candidates and workflow</span>
        </div>
        <button class="btn btn-primary d-flex align-items-center gap-2" data-bs-toggle="modal" data-bs-target="#addDealModal">
          <ion-icon name="add-outline"></ion-icon> Add Candidate
        </button>
      </div>

      <!-- Kanban Board (Bootstrap Grid) -->
      <div class="row flex-nowrap overflow-auto pb-3 h-100" style="min-height: 500px;">
        
        <!-- Column 1 -->
        <div class="col column" data-stage="Applied" style="min-width: 280px; max-width: 320px;">
          <div class="card h-100 border-0 bg-transparent">
            <div class="card-header bg-transparent border-bottom-0 pb-0 d-flex justify-content-between align-items-center">
              <h6 class="mb-0 fw-semibold d-flex align-items-center gap-2">
                <span class="rounded-circle bg-secondary" style="width:8px;height:8px;"></span> Applied
              </h6>
              <span class="badge bg-white text-dark border" id="count-Applied">0</span>
            </div>
            <div class="card-body px-2 py-3 cards-container" id="cards-Applied">
            </div>
          </div>
        </div>

        <!-- Column 2 -->
        <div class="col column" data-stage="Screening" style="min-width: 280px; max-width: 320px;">
          <div class="card h-100 border-0 bg-transparent">
            <div class="card-header bg-transparent border-bottom-0 pb-0 d-flex justify-content-between align-items-center">
              <h6 class="mb-0 fw-semibold d-flex align-items-center gap-2">
                <span class="rounded-circle" style="width:8px;height:8px;background-color:#6f42c1;"></span> Screening
              </h6>
              <span class="badge bg-white text-dark border" id="count-Screening">0</span>
            </div>
            <div class="card-body px-2 py-3 cards-container" id="cards-Screening">
            </div>
          </div>
        </div>

        <!-- Column 3 -->
        <div class="col column" data-stage="Interviewing" style="min-width: 280px; max-width: 320px;">
          <div class="card h-100 border-0 bg-transparent">
            <div class="card-header bg-transparent border-bottom-0 pb-0 d-flex justify-content-between align-items-center">
              <h6 class="mb-0 fw-semibold d-flex align-items-center gap-2">
                <span class="rounded-circle bg-warning" style="width:8px;height:8px;"></span> Interviewing
              </h6>
              <span class="badge bg-white text-dark border" id="count-Interviewing">0</span>
            </div>
            <div class="card-body px-2 py-3 cards-container" id="cards-Interviewing">
            </div>
          </div>
        </div>

        <!-- Column 4 -->
        <div class="col column" data-stage="Offered" style="min-width: 280px; max-width: 320px;">
          <div class="card h-100 border-0 bg-transparent">
            <div class="card-header bg-transparent border-bottom-0 pb-0 d-flex justify-content-between align-items-center">
              <h6 class="mb-0 fw-semibold d-flex align-items-center gap-2">
                <span class="rounded-circle bg-primary" style="width:8px;height:8px;"></span> Offered
              </h6>
              <span class="badge bg-white text-dark border" id="count-Offered">0</span>
            </div>
            <div class="card-body px-2 py-3 cards-container" id="cards-Offered">
            </div>
          </div>
        </div>

        <!-- Column 5 -->
        <div class="col column" data-stage="Hired" style="min-width: 280px; max-width: 320px;">
          <div class="card h-100 border-0 bg-transparent">
            <div class="card-header bg-transparent border-bottom-0 pb-0 d-flex justify-content-between align-items-center">
              <h6 class="mb-0 fw-semibold d-flex align-items-center gap-2">
                <span class="rounded-circle bg-success" style="width:8px;height:8px;"></span> Hired
              </h6>
              <span class="badge bg-white text-dark border" id="count-Hired">0</span>
            </div>
            <div class="card-body px-2 py-3 cards-container" id="cards-Hired">
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</div>

<!-- Bootstrap Modal -->
<div class="modal fade" id="addDealModal" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title fw-bold">Add New Candidate</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">
        <div class="mb-3">
          <label class="form-label text-muted small fw-bold text-uppercase">Candidate Name</label>
          <input type="text" class="form-control" id="newCompanyName" placeholder="e.g. John Doe">
        </div>
        <div class="mb-3">
          <label class="form-label text-muted small fw-bold text-uppercase">Expected Salary ($)</label>
          <input type="number" class="form-control" id="newDealValue" placeholder="e.g. 75000">
        </div>
        <div class="mb-3">
          <label class="form-label text-muted small fw-bold text-uppercase">Stage</label>
          <select class="form-select" id="newDealStage">
            <option value="Applied">Applied</option>
            <option value="Screening">Screening</option>
            <option value="Interviewing">Interviewing</option>
            <option value="Offered">Offered</option>
            <option value="Hired">Hired</option>
          </select>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-light border" data-bs-dismiss="modal">Cancel</button>
        <button type="button" class="btn btn-primary" id="saveNewDealBtn">Save Candidate</button>
      </div>
    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="app.js"></script>
</body>
</html>
"""

css_content = """
:root {
  --primary-color: #246dec;
  --sidebar-bg: #1e1e2d;
  --sidebar-hover: #1b1b28;
}

body {
  font-family: 'Poppins', sans-serif;
}

.sidebar-bg {
  background-color: var(--sidebar-bg);
}

.sidebar-link {
  font-size: 0.95rem;
  font-weight: 500;
  border-radius: 6px;
  display: flex;
  align-items: center;
  transition: all 0.2s;
}

.sidebar-link ion-icon {
  font-size: 1.25rem;
}

.sidebar-link:hover {
  background-color: var(--sidebar-hover);
}

.nav-pills .nav-link.active, .nav-pills .show>.nav-link {
  background-color: var(--sidebar-hover) !important;
  color: var(--primary-color) !important;
  border-left: 3px solid var(--primary-color);
  border-radius: 0;
}

.search-bar {
  width: 300px;
}

.btn-primary {
  background-color: var(--primary-color);
  border-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: #1e5bbd;
  border-color: #1e5bbd;
}

/* Kanban specific styles */
.deal-card {
  cursor: grab;
  transition: all 0.2s ease;
}

.deal-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 .5rem 1rem rgba(0,0,0,.15)!important;
}

.deal-card.dragging {
  opacity: 0.5;
}

.column {
  transition: background-color 0.2s ease;
}

.column.drag-over {
  background-color: rgba(36, 109, 236, 0.05);
  border-radius: 8px;
}
"""

js_content = """// Diverse HRMS - Core Recruitment Logic (Bootstrap Integrated)
const candidates = [
  { id: 1, name: "John Doe", value: 75000, stage: "Applied", sentiment: "positive", context: "Applied for Software Engineer role." },
  { id: 2, name: "Jane Smith", value: 85000, stage: "Screening", sentiment: "neutral", context: "Pending initial technical screen." },
  { id: 3, name: "Bob Lee", value: 65000, stage: "Interviewing", sentiment: "positive", context: "Completed round 2." },
  { id: 4, name: "Alice Green", value: 90000, stage: "Offered", sentiment: "positive", context: "Offer sent, awaiting signature." },
];

const cardsContainers = {
  'Applied': document.getElementById('cards-Applied'),
  'Screening': document.getElementById('cards-Screening'),
  'Interviewing': document.getElementById('cards-Interviewing'),
  'Offered': document.getElementById('cards-Offered'),
  'Hired': document.getElementById('cards-Hired'),
};

const countsElements = {
  'Applied': document.getElementById('count-Applied'),
  'Screening': document.getElementById('count-Screening'),
  'Interviewing': document.getElementById('count-Interviewing'),
  'Offered': document.getElementById('count-Offered'),
  'Hired': document.getElementById('count-Hired'),
};

function renderBoard() {
  Object.keys(cardsContainers).forEach(stage => {
    cardsContainers[stage].innerHTML = '';
    countsElements[stage].textContent = '0';
  });

  let counts = { 'Applied': 0, 'Screening': 0, 'Interviewing': 0, 'Offered': 0, 'Hired': 0 };
  let activeCount = 0;
  let salarySum = 0;
  let hireCount = 0;

  candidates.forEach(candidate => {
    counts[candidate.stage]++;
    if (candidate.stage !== 'Hired') {
      activeCount++;
      salarySum += candidate.value;
    } else {
      hireCount++;
    }

    const card = document.createElement('div');
    // Bootstrap Card structure
    card.className = 'card shadow-sm mb-3 deal-card border-0';
    card.setAttribute('draggable', 'true');
    card.dataset.id = candidate.id;

    // Badge styling based on sentiment
    let badgeClass = 'bg-secondary';
    if(candidate.sentiment === 'positive') badgeClass = 'bg-success';
    if(candidate.sentiment === 'neutral') badgeClass = 'bg-warning text-dark';
    if(candidate.sentiment === 'at-risk') badgeClass = 'bg-danger';

    card.innerHTML = `
      <div class="card-body p-3">
        <div class="d-flex justify-content-between align-items-start mb-2">
          <h6 class="card-title fw-bold mb-0">${candidate.name}</h6>
          <span class="badge ${badgeClass}">${candidate.sentiment}</span>
        </div>
        <h5 class="text-primary fw-bold mb-2">$${candidate.value.toLocaleString()}</h5>
        <p class="card-text text-muted small lh-sm mb-3" style="display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;">${candidate.context}</p>
        <div class="d-flex justify-content-end border-top pt-2 mt-2">
          <button class="btn btn-sm btn-link text-muted p-0"><ion-icon name="ellipsis-horizontal-outline"></ion-icon></button>
        </div>
      </div>
    `;

    card.addEventListener('dragstart', handleDragStart);
    card.addEventListener('dragend', handleDragEnd);

    if (cardsContainers[candidate.stage]) {
      cardsContainers[candidate.stage].appendChild(card);
    }
  });

  Object.keys(countsElements).forEach(stage => {
    countsElements[stage].textContent = counts[stage];
  });

  const avgSalary = activeCount > 0 ? Math.round(salarySum / activeCount) : 0;
  
  document.getElementById('activeDealsCount').textContent = activeCount;
  document.getElementById('totalPipelineValue').textContent = '$' + avgSalary.toLocaleString();
  document.getElementById('closedWonValue').textContent = hireCount;

  Object.values(cardsContainers).forEach(container => {
    const column = container.parentElement;
    column.addEventListener('dragover', handleDragOver);
    column.addEventListener('dragleave', handleDragLeave);
    column.addEventListener('drop', handleDrop);
  });
}

function handleDragStart(e) {
  e.target.classList.add('dragging');
  e.dataTransfer.setData('text/plain', e.target.dataset.id);
}

function handleDragEnd(e) {
  e.target.classList.remove('dragging');
  Object.values(cardsContainers).forEach(c => c.parentElement.classList.remove('drag-over'));
}

function handleDragOver(e) {
  e.preventDefault();
  const column = e.currentTarget;
  column.classList.add('drag-over');
}

function handleDragLeave(e) {
  const column = e.currentTarget;
  column.classList.remove('drag-over');
}

function handleDrop(e) {
  e.preventDefault();
  const column = e.currentTarget;
  column.classList.remove('drag-over');
  const cardId = e.dataTransfer.getData('text/plain');
  const targetStage = column.dataset.stage;

  const candidate = candidates.find(c => c.id == cardId);
  if (candidate && candidate.stage !== targetStage) {
    candidate.stage = targetStage;
    renderBoard();
  }
}

// Bootstrap Modal save logic
document.getElementById('saveNewDealBtn').addEventListener('click', () => {
  const name = document.getElementById('newCompanyName').value;
  const val = parseInt(document.getElementById('newDealValue').value) || 0;
  const stage = document.getElementById('newDealStage').value;

  if (name.trim() === '') return;

  candidates.push({
    id: Date.now(),
    name: name,
    value: val,
    stage: stage,
    sentiment: 'neutral',
    context: 'Manually added candidate.'
  });

  // Use Bootstrap's native Modal API to close it
  const myModalEl = document.getElementById('addDealModal');
  const modal = bootstrap.Modal.getInstance(myModalEl);
  if(modal) {
    modal.hide();
  }

  document.getElementById('newCompanyName').value = '';
  document.getElementById('newDealValue').value = '';
  renderBoard();
});

renderBoard();
"""

html_path = "c:\\Users\\yukes\\Documents\\Agentic AI CRM\\index.html"
css_path = "c:\\Users\\yukes\\Documents\\Agentic AI CRM\\style.css"
js_path = "c:\\Users\\yukes\\Documents\\Agentic AI CRM\\app.js"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)
    
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

