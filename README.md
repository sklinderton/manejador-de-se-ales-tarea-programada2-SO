# Explicación:

### Este script usa psutil para obtener:

-Interrupciones de CPU (psutil.cpu_stats().interrupts)

-Memoria virtual (psutil.virtual_memory())

-CPU % usado (psutil.cpu_percent())

-Swap

-Uso de disco

-Tráfico de red (bytes enviados/recibidos)

### Cada 10 segundos, toma una muestra y la guarda en OUTPUT.csv.

### El CSV tiene encabezado (solo se escribe una vez).

## Puedes abortarlo con CTRL + C.
