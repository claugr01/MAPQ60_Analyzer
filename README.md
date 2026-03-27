# SAM MAPQ60 Analyzer

Este repositorio contiene una herramienta de procesamiento de archivos SAM (Sequence Alignment Map) desarrollada en Python. El objetivo principal es filtrar alineamientos de alta calidad basándose en el valor MAPQ=60 y presentar estadísticas de forma clara.


## 📂 Estructura del Proyecto

- main.py: script principal en Python que procesa el archivo SAM.
- main.nf: workflow de Nextflow que ejecuta el análisis.
- pyproject.toml: configuración de dependencias gestionada por uv.

---

## 🛠️ Requisitos Previos

Asegúrate de tener instalados los siguientes componentes:
1. *Python 3.12+*
2. *uv*: 
3. *Nextflow*: 

---

## 🚀 Instalación y Configuración

1. *Clonar el repositorio:*
```bash
   git clone [https://github.com/TU_USUARIO/proyecto-sam.git](https://github.com/TU_USUARIO/proyecto-sam.git)
   cd proyecto-sam
```


2. *Modo de uso*

*Opción A) Ejecución directa con uv*

```bash
uv run main.py path/archivo.sam
```


*Opción B) Ejecución con nextflow*

```bash
nextflow run main.nf --sam path/archivo_sam
```

## Salida esperada

El programa ignorará las cabeceras (@), contará las lecturas totales y nos indicará el número y porcentaje de lecturas con un alineamiento de alta calidad (MAPQ=60)


## Ejemplo de ejecución

*Ej: Ejecución directa con uv*

```bash
uv run main.py prueba.sam 
```


*Ej: Ejecución con Nextflow*

```bash
nextflow run main.nf --sam ~/sam_project/prueba.sam  
```
