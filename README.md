# 🏗️ Multi-Agent AI Supply Chain Management System (Construction SCM)

This project demonstrates a **multi-agent system** for **supply chain management** for **civil engineering/construction** use case using **CrewAI**

### Author - Rudresh Veerappaji
---

## 📌 Overview

Agents collaborate to handle procurement, forecasting, logistics, and site material tracking.

### 🔄 Agents

1. **ForecastingAgent** → predicts demand from usage data
2. **ProcurementAgent** → places material orders from forecasts
3. **LogisticsAgent** → schedules delivery of ordered materials
4. **SiteManagerAgent** → tracks delivery and usage, updates forecast loop

### Supply Chain Management Tasks
Task flow definitions have been created and saved in the tasks/ folder:

1. **forecast_task.py** – Task is to generates material demand
2. **procure_task.py** – Task is to creates purchase orders based on forecast
3. **logistics_task.py** – Task is to arranges delivery logistics
4. **site_task.py** – Task is to tracks site confirmations and usage
5. **setup_tasks.py** – Task is to chain all tasks together for CrewAI

## 📁 Project Structure

```
construction_scm_crewai/
├── agents/           # Agent definitions
├── tasks/            # Task flows
├── tools/            # Integrations (optional)
├── data/             # CSV files for mock usage and outputs
├── configs/          # Settings/config files
├── logs/             # Optional runtime logs
├── main.py           # Entry point to run CrewAI system
├── README.md         # This file
└── agent_flowchart.png # Visualization of agent interactions
```

---

## Project architecture

### Backend:
* Hosted on Railway
* Runs CrewAI agents via Flask

### Frontend:
* Hosted on Streamlit Community Cloud
* Sends API calls to Railway backend and shows results

## ▶️ How to Run

```bash
python main.py
```

This will:
1. Load agents from `agents/setup_agents.py`
2. Set up tasks from `tasks/setup_tasks.py`
3. Launch the CrewAI multi-agent orchestration
4. Output results in `data/` folder

---

## 📊 Sample Data

- `data/material_usage_log.csv` contains mock usage history
- Outputs like `material_forecast.csv`, `purchase_orders.csv`, `delivery_schedule.csv`, etc., are generated

---

## 🚀 Next Steps

- Add tools (e.g., Google Sheets, OCR, DB integration)
- Expand agents (ComplianceAgent, FinanceAgent, etc.)
- Deploy with a Streamlit or FastAPI interface

---

Built using ❤️ with [CrewAI](https://github.com/joaomdmoura/crewAI)
