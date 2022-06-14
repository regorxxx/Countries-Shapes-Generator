# -*- coding: utf-8 -*-
"""countries-shapes-generator
Created on Tue Jun 14 17:55:08 2022

@author: Regorxxx

Requires:
  - cartopy
  - matplotlib
  - Natural Earth 'shaded relief and water':
    https://www.naturalearthdata.com/download/downloads/50m-natural-earth-1/

Main output: 
Subfolders with files for selected projection. Images are size-compatible, i.e.
shapes may be overlayed over any world map 'as is'.
  - worldmap_shapes.png
  - worldmap_natural.png
  - XXX.png (shape per country named with ISO A3)

Every single func output uses Mercator projection by default.

Running the file without importing iterates over 6 projections (PlateCarree, 
LambertCylindrical, Mercator, Miller, Mollweide, Robinson) and generates a
set of images for every projection in different subfolders at the current path.
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib.image import imread
import cartopy.io.shapereader as shpreader
import numpy as np
import re
import os

# Globals
my_dpi = 1000

# Retrieve countries
shapename = 'admin_0_countries'
countries_shp = shpreader.natural_earth(resolution='110m',
                                        category='cultural', name=shapename)
# # FOR DEBUG Print keys
# countries = shpreader.Reader(countries_shp).records()
# country = next(countries)
# print(sorted(country.attributes.keys()))

def printShapes(toPath, proj = ccrs.Mercator(),
                color = np.array((199, 233, 192)) / 255):
    """
    Print every country shape with transparent background and placed in its
    absolute position at the world map, i.e. just delete the other countries.

    Parameters
    ----------
    toPath : str
        Folder path for output.
    proj : cartopy.crs projection, optional
        Projection used. The default is ccrs.Mercator().
    color : rgb array, optional
        Shape color. The default is np.array((199, 233, 192)) / 255.

    Returns
    -------
    None. (output files on path)
    """
    for countryHighlight in shpreader.Reader(countries_shp).records():
        plt.cla() # Reset on every loop to only paint current country
        ax = plt.axes(projection=proj)
        name = countryHighlight.attributes['NAME']
        for country in shpreader.Reader(countries_shp).records():
            if name == country.attributes['NAME']:
                ax.add_geometries([country.geometry], ccrs.PlateCarree(),
                                  facecolor=color,
                                  label=country.attributes['NAME_LONG'])
        
        # Use ISO A3 if possible as name
        # Source data has some holes... so this is a workaround
        # files with missing ISO will start with '_'
        iso_id = countryHighlight.attributes['ISO_A3_EH']
        if (iso_id == '-99' or iso_id is None):
            iso_id = countryHighlight.attributes['ISO_A3']
            if (iso_id == '-99' or iso_id is None):
                iso_id = countryHighlight.attributes['NAME']
                print('Missing ISO A3')
                # Sanitize names
                iso_id = '_' + name.strip()
                iso_id = re.sub(r'[^\w\-_\. ]', '', iso_id)
        
        path = toPath + iso_id + '.png'
        print(iso_id + ': ' + path)
        plt.box(False)
        plt.savefig(path, dpi = my_dpi, transparent=True, bbox_inches='tight')
        plt.show(block=False)

# 
def printShapesMap(toPath, proj = ccrs.Mercator(),
                   color = np.array((0, 0, 0)) / 255):
    """
    Print entire world map using country shapes.

    Parameters
    ----------
    toPath : str
        Folder path for output.
    proj : cartopy.crs projection, optional
        Projection used. The default is ccrs.Mercator().
    color : rgb array, optional
        Shape color. The default is np.array((0, 0, 0)) / 255.

    Returns
    -------
    None. (output files on path)

    """
    plt.cla()
    ax = plt.axes(projection=proj)
    for country in shpreader.Reader(countries_shp).records():
        ax.add_geometries([country.geometry], ccrs.PlateCarree(),
                          facecolor=color,
                          label=country.attributes['NAME_LONG'])
    
    path = toPath + 'worldmap_shapes.png'
    plt.box(False)
    plt.savefig(path, dpi = my_dpi, transparent=True, bbox_inches='tight')
    plt.show(block=False)
    print('Shapes earth map: ' + path)

def printNaturalMap(toPath, proj = ccrs.Mercator()):
    """
    Print entire natural map (use hires instead of ax.stock_img() low res).

    Parameters
    ----------
    toPath : str
        Folder path for output.
    proj : cartopy.crs projection, optional
        Projection used. The default is ccrs.Mercator().

    Returns
    -------
    None. (output files on path)

    """
    plt.cla()
    ax = plt.axes(projection=proj)
    path = toPath + 'worldmap_natural.png'
    hires_img = 'images\\NE1_50M_SR_W.png'
    ax.imshow(imread(hires_img), origin='upper', transform=ccrs.PlateCarree(), 
              extent=[-180, 180, -90, 90])
    plt.box(False)
    plt.savefig(path, dpi = my_dpi, transparent=True, bbox_inches='tight')
    plt.show(block=False)
    print('Earth map: ' + path)

def main(toPath = 'countries-Mercator\\',
         proj = ccrs.Mercator()):
    """
    Print shapes, shapes map and natural map.

    Parameters
    ----------
    toPath : str
        Folder path for output.
    proj : cartopy.crs projection, optional
        Projection used. The default is ccrs.Mercator().

    Returns
    -------
    None. (output files on path)
    """
    if not os.path.exists(toPath):
        os.makedirs(toPath)
    
    printShapes(toPath, proj)
    printShapesMap(toPath, proj)
    printNaturalMap(toPath, proj)

if __name__ == '__main__':
    projs = [{'proj': ccrs.PlateCarree(), 'toPath': 'countries-PlateCarree\\'},
             {'proj': ccrs.LambertCylindrical(),
              'toPath': 'countries-LambertCylindrical\\'},
             {'proj': ccrs.Mercator(), 'toPath': 'countries-Mercator\\'},
             {'proj': ccrs.Miller(), 'toPath': 'countries-Miller\\'},
             {'proj': ccrs.Mollweide(), 'toPath': 'countries-Mollweide\\'},
             {'proj': ccrs.Robinson(), 'toPath': 'countries-Robinson\\'}]
    for method in projs:
        main(toPath = method['toPath'], proj = method['proj'])