import os
import sys
from datetime import datetime  # 👈 IMPORTANTE

def analizar_logs(carpeta):

    errores = 0
    warnings = 0
    info = 0
    resultados = []
    errores_archivo = 0
    warnings_archivos = 0
    info_archivo = 0

    for archivo in os.listdir(carpeta):
        errores_archivo = 0

        if not archivo.endswith(".txt"):
            continue

        ruta = os.path.join(carpeta, archivo)

        try:
            with open(ruta, "r") as f:
                resultados.append([archivo,errores_archivo,warnings_archivos, info_archivo])
                for linea in f:

                    if "ERROR" in linea:
                        errores += 1
                        errores_archivo +=1
                    elif "WARNING" in linea:
                        warnings += 1
                        errores_archivo +=1
                    elif "INFO" in linea:
                        info += 1
                        errores_archivo +=1

                print(f"Archivo: {archivo}  - errores: {errores_archivo}")

        except Exception as e:
            print(f"No se pudo leer {archivo}: {e}")

    return errores, warnings, info, resultados


# Validación de argumento
if len(sys.argv) < 2:
    print("Uso: python3 analizador_logs.py <carpeta>")
    sys.exit()

carpeta = sys.argv[1]

# Ejecutar análisis
errores, warnings, info, resultados = analizar_logs(carpeta)

# 🔥 AQUÍ VA TU PARTE (correctamente integrada)

fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nombre_archivo = f"reportes/reporte_{fecha}.csv"

if not os.path.exists("reportes"):
          os.makedirs("reportes")

with open(nombre_archivo, "w") as f:
    f.write(f"fECHA DEL ANALISIS, {fecha}\n")
    f.write(f"Carpeta analizada{carpeta}\n\n")
    f.write("Archivo, Errores, Wanings, Info \n")

    for fila in resultados:
        f.write(f"{fila[0]},{fila[1]},{fila[2]},{fila[3]}\n")

    f.write("\n")
    f.write(f"total, {errores},{warnings},{info}\n")

#print(f"Reporte generado: {nombre_archivo}")
print("\n====================================")
print("       LOG ANALYZER TOOL")
print("====================================")

print(f"\nCarpeta analizada: {carpeta}")

print("\nResumen:")
print(f"Errores: {errores}")
print(f"Warnings: {warnings}")
print(f"Info: {info}")

print(f"\nReporte generado en:\n{nombre_archivo}")
