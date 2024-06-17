# UniversityConnect

## Prototipo Tarea Intro Grupo 2

## Participantes

1. Nicolas Cepeda
2. Eduardo Sandoval
3. Martin Velasquez
4. Matias Vergara
5. Yun Zhao

## Explicación prototipo

El prototipo de se divide en dos partes, la primera es una script de python llamado DatasetHandlder.py que lee 4 archivos:
- Todas la matriculas realizadas el año 2023 en todas la universidades de Chile.
- 3 archivos con todos los alumnos egresados de enseñanza media en Chile en los años 2020, 2021, 2023

estos archivos se pueden revisar en la página de datos abiertos del [Mineduc](https://datosabiertos.mineduc.cl/)

Luego el script filtra esa data para obtener a los alumnos egresados en esos años que se matricularon y estudian de la sede casa central de la PUCV.

La segunda parte es un google colab donde se procesa esta data, mostrando gráficos con las 10 comunas con más matriculas en la PUCV y el porcentaje de alumnos que son de las comunas de Viña del Mar y Valparaíso respecto a el resto de comunas del país. Por ultimo, obtiene las 10 comunas con más matriculados y, por medio de una API de OpenStreetMap, obtiene las coordenadas de un POI para iniciar la creación de rutas hacia las coordenadas de Casa Central. Es importante destacar que algunas rutas no se dibujan hasta el final debido a que el costo computacional es muy alto y el radio de busqueda que se utilizo no cubre la totalidad del espacio, para conseguir la totalidad hay que optimizar las consultas para agilizar el cálculo y el dibujado. Falto filtrar a solo comunas de la quinta región para el dibujado por lo que aparecen comunas como Rancagua que no estan dentro del scope del proyecto.