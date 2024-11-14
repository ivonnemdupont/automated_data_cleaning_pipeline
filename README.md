# Pipeline Automatizado de Limpieza de Datos

Este proyecto implementa un pipeline automatizado de limpieza de datos para procesar conjuntos de datos crudos. El pipeline se encarga de:

- Manejar valores faltantes y formatos inconsistentes
- Detectar y eliminar valores atípicos
- Registrar cada paso de limpieza para auditoría y rastreo

## Estructura del Proyecto

- `data/raw`: Datos de entrada crudos
- `data/processed`: Datos procesados y listos para análisis
- `src/data_cleaning.py`: Módulo con funciones de limpieza
- `src/main.py`: Script principal para ejecutar el pipeline
- `config.yaml`: Archivo de configuración con parámetros de limpieza
- `logs/data_cleaning.log`: Log del pipeline de limpieza

## Instalación

1. Clona el repositorio y navega al directorio:
   ```bash
   git clone https://github.com/ivonnemdupont/automated_data-cleaning-pipeline.git
   cd automated_data-cleaning-pipeline
