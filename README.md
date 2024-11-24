<!-- PROJECT SHIELDS -->
![Contributors](https://img.shields.io/badge/Contributors-2-brightgreen?style=for-the-badge)
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

# Crawlers

Proyecto de laboratorio enfocado en la elaboración y programación de un rastreador web (web crawler). Este proyecto utiliza Python y diversas bibliotecas para extraer información de dos sitios web: la Wikipedia en inglés y la página oficial de la ESI, almacenando los datos en una base de datos SQLite y visualizándolos con colores personalizados en la consola.

## Tabla de Contenidos
1. [Descripción General](#descripcion-general)
2. [Características del Crawler](#caracteristicas-del-crawler)
3. [Requisitos del Proyecto](#requisitos-del-proyecto)
4. [Tecnologías Utilizadas](#tecnologias-utilizadas)
5. [Cómo Ejecutar el Proyecto](#como-ejecutar-el-proyecto)
6. [Contacto](#contacto)

---

## Descripción General

El proyecto es un rastreador web que automatiza la extracción de datos de páginas específicas. Incluye:

- **Extracción de datos de Wikipedia y la página de la ESI**:
  - Títulos principales, secciones específicas, contenido destacado e imágenes.
  - Almacenamiento de los datos en una base de datos SQLite.
- **Impresión de los resultados en la consola**:
  - Visualización de los datos con colores y estilos utilizando la biblioteca `colorama`.
- **Diseño modular**:
  - Implementación separada de funciones para solicitudes HTTP, análisis HTML, almacenamiento y visualización de datos.

<p align="right">(<a href="#">volver arriba</a>)</p>

---

## Características del Crawler

El crawler implementado incluye las siguientes funcionalidades:

1. **Obtención de páginas web**:
   - Uso de la biblioteca `requests` para realizar solicitudes HTTP a las URLs especificadas.

2. **Análisis HTML**:
   - Uso de `BeautifulSoup` para analizar y extraer datos específicos como títulos, imágenes y secciones de contenido.

3. **Almacenamiento de datos**:
   - Los datos extraídos se almacenan en una base de datos SQLite, organizada por tablas.

4. **Impresión estilizada en consola**:
   - Uso de `colorama` para agregar colores y mejorar la legibilidad de la salida.

<p align="right">(<a href="#">volver arriba</a>)</p>

---

## Requisitos del Proyecto

### Bibliotecas necesarias

El proyecto requiere las siguientes bibliotecas de Python, que se pueden instalar ejecutando:

```bash
pip install requests beautifulsoup4 colorama
```

---


## Contacto

Equipo de Desarrollo:
- Jesús García-Peñuela Molina-Prados
- Ángela Gijón Flores
  
Correo Electrónico: [jesuusgpmp14.2002@gmail.com](mailto:jesuusgpmp14.2002@gmail.com)

<p align="right">(<a href="#">volver arriba</a>)</p>


[forks-shield]: https://img.shields.io/github/forks/JESUSGPMP14/Crawler.svg?style=for-the-badge
[forks-url]: https://github.com/JESUSGPMP14/Crawler/network/members
[stars-shield]: https://img.shields.io/github/stars/JESUSGPMP14/Crawler.svg?style=for-the-badge
[stars-url]: https://github.com/JESUSGPMP14/Crawler/stargazers
[issues-shield]: https://img.shields.io/github/issues/JESUSGPMP14/Crawler.svg?style=for-the-badge
[issues-url]: https://github.com/JESUSGPMP14/Crawler/issues
