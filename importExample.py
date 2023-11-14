import countriesShapesGenerator as csg
import cartopy.crs as ccrs
import numpy as np

# Run only mercator projection
csg.main(toPath = 'countries-Mercator\\', proj = ccrs.Mercator())

# Create black shapes with white background
csg.printShapes('countries-Mercator-Mask\\', ccrs.Mercator(),
                np.array((0, 0, 0)) / 255, np.array((255, 255, 255)) / 255)

# Create grey shapes with transparent background
csg.printShapes('countries-Mercator-Mask-Grey\\', ccrs.Mercator(),
                np.array((150, 150, 50)) / 255, None)