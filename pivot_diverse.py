import os
import re

html_path = "c:\\Users\\yukes\\Documents\\Agentic AI CRM\\index.html"
css_path = "c:\\Users\\yukes\\Documents\\Agentic AI CRM\\style.css"
js_path = "c:\\Users\\yukes\\Documents\\Agentic AI CRM\\app.js"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. HTML Replace
html = html.replace("Horilla HRMS Mock", "Diverse HRMS")
html = html.replace('<img src="https://www.horilla.com/wp-content/themes/horilla-wp-theme-main/assets/images/brand/horilla-logo-icon.ico" alt="Horilla">', '<div style="background:var(--primary-color);color:#fff;width:30px;height:30px;display:flex;align-items:center;justify-content:center;border-radius:4px;font-weight:bold;">D</div>')
html = html.replace('<h2>Horilla</h2>', '<h2>Diverse</h2>')
html = html.replace('horilla', 'diverse')
html = html.replace('Horilla', 'Diverse')

# Remove Agent Widgets
start_idx = html.find('<div class="agent-widgets">')
end_idx = html.find('<!-- RIGHT COL: KANBAN BOARD -->')
if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + html[end_idx:]

# Remove Agent Status Bar
start_agent_bar = html.find('<div class="agent-status-bar">')
end_agent_bar = html.find('</div>', html.find('</div>', start_agent_bar) + 6) + 6
if start_agent_bar != -1:
    html = html[:start_agent_bar] + html[end_agent_bar:]

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# 2. CSS Replace
css = css.replace('.horilla-', '.diverse-')
css = css.replace('grid-template-columns: 320px 1fr;', 'display: flex; flex-direction: column;')

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# 3. JS Replace
# We'll just write a fresh app.js that only has the Kanban core logic.
js_content = """// Diverse HRMS - Core Recruitment Logic
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
    card.className = 'deal-card';
    card.setAttribute('draggable', 'true');
    card.dataset.id = candidate.id;

    card.innerHTML = `
      <div class="deal-card-header">
        <span class="company-name">${candidate.name}</span>
        <span class="sentiment-badge ${candidate.sentiment}">${candidate.sentiment}</span>
      </div>
      <div class="deal-value">$${candidate.value.toLocaleString()}</div>
      <div class="deal-context">${candidate.context}</div>
      <div class="card-actions">
        <button class="btn-card-action"><ion-icon name="ellipsis-horizontal-outline"></ion-icon></button>
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
  
  const sentimentElem = document.getElementById('avgSentiment');
  if(sentimentElem) sentimentElem.textContent = 'N/A'; // No AI sentiment tracking needed

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

// Modals
document.getElementById('openAddModalBtn').addEventListener('click', () => {
  document.getElementById('addDealModal').classList.add('active');
});

document.getElementById('closeAddModalBtn').addEventListener('click', () => {
  document.getElementById('addDealModal').classList.remove('active');
});

document.getElementById('cancelAddBtn').addEventListener('click', () => {
  document.getElementById('addDealModal').classList.remove('active');
});

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

  document.getElementById('addDealModal').classList.remove('active');
  document.getElementById('newCompanyName').value = '';
  document.getElementById('newDealValue').value = '';
  renderBoard();
});

renderBoard();
"""

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)
