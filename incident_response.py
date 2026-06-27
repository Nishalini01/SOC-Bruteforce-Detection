# STEP 2: Detect Brute Force Login Attempts

log_file = "logs/auth.log"
failed_attempts = 0
THRESHOLD = 3   # minimum failures to consider attack

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_attempts += 1

print("Total Failed Login Attempts:", failed_attempts)

if failed_attempts >= THRESHOLD:
    print("🚨 INCIDENT DETECTED: Possible Brute Force Attack")
    incidents = True
else:
    print("✅ No Brute Force Attack Detected")
    incidents = False
from datetime import datetime

report_file = "incident_report.txt"

with open(report_file, "w") as report:
    report.write("SOC INCIDENT REPORT\n")
    report.write("===================\n")
    report.write(f"Date & Time       : {datetime.now()}\n")
    report.write(f"Log File Analyzed : logs/auth.log\n")
    report.write(f"Failed Attempts  : {failed_attempts}\n")
    report.write(f"Incident Status  : {'INCIDENT DETECTED' if incidents else 'NO INCIDENT'}\n")

print("📄 Incident report created successfully!")
