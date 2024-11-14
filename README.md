# Proyecto de Pipeline de Limpieza de Datos

La limpieza de datos, como seguramente sabes, es necesaria pero bastante intimidante, especialmente cuando se trata de conjuntos de datos del mundo real. Este proyecto tiene como objetivo construir un pipeline de limpieza de datos que limpie automáticamente conjuntos de datos crudos, manejando valores faltantes, formateando datos y detectando valores atípicos.

## Enfoque del Proyecto

### 1. **Manipulación de Datos**
   Aplicar transformaciones para limpiar los conjuntos de datos. Esto incluye tareas como:
   - Imputación de valores faltantes.
   - Conversión de tipos de datos.
   - Normalización de formatos (por ejemplo, fechas, cadenas).

### 2. **Manejo de Errores**
   Abordar posibles errores durante el proceso de limpieza. El pipeline debería poder manejar:
   - Errores al procesar columnas o valores inesperados.
   - Datos faltantes o mal formateados.

### 3. **Diseño de Código Modular**
   Crear funciones reutilizables para diferentes tareas de limpieza. El código está diseñado de manera modular para facilitar su mantenimiento y reutilización. Las funciones pueden ser fácilmente modificadas o extendidas para proyectos futuros.

## Tecnologías Usadas
Este proyecto hace uso principalmente de la librería **pandas** para la manipulación de datos.

- **pandas**: Para cargar, limpiar y transformar los datos.

## Funcionalidades

- Limpieza automática de datos crudos.
- Manejo de valores faltantes.
- Formateo y normalización de datos.
- Detección de valores atípicos (outliers).
- Registro de acciones de limpieza y errores.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
