import psutil

def get_disk_usage():
    disk_usage={}
    partitions=psutil.disk_partitions()

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_usage[partition.mountpoint] = usage.percent
        except PermissionError:
            continue

    return disk_usage