import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Horilla HRMS Mock</title>
  <link rel="stylesheet" href="style.css">
  <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
  <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>

  <div class="horilla-layout">
    
    <!-- LEFT SIDEBAR -->
    <aside class="horilla-sidebar">
      <div class="sidebar-brand">
        <img src="https://www.horilla.com/wp-content/themes/horilla-wp-theme-main/assets/images/brand/horilla-logo-icon.ico" alt="Horilla">
        <h2>Horilla</h2>
      </div>
      <ul class="sidebar-menu">
        <li><a href="#"><ion-icon name="home-outline"></ion-icon> Dashboard</a></li>
        <li><a href="#"><ion-icon name="people-outline"></ion-icon> Employees</a></li>
        <li class="active"><a href="#"><ion-icon name="briefcase-outline"></ion-icon> Recruitment</a></li>
        <li><a href="#"><ion-icon name="time-outline"></ion-icon> Attendance</a></li>
        <li><a href="#"><ion-icon name="calendar-outline"></ion-icon> Leave</a></li>
        <li><a href="#"><ion-icon name="cash-outline"></ion-icon> Payroll</a></li>
        <li><a href="#"><ion-icon name="settings-outline"></ion-icon> Settings</a></li>
      </ul>
    </aside>

    <!-- MAIN CONTENT WRAPPER -->
    <div class="horilla-main">
      
      <!-- TOP NAVBAR -->
      <header class="horilla-topbar">
        <div class="topbar-left">
          <button class="menu-toggle"><ion-icon name="menu-outline"></ion-icon></button>
          <div class="search-box">
            <ion-icon name="search-outline"></ion-icon>
            <input type="text" placeholder="Search...">
          </div>
        </div>
        <div class="topbar-right">
          <div class="header-metrics">
            <div class="metric">
              <span class="metric-label">Active Candidates</span>
              <strong id="activeDealsCount">0</strong>
            </div>
            <div class="metric">
              <span class="metric-label">Avg Exp. Salary</span>
              <strong id="totalPipelineValue">$0</strong>
            </div>
            <div class="metric">
              <span class="metric-label">Hires This Month</span>
              <strong id="closedWonValue">0</strong>
            </div>
            <div class="metric">
              <span class="metric-label">Candidate Sentiment</span>
              <strong id="avgSentiment">0.0</strong>
            </div>
          </div>
          <button class="icon-btn"><ion-icon name="notifications-outline"></ion-icon></button>
          <div class="user-profile">
            <div class="avatar">A</div>
            <span>Admin</span>
            <ion-icon name="chevron-down-outline"></ion-icon>
          </div>
        </div>
      </header>

      <!-- PAGE CONTENT -->
      <main class="horilla-content">
        
        <div class="page-header">
          <div>
            <h1>Recruitment Pipeline</h1>
            <p>Manage candidates and automated outreach.</p>
          </div>
          <div class="page-actions">
            <div class="agent-status-bar">
              <div class="agent-indicator">
                <div class="status-dot pulsing"></div>
                Agentic AI Active
              </div>
            </div>
            <button class="btn-primary" id="openAddModalBtn">
              <ion-icon name="add-outline"></ion-icon> Add Candidate
            </button>
          </div>
        </div>

        <div class="recruitment-grid">
          
          <!-- LEFT COL: SIMULATOR & AGENT (Instead of a full column, it's a widget on the left) -->
          <div class="agent-widgets">
            <div class="widget-card simulator-box">
              <h3 class="widget-title"><ion-icon name="chatbubbles-outline"></ion-icon> Inbox Simulator</h3>
              <div class="select-wrapper">
                <select id="liveMessageSelect">
                  <option value="" disabled selected>Select an incoming message...</option>
                </select>
              </div>
              <textarea id="customMessageText" placeholder="Or type a custom message..."></textarea>
              <button id="runAgentBtn" class="btn-primary">
                <ion-icon name="flash-outline"></ion-icon> Run Agent Workflow
              </button>
            </div>

            <div class="widget-card console-box" id="agentConsole">
              <div class="console-header">
                <span>Agent Workflow Logs</span>
                <button id="clearLogsBtn" class="btn-icon" style="background:none;border:none;color:#64748b;cursor:pointer;"><ion-icon name="trash-outline"></ion-icon></button>
              </div>
              <!-- Logs go here -->
            </div>
            
            <div class="widget-card prompt-box">
               <h3 class="widget-title"><ion-icon name="options-outline"></ion-icon> AI Studio</h3>
               <div style="display:none;">
                 <!-- Hidden to save space but required by app.js -->
                 <textarea id="triagerPrompt">Determine the candidate's intent.</textarea>
                 <textarea id="pipelinePrompt">Determine the pipeline stage.</textarea>
                 <textarea id="personalizerPrompt">Compose email.</textarea>
               </div>
               
               <!-- AI DRAFT BOARD -->
               <div class="draft-board">
                  <div class="draft-header">
                    <div class="draft-meta">
                      <ion-icon name="mail-outline"></ion-icon> Draft Output
                    </div>
                  </div>
                  <textarea id="draftTextarea" class="draft-textarea" placeholder="AI generated response will appear here..."></textarea>
                  <div class="draft-actions" style="display:flex; gap: 0.5rem; margin-top:0.5rem;">
                     <button class="btn-secondary" id="regenerateDraftBtn">Regenerate</button>
                     <button class="btn-action-primary" id="sendDraftBtn">Send Email</button>
                  </div>
               </div>
            </div>

          </div>

          <!-- RIGHT COL: KANBAN BOARD -->
          <div class="crm-container">
            <div class="crm-column column" data-stage="Applied">
              <div class="column-header">
                <div class="column-title">
                  <div class="column-dot" style="background:#64748b;"></div> Applied
                </div>
                <span class="column-count" id="count-Applied">0</span>
              </div>
              <div class="cards-container" id="cards-Applied"></div>
            </div>

            <div class="crm-column column" data-stage="Screening">
              <div class="column-header">
                <div class="column-title">
                  <div class="column-dot" style="background:#7c3aed;"></div> Screening
                </div>
                <span class="column-count" id="count-Screening">0</span>
              </div>
              <div class="cards-container" id="cards-Screening"></div>
            </div>

            <div class="crm-column column" data-stage="Interviewing">
              <div class="column-header">
                <div class="column-title">
                  <div class="column-dot" style="background:#f59e0b;"></div> Interviewing
                </div>
                <span class="column-count" id="count-Interviewing">0</span>
              </div>
              <div class="cards-container" id="cards-Interviewing"></div>
            </div>

            <div class="crm-column column" data-stage="Offered">
              <div class="column-header">
                <div class="column-title">
                  <div class="column-dot" style="background:#2563eb;"></div> Offered
                </div>
                <span class="column-count" id="count-Offered">0</span>
              </div>
              <div class="cards-container" id="cards-Offered"></div>
            </div>

            <div class="crm-column column" data-stage="Hired">
              <div class="column-header">
                <div class="column-title">
                  <div class="column-dot" style="background:#10b981;"></div> Hired
                </div>
                <span class="column-count" id="count-Hired">0</span>
              </div>
              <div class="cards-container" id="cards-Hired"></div>
            </div>
          </div>

        </div>

      </main>
    </div>
  </div>

  <!-- ADD CANDIDATE MODAL (Required by app.js) -->
  <div class="modal-overlay" id="addDealModal">
    <div class="modal-content">
      <div class="modal-header">
        <h2>Add New Candidate</h2>
        <button class="close-modal" id="closeAddModalBtn">&times;</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label>Candidate Name</label>
          <input type="text" id="newCompanyName" placeholder="e.g. John Doe">
        </div>
        <div class="form-group">
          <label>Expected Salary ($)</label>
          <input type="number" id="newDealValue" placeholder="e.g. 75000">
        </div>
        <div class="form-group">
          <label>Stage</label>
          <select id="newDealStage">
            <option value="Applied">Applied</option>
            <option value="Screening">Screening</option>
            <option value="Interviewing">Interviewing</option>
            <option value="Offered">Offered</option>
            <option value="Hired">Hired</option>
          </select>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn-secondary" id="cancelAddBtn">Cancel</button>
        <button class="btn-primary" id="saveNewDealBtn">Save Candidate</button>
      </div>
    </div>
  </div>

  <div id="toastContainer" class="toast-container"></div>
  <script src="app.js"></script>
</body>
</html>
"""

css_content = """
:root {
  --primary-color: #246dec;
  --sidebar-bg: #1e1e2d;
  --sidebar-hover: #1b1b28;
  --sidebar-text: #a1a5b7;
  --sidebar-active: #ffffff;
  
  --bg-main: #f5f8fa;
  --bg-card: #ffffff;
  --border-color: #eff2f5;
  
  --text-main: #3f4254;
  --text-muted: #7e8299;
  --text-light: #b5b5c3;
  
  --success: #50cd89;
  --warning: #ffc700;
  --danger: #f1416c;
  --info: #7239ea;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Poppins', sans-serif;
}

body {
  background-color: var(--bg-main);
  color: var(--text-main);
  overflow: hidden;
}

.horilla-layout {
  display: flex;
  height: 100vh;
  width: 100vw;
}

/* SIDEBAR */
.horilla-sidebar {
  width: 265px;
  background-color: var(--sidebar-bg);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  transition: width 0.3s;
}

.sidebar-brand {
  height: 70px;
  display: flex;
  align-items: center;
  padding: 0 25px;
  gap: 10px;
  border-bottom: 1px dashed rgba(255,255,255,0.1);
}

.sidebar-brand img {
  width: 30px;
  height: 30px;
}

.sidebar-brand h2 {
  color: #fff;
  font-size: 1.2rem;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.sidebar-menu {
  list-style: none;
  padding: 20px 0;
  flex: 1;
  overflow-y: auto;
}

.sidebar-menu li a {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 25px;
  color: var(--sidebar-text);
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
  transition: all 0.3s;
}

.sidebar-menu li a:hover {
  background-color: var(--sidebar-hover);
  color: var(--sidebar-active);
}

.sidebar-menu li.active a {
  background-color: var(--sidebar-hover);
  color: var(--primary-color);
  border-left: 3px solid var(--primary-color);
}

.sidebar-menu li a ion-icon {
  font-size: 1.2rem;
}

/* MAIN AREA */
.horilla-main {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}

/* TOPBAR */
.horilla-topbar {
  height: 70px;
  background-color: #fff;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 30px;
  flex-shrink: 0;
}

.topbar-left {
  display: flex;
  align-items: center;
  gap: 20px;
}

.menu-toggle {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: var(--text-muted);
  cursor: pointer;
}

.search-box {
  display: flex;
  align-items: center;
  background-color: var(--bg-main);
  padding: 8px 15px;
  border-radius: 6px;
  gap: 10px;
  width: 300px;
}

.search-box ion-icon {
  color: var(--text-muted);
}

.search-box input {
  border: none;
  background: none;
  outline: none;
  width: 100%;
  font-size: 0.9rem;
  color: var(--text-main);
}

.topbar-right {
  display: flex;
  align-items: center;
  gap: 25px;
}

.header-metrics {
  display: flex;
  gap: 20px;
  border-right: 1px solid var(--border-color);
  padding-right: 20px;
}

.metric {
  display: flex;
  flex-direction: column;
}

.metric-label {
  font-size: 0.7rem;
  color: var(--text-muted);
  text-transform: uppercase;
}

.metric strong {
  font-size: 1.1rem;
  color: var(--text-main);
  font-weight: 600;
}

.icon-btn {
  background: none;
  border: none;
  font-size: 1.3rem;
  color: var(--text-muted);
  cursor: pointer;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

.avatar {
  width: 35px;
  height: 35px;
  background-color: var(--primary-color);
  color: #fff;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
}

.user-profile span {
  font-weight: 500;
  font-size: 0.9rem;
}

/* CONTENT AREA */
.horilla-content {
  flex: 1;
  padding: 30px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.page-header h1 {
  font-size: 1.4rem;
  font-weight: 600;
  color: var(--text-main);
}

.page-header p {
  color: var(--text-muted);
  font-size: 0.9rem;
}

.page-actions {
  display: flex;
  align-items: center;
  gap: 15px;
}

.agent-status-bar {
  background: #fff;
  padding: 8px 15px;
  border-radius: 6px;
  border: 1px solid var(--border-color);
  font-size: 0.85rem;
  font-weight: 500;
  box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}

.agent-indicator {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--primary-color);
}

.status-dot {
  width: 8px;
  height: 8px;
  background: var(--primary-color);
  border-radius: 50%;
}

.pulsing {
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(36, 109, 236, 0.4); }
  70% { box-shadow: 0 0 0 6px rgba(36, 109, 236, 0); }
  100% { box-shadow: 0 0 0 0 rgba(36, 109, 236, 0); }
}

.btn-primary {
  background-color: var(--primary-color);
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  font-weight: 500;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-primary:hover {
  background-color: #1e5bbd;
}

.btn-secondary {
  background-color: #f5f8fa;
  color: var(--text-main);
  border: 1px solid var(--border-color);
  padding: 10px 20px;
  border-radius: 6px;
  font-weight: 500;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-action-primary {
  background-color: var(--success);
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  font-weight: 500;
  font-size: 0.9rem;
  cursor: pointer;
}

/* RECRUITMENT GRID */
.recruitment-grid {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 20px;
  flex: 1;
  min-height: 0;
}

.agent-widgets {
  display: flex;
  flex-direction: column;
  gap: 20px;
  overflow-y: auto;
  padding-right: 5px;
}

.widget-card {
  background: var(--bg-card);
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.02);
  border: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.widget-title {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-main);
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 5px;
}

select, textarea, input[type="text"], input[type="number"] {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #e4e6ef;
  border-radius: 6px;
  font-size: 0.9rem;
  background: var(--bg-main);
  color: var(--text-main);
  outline: none;
}

select:focus, textarea:focus, input:focus {
  border-color: var(--primary-color);
}

textarea {
  min-height: 80px;
  resize: vertical;
}

/* CONSOLE */
.console-box {
  background-color: #1e1e2d;
  color: #a1a5b7;
  font-family: monospace;
  font-size: 0.8rem;
  min-height: 250px;
  max-height: 350px;
  overflow-y: auto;
}

.console-header {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px dashed rgba(255,255,255,0.1);
  padding-bottom: 10px;
  margin-bottom: 10px;
  color: #fff;
  font-weight: 500;
}

.log-line {
  margin-bottom: 4px;
  line-height: 1.4;
}
.log-time { color: #565674; margin-right: 8px;}
.log-system { color: #a1a5b7; }
.log-triager { color: #7239ea; }
.log-pipeline { color: #50cd89; }
.log-personalizer { color: #009ef7; }
.log-thought { color: #565674; font-style: italic; display: block; padding-left: 10px;}

/* KANBAN BOARD */
.crm-container {
  display: flex;
  gap: 15px;
  overflow-x: auto;
  padding-bottom: 10px;
}

.crm-column {
  flex: 1;
  min-width: 250px;
  background: #f1f5f9;
  border-radius: 8px;
  padding: 15px;
  display: flex;
  flex-direction: column;
  gap: 15px;
  border: 1px solid #e2e8f0;
}

.column-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 10px;
  border-bottom: 1px solid #e2e8f0;
}

.column-title {
  font-weight: 600;
  font-size: 0.95rem;
  display: flex;
  align-items: center;
  gap: 8px;
}

.column-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.column-count {
  background: #e2e8f0;
  padding: 2px 8px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-main);
}

.cards-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
  overflow-y: auto;
}

/* CARDS */
.deal-card {
  background: #fff;
  border-radius: 8px;
  padding: 15px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  border: 1px solid var(--border-color);
  cursor: grab;
  transition: all 0.2s;
}

.deal-card:hover {
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  transform: translateY(-2px);
}

.deal-card.dragging {
  opacity: 0.5;
}

.deal-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
}

.company-name {
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--text-main);
}

.sentiment-badge {
  font-size: 0.7rem;
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 600;
  text-transform: uppercase;
}

.sentiment-badge.positive { background: #e8fff3; color: var(--success); }
.sentiment-badge.neutral { background: #fff8dd; color: var(--warning); }
.sentiment-badge.at-risk { background: #fff5f8; color: var(--danger); }

.deal-value {
  font-weight: 600;
  font-size: 1.05rem;
  color: var(--primary-color);
  margin-bottom: 5px;
}

.deal-context {
  font-size: 0.8rem;
  color: var(--text-muted);
  line-height: 1.4;
  margin-bottom: 10px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-actions {
  display: flex;
  justify-content: flex-end;
  gap: 5px;
  border-top: 1px dashed var(--border-color);
  padding-top: 8px;
}

.btn-card-action {
  background: none;
  border: none;
  color: var(--text-light);
  cursor: pointer;
  padding: 4px;
  transition: color 0.2s;
}

.btn-card-action:hover {
  color: var(--primary-color);
}

/* MODAL */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s;
}

.modal-overlay.active {
  opacity: 1;
  pointer-events: auto;
}

.modal-content {
  background: #fff;
  border-radius: 8px;
  width: 450px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  transform: translateY(20px);
  transition: transform 0.3s;
}

.modal-overlay.active .modal-content {
  transform: translateY(0);
}

.modal-header {
  padding: 20px;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h2 {
  font-size: 1.2rem;
  font-weight: 600;
}

.close-modal {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--text-muted);
}

.modal-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.form-group label {
  font-size: 0.85rem;
  font-weight: 500;
}

.modal-footer {
  padding: 20px;
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

/* TOASTS */
.toast-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  z-index: 1000;
}

.toast {
  background: #fff;
  padding: 15px 20px;
  border-radius: 6px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  border-left: 4px solid var(--primary-color);
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  font-weight: 500;
  animation: slideIn 0.3s ease-out forwards;
}

@keyframes slideIn {
  from { transform: translateX(100%); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}

.toast.success { border-left-color: var(--success); }
.toast.info { border-left-color: var(--info); }
.toast.warning { border-left-color: var(--warning); }
"""

with open("c:\\Users\\yukes\\Documents\\Agentic AI CRM\\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("c:\\Users\\yukes\\Documents\\Agentic AI CRM\\style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

