import time
import logging
from monitor.email_alert import send_email_alert

from monitor.cpu import get_cpu_usage
from monitor.memory import get_memory_usage
from monitor.disk import get_disk_usage
from monitor.alerts import check_alerts
from monitor.logger import setup_logger
from config import CHECK_INTERVAL
def main():
    setup_logger()

    while True:
        cpu = get_cpu_usage()
        ram = get_memory_usage()
        disks = get_disk_usage()

        log_msg = f"CPU={cpu}% | RAM={ram}% | DISKS={disks}"
        print(log_msg)
        logging.info(log_msg)

        alerts = check_alerts(cpu, ram, disks)
        for alert in alerts:
            print(f"⚠ {alert}")
            send_email_alert(alert)
            logging.warning(alert)

        time.sleep(CHECK_INTERVAL)
if __name__ == "__main__":
    main()
