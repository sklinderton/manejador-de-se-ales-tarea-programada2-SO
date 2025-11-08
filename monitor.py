import psutil
import csv
import time
from datetime import datetime


def main():
    output_file = "OUTPUT.csv"

    # Encabezados del CSV
    headers = [
        "timestamp",
        "cpu_percent",
        "cpu_interrupts",
        "virtual_memory_total",
        "virtual_memory_available",
        "virtual_memory_used",
        "virtual_memory_percent",
        "swap_total",
        "swap_used",
        "swap_percent",
        "disk_usage_total",
        "disk_usage_used",
        "disk_usage_percent",
        "net_bytes_sent",
        "net_bytes_recv"
    ]

    # Crear archivo CSV y escribir encabezado UNA sola vez
    try:
        with open(output_file, "x", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
    except FileExistsError:
        pass  # Si ya existe, se utiliza el mismo sin borrarlo

    print("Comenzando monitoreo... (Presiona CTRL + C para detener)")

    while True:
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_interrupts = psutil.cpu_stats().interrupts

            vm = psutil.virtual_memory()
            swap = psutil.swap_memory()
            disk = psutil.disk_usage("/")
            net = psutil.net_io_counters()

            row = [
                timestamp,
                cpu_percent,
                cpu_interrupts,
                vm.total,
                vm.available,
                vm.used,
                vm.percent,
                swap.total,
                swap.used,
                swap.percent,
                disk.total,
                disk.used,
                disk.percent,
                net.bytes_sent,
                net.bytes_recv
            ]

            with open(output_file, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(row)

            time.sleep(10)  # Esperar 10 segundos

        except KeyboardInterrupt:
            print("\nMonitoreo detenido por el usuario.")
            break


if __name__ == "__main__":
    main()
