# System Monitor
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A **lightweight, Python-based system monitoring tool** built to track server health in real-time.
The System Monitor continuously checks CPU, RAM, and Disk usage, logging performance data and automatically dispatching email alerts when critical thresholds are exceeded.

Designed for **simplicity, reliability, and automated oversight** (SysAdmin automation, remote server monitoring, resource tracking).

---

## Table of Contents
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Installation](#-installation)
- [Environment Setup](#-environment-setup)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Logs & Outputs](#-logs--outputs)
- [Contributing](#-contributing)
- [License](#-license)

---

## Key Features
-   **Real-Time Resource Tracking**:
    Utilizes `psutil` to monitor CPU load, RAM usage, and Disk partition storage every few seconds.
-   **Automated Alerting System**:
    Instantly detects when resources breach safety limits and sends email notifications via SMTP (Gmail).
-   **Persistent Logging**:
    Maintains a historical record of system performance in `system.log` for audit and analysis purposes.
-   **Configurable Thresholds**:
    Easily adjustable sensitivity settings for CPU, RAM, and Disk usage via a central configuration file.
-   **Multi-Partition Support**:
    Dynamically discovers and monitors usage across all mounted disk partitions (e.g., `C:\`, `D:\`).

---

## Project Architecture
Based on the modular structure, the project is organized as follows:

```bash
System_Monitor/
│
├── main.py                  # Application entry point & main loop
├── config.py                # User-defined thresholds & intervals
├── system.log               # Output log file (auto-generated)
├── README.md
│
└── monitor/                 # Core monitoring logic
    ├── __init__.py
    ├── cpu.py               # CPU usage extraction
    ├── memory.py            # RAM usage extraction
    ├── disk.py              # Disk partition scanning
    ├── alerts.py            # Threshold logic & message generation
    ├── email_alert.py       # SMTP email dispatcher
    └── logger.py            # Logging configuration
```
---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/System_Monitor](https://github.com/YourUsername/System_Monitor)
    cd System_Monitor
    ```

2.  **Prerequisites:**
    This project requires Python 3.x+ and the `psutil` library for hardware monitoring.
    ```bash
    pip install psutil
    ```

3.  **Prepare Directories:**
    Ensure the directory structure matches the architecture above so `main.py` can correctly import modules.

---
## Environment Setup
To enable email alerts, you must configure environment variables for your email credentials. The application looks for the specific keys defined in `email_alert.py`:

**Linux/Mac:**
```bash
export Sender_mail@example.com="your_email@gmail.com"
export Recievers_mail@example.com="admin_email@example.com"
export EMAIL_APP_PASSWORD="your_app_password"
```
**Windows (Command Prompt):**
```
set Sender_mail@example.com="your_email@gmail.com"
set Recievers_mail@example.com="admin_email@example.com"
set EMAIL_APP_PASSWORD="your_app_password"
```
Note: If using Gmail, you must generate an "App Password" in your Google Account security settings.
---

## Usage

1.  **Run the monitor:**
    Execute the main script to start the monitoring loop.
    ```bash
    python main.py
    ```

2.  **Console Output:**
    The system will print real-time stats and alerts to the console:
    ```text
    CPU=4.9% | RAM=81.5% | DISKS={'C:\\': 55.7, 'D:\\': 0.3}
    CPU=12.1% | RAM=82.0% | DISKS={'C:\\': 55.7, 'D:\\': 0.3}
    ⚠ CPU usage high: 95.2%
    ⚠ Disk usage high on C:\: 88.0%
    ```
---

## Configuration
You can tune the sensitivity of the monitor by modifying `config.py`.

**File:** `config.py`
```python
# Resource Thresholds (Percentage)
CPU_THRESHOLD = 80
DISK_THRESHOLD = 75
RAM_THRESHOLD = 85

# Loop Interval
CHECK_INTERVAL = 5   # Seconds between checks
```
---
## Logs & Outputs
The tool automatically generates a log file in the root directory.

### System Log (`system.log`)
-   **Format:** Text / Log structure
-   **Content:**
    -   Timestamps for every check.
    -   Detailed breakdown of CPU, RAM, and individual Disk partition usage.
    -   Information on sent alerts.

**Example Entry:**
```log
2026-01-21 14:09:54,052 - INFO - CPU=4.9% | RAM=81.5% | DISKS={'C:\\': 55.7, 'D:\\': 0.3}
2026-01-21 14:10:06,059 - INFO - CPU=7.2% | RAM=81.3% | DISKS={'C:\\': 55.7, 'D:\\': 0.3}
```

---

## Contributing
Contributions are welcome! Please follow these steps:

1.  Fork the repository
2.  Create a feature branch: `git checkout -b feature/NewMonitor`
3.  Commit your changes
4.  Open a Pull Request

---

## Roadmap & Future Improvements
Here are some features planned for future releases to make the System Monitor more robust and user-friendly:

- [ ] **Web Dashboard:** Implement a lightweight web interface (using Flask or Streamlit) to visualize CPU and Memory trends with real-time graphs.
- [ ] **Multi-Channel Alerts:** Expand alerting beyond Email to include integrations for Slack, Discord, or SMS (via Twilio).
- [ ] **Database Integration:** Transition from text-based logging (`system.log`) to a local database (SQLite) to enable historical data queries and long-term analysis.
- [ ] **Background Service:** Create a setup script to run the monitor as a `systemd` service (Linux) or Windows Service, ensuring it runs automatically on boot.
- [ ] **Daily Health Reports:** specific module to generate and email a daily summary PDF of system performance statistics.

---
## License
Distributed under the **MIT License**.

---
