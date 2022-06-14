# countries-shapes-generator
[<img src="https://user-images.githubusercontent.com/83307074/173630971-d75d3631-0711-4e7c-b494-11347fea6889.png" width=30% height=30%>](https://www.naturalearthdata.com/downloads/50m-natural-earth-1/50m-natural-earth-i-with-shaded-relief-and-water/)

[![version][version_badge]][changelog]
[![CodeFactor][codefactor_badge]](https://www.codefactor.io/repository/github/regorxxx/Countries-Shapes-Generator/overview/main)
[![Codacy Badge][codacy_badge]](https://www.codacy.com/gh/regorxxx/Countries-Shapes-Generator/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=regorxxx/countries-shapes-generatorn&amp;utm_campaign=Badge_Grade)
![GitHub](https://img.shields.io/github/license/regorxxx/Countries-Shapes-Generator)

A python script to generate country shapes in multiple [projections](https://scitools.org.uk/cartopy/docs/latest//reference/projections.html) compatible in size with world maps (i.e. meant to be used as layers). Output as png files. Designed to be used as an alternative to server-side JS libraries for world map rendering in some use-cases.

![worldmap_shapes](https://user-images.githubusercontent.com/83307074/173636127-d3d96671-2780-4698-93d7-9a4a7654143a.png)

## Usage
Put all files into folder, for example at 'countries-shapes-generator'. Since every figure will be shown on the GUI, it's recommended to use an IDE which allows to show plots on its own window, like [spyder-ide](https://www.spyder-ide.org/). Otherwise run on python:
```
python countries-shapes-generator.py
```
As output multiple sub-folders will be created at the root, one per projection (should take +20 min):

![image](https://user-images.githubusercontent.com/83307074/173627870-5231298e-74f7-4f32-a6af-77ea07917803.png)

Every country will have an associated file by its [ISO 3166-1 alfa-3 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) (i.e. Canada -> CAN).
Also 2 world maps image files will be available: 'worldmap_shapes' ad 'worldmap_natural'. They should be size-compatible with all the other files.

![image](https://user-images.githubusercontent.com/83307074/173627927-043a70f6-030c-4f15-a590-067fd32bb922.png)

Python docstrings are available for all the functions. Output may be configured for any [projection](https://scitools.org.uk/cartopy/docs/latest//reference/projections.html) when importing the file as module and running the main function manually.
```
import countriesShapesGenerator as csg
import cartopy.crs as ccrs

csg.main(toPath = 'countries-Mercator\\', proj = ccrs.Mercator())
```

![image](https://user-images.githubusercontent.com/83307074/173628273-7b2c224a-81ae-4480-9b34-a39836e08894.png)

## Real World Implementation
Selectable country shapes are used as layers over a world map background here:

 1. [World-Map-SMP](https://github.com/regorxxx/World-Map-SMP): displays current artist's country on the world map and lets you generate autoplaylists based on selection.

![image](https://user-images.githubusercontent.com/83307074/173629306-12e902bc-55c6-4828-99a1-73e114d39b1c.png)

[changelog]: CHANGELOG.md
[version_badge]: https://img.shields.io/github/release/regorxxx/Countries-Shapes-Generator.svg
[codacy_badge]: https://api.codacy.com/project/badge/Grade/1e7a52c1cd0e406f9c46357d21f7bfac
[codefactor_badge]: https://www.codefactor.io/repository/github/regorxxx/Countries-Shapes-Generator/badge/main
