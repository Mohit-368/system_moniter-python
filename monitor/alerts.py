from config import CPU_THRESHOLD, RAM_THRESHOLD, DISK_THRESHOLD

def check_alerts(cpu_usage,ram_usage,disk_usages):
    alerts=[]

    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"CPU usage high: {cpu_usage}%")

    if ram_usage > RAM_THRESHOLD:
        alerts.append(f"RAM usage high: {ram_usage}%")

    for mount ,usage in disk_usages.items():
        if usage > DISK_THRESHOLD:
            alerts.append(
                f"Disk usage high on {mountpoint}: {usage}%"
            )
    return alerts
