# countries-shapes-generator

[![version][version_badge]][changelog]
[![CodeFactor][codefactor_badge]](https://www.codefactor.io/repository/github/regorxxx/Countries-Shapes-Generator/overview/main)
[![Codacy Badge][codacy_badge]](https://www.codacy.com/gh/regorxxx/Countries-Shapes-Generator/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=regorxxx/countries-shapes-generatorn&amp;utm_campaign=Badge_Grade)
![GitHub](https://img.shields.io/github/license/regorxxx/Countries-Shapes-Generator)  
A python script to generate country shapes in multiple [projections](https://scitools.org.uk/cartopy/docs/latest//reference/projections.html) compatible in size with world maps (i.e. meant to be used as layers). Output as png files.

## Usage
Put file into a folder, for example at 'countries-shapes-generator'. Then run on python:
```
python countries-shapes-generator.py
```
As output multiple sub-folders will be created, one per projection:

IMAGE FOLDERS

Every country will have an associated file by its [ISO 3166-1 alfa-3 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) (i.e. Canada -> CAN).
Also 2 world maps image files will be available: 'worldmap_shapes' ad 'worldmap_natural'. They should be size-compatible with all the other files.

IMAGE FILES

Python docstrings are available for all the functions. Output may be configured for any [projection](https://scitools.org.uk/cartopy/docs/latest//reference/projections.html) when importing the file and running the main function manually.

## Real World Implementation
You can find such examples in this foobar2000's script:

 1. [World-Map-SMP](https://github.com/regorxxx/World-Map-SMP): displays current artist's country on the world map and lets you generate autoplaylists based on selection.

GIF

[changelog]: CHANGELOG.md
[version_badge]: https://img.shields.io/github/release/regorxxx/Countries-Shapes-Generator.svg
[codacy_badge]: https://api.codacy.com/project/badge/Grade/1e7a52c1cd0e406f9c46357d21f7bfac
[codefactor_badge]: https://www.codefactor.io/repository/github/regorxxx/Countries-Shapes-Generator/badge/main
