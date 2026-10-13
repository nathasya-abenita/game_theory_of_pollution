import geopandas as gpd
import matplotlib.pyplot as plt
from main.config import COUNTRY_NAMES
if __name__ == '__main__':
    
    # Read raw data of countries polygons
    gdf = gpd.read_file('./data/vector/ne_10m_admin_0_countries.zip')
    
    # Decide filter indexes
    idxs = gdf['NAME'].isin(COUNTRY_NAMES)

    # Print filtered data
    print(gdf[idxs])
    gdf_filtered = gdf[idxs].copy()

    # Save as a new shapefile
    # gdf_filtered.to_file('./data/vector/countries.shp')

    # Plot map
    fig, ax = plt.subplots()
    gdf_filtered.plot(ax=ax)                        # Plot polygons
    gdf_filtered.boundary.plot(ax=ax, color='k')    # Plot countries' boundary
    plt.show()