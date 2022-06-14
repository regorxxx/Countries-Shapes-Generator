import countriesShapesGenerator as csg
import cartopy.crs as ccrs

# Run only mercator projection
csg.main(toPath = 'countries-Mercator\\', proj = ccrs.Mercator())