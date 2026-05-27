import schedule
import time
import subprocess

def job():

    print("\nRunning market data pipeline...\n")

    subprocess.run(
        ["venv\\Scripts\\python.exe", "data_pipeline/fetch_data.py"]
    )

# Run every 5 minutes
schedule.every(1).minutes.do(job)

print("Scheduler started...")

# Keep scheduler running
while True:

    schedule.run_pending()

    time.sleep(1)