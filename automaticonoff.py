import os
import time
from datetime import datetime

# User Inputs
on_time = input("Enter ON time (HH:MM AM/PM): ")
off_time = input("Enter OFF time (HH:MM AM/PM): ")

# Formatting Fix
on_time = on_time.replace(".", ":").upper()
off_time = off_time.replace(".", ":").upper()

print("\n===== SYSTEM SCHEDULER =====")
print("System ON Time :", on_time)
print("System OFF Time:", off_time)
print("============================\n")

print("Scheduler Running...\n")

while True:
    current_time = datetime.now().strftime("%I:%M %p")

    print("Current Time:", current_time)

    # OFF condition
    if current_time == off_time:
        print("System shutting down...")
        os.system("shutdown /s /t 1")
        break

    time.sleep(10)
