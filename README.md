🛡️ SOC Brute Force Detection using Python
📌 Project Overview

This project simulates a Security Operations Center (SOC) workflow by detecting brute-force login attacks through authentication log analysis using Python.
It identifies suspicious login failures, triggers alerts, and automatically generates an incident report.

This project is designed for Cyber Security beginners and freshers to understand real-world SOC monitoring and incident handling.

🎯 Objective
Analyze authentication logs
Detect brute-force login attempts
Generate SOC-style alerts
Create automated incident reports
🧰 Tools & Technologies Used
Python 3
Command Prompt (Windows)
Authentication Log Files
Basic SOC & Blue Team concepts
🗂️ Project Structure
SOC-Bruteforce-Detection/
│
├── incident_response.py
├── incident_report.txt
├── README.md
└── logs/
    └── auth.log
⚙️ How It Works
The script reads the auth.log file
Counts failed login attempts
Applies a threshold to detect brute-force attacks
Triggers a SOC-style alert (email simulation)
Automatically generates an incident report
🚨 Detection Logic
Failed login attempts ≥ 3 → Possible Brute Force Attack
Incident is flagged and documented automatically
📄 Sample Output

Console Output:

Total Failed Login Attempts: 5
INCIDENT DETECTED: Possible Brute Force Attack
Incident report created successfully!

Incident Report (incident_report.txt):

SOC INCIDENT REPORT
===================
Date & Time       : 2026-06-27
Log File Analyzed : logs/auth.log
Failed Attempts  : 5
Incident Status  : INCIDENT DETECTED
🧠 Skills Gained
Log analysis & monitoring
Brute-force attack detection
SOC incident workflow understanding
Python automation for cyber security
Debugging real-world file path issues
🚀 Future Enhancements
IP-based attack detection
Severity classification (Low / Medium / High)
Email alert integration
SIEM tool integration (Splunk / ELK)

👩‍💻 Author

Nishalini M
BE CSE (Cyber Security)
Aspiring Cyber Security Analyst
#CyberSecurity #SOC #Python #LogAnalysis #BlueTeam #FresherProject

