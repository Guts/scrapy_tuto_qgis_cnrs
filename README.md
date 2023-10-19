# Scraping du site Tutoriel QGIS et conversion au format Markdown

![Python quality basics](https://github.com/geotribu/scraping_old_site/workflows/Python%20quality%20basics/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

L'objectif est de récupérer le contenu depuis le [site du Tutoriel QGIS](https://tutoqgis.cnrs.fr/) édité par le CNRS (Julie Pierson en particulier) pour le convertir en Markdown, permettre de le servir sous forme de site statique (Mkdocs) et en faciliter ainsi la maintenance.

Découpage :

- [web scraping](https://fr.wikipedia.org/wiki/Web_scraping) avec [Scrapy](https://scrapy.org/)
- conversion et export des contenus en markdown avec [markdownify](https://pypi.org/project/markdownify/)
- structuration et génération du site web avec [Mkdocs](https://www.mkdocs.org)

## Pré-requis

- Python 3.10+
- accès réseau sur <https://tutoqgis.cnrs.fr/>
