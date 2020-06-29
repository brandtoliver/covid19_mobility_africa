import fiona.io
from os import path
import geopandas as gpd
import requests
import json
import numpy as np
import pycountry

import os
import pandas as pd
import glob


import shapely
import geopandas as gpd
from shapely.geometry import shape, LineString, Polygon

import geojson


def poly_convert(polygon):
    all_coords = []
    if polygon.boundary.geometryType() == "MultiLineString":
        for b in polygon.boundary:
            coords = np.dstack(b.coords.xy).tolist()
            all_coords.append(*coords)
    else:
        coords = np.dstack(polygon.boundary.coords.xy).tolist()
        all_coords.append(*coords)
    return all_coords


# def inconsistency_map(name):
#     incmap = {
#         'Århus': 'Aarhus',
#         'Høje Taastrup': 'Høje-Taastrup'
#     }
#     if name in incmap:
#         return incmap[name]
#     return name

# Example that creates shape_file and saves it in current directory:  create_shape_file('Denmark',adm = 2,save_dir='')
def create_shape_file(
    country,
    adm,
    save_dir=False,
    file_return=True,
    return_geo_pd=False,
    exists_skip=True,
):
    if save_dir != False:
        full_path = save_dir + country.title() + "_geojson.json"
    else:
        full_path = ""
    if (path.exists(full_path)) and (exists_skip):
        return None
    else:
        if country == "Britain":
            iso3 = pycountry.countries.get(name="United Kingdom").alpha_3
        else:
            iso3 = pycountry.countries.get(name=country).alpha_3

        # iso3 = pycountry.countries.get(name=country).alpha_3
        response = requests.get(
            f"https://biogeo.ucdavis.edu/data/gadm3.6/shp/gadm36_{iso3}_shp.zip"
        )
        data_bytes = response.content

        with fiona.io.ZipMemoryFile(data_bytes) as zip_memory_file:
            with zip_memory_file.open(f"gadm36_{iso3}_{adm}.shp") as collection:
                geodf = gpd.GeoDataFrame.from_features(collection, crs="epsg:4326")
                columns_replace = geodf.columns[geodf.columns.str.startswith("NAME_")]
                for column in columns_replace:
                    geodf[column] = geodf[column].str.replace("\W+", " ").str.strip()
                geodf = geodf.dropna(subset=columns_replace)

                if return_geo_pd:
                    return geodf
                geodf.geometry = geodf.geometry.simplify(0.001)

    shape_file = [
        {"kommune": loc["NAME_2"], "polygons": poly_convert(loc["geometry"])}
        for i, loc in geodf.iterrows()
    ]
    if save_dir != False:
        full_path = save_dir + country.title() + "_geojson.json"
        with open(full_path, "w") as f:
            json.dump(shape_file, f)
    if file_return:
        return shape_file


def create_shape_file_tile(
    country, city, save_dir, file_return=True,
):
    full_path = save_dir + country.title() + "_geojson.json"

    PATH_IN_TILE = f"Facebook/{country}/movement_tile/"
    PATH_IN_TILE = os.path.join(PATH_IN_TILE, "*.csv")

    all_files = glob.glob(PATH_IN_TILE)

    tile_data = pd.concat((pd.read_csv(f) for f in all_files))
    tile_data["start_quadkey"] = tile_data.start_quadkey.astype("int")
    tile_data["end_quadkey"] = tile_data.end_quadkey.astype("int")

    # TODO: not all tiles are guaranteed, ´end_polygon_name´ should be included.
    # 1. iteration
    ## nairobi_df = tile_data[
    ##    (tile_data.start_polygon_name == city) & (tile_data.end_polygon_name == city)
    ## ]

    # 2. iteration
    max_lat = 7.989807128906249
    min_lat = 6.998291015625

    max_lon = 9.538457618319674
    min_lon = 8.651626379005748

    nairobi_df = tile_data[
        (
            (tile_data.end_lat <= max_lat)
            & (tile_data.end_lat >= min_lat)
            & (tile_data.end_lon <= max_lon)
            & (tile_data.end_lon >= min_lon)
        )
    ]

    # TODO: avoid using ´.first()´. Check if one quadkey by mistake has multiple different ´end_lat´and ´end_lon´.
    unique_tiles = (
        nairobi_df.groupby(["end_quadkey"])[["end_lat", "end_lon"]]
        .first()
        .reset_index()
    )
    print(len(unique_tiles))
    shape_file = []

    for _, row in unique_tiles.iterrows():

        lat = row.end_lat
        lng = row.end_lon

        size = 0.045  # kenya 0.022 Nigeria 0.045

        # create geodataframe with some variables
        gf = gpd.GeoDataFrame(
            {"lat": lat, "lon": lng, "width": size, "height": size},
            index=[1],
            crs="epsg:4326",
        )

        # create center as a shapely geometry point type and set geometry of dataframe to this
        gf["center"] = gf.apply(
            lambda x: shapely.geometry.Point(x["lon"], x["lat"]), axis=1
        )
        gf = gf.set_geometry("center")

        # create polygon using width and height
        gf["center"] = shapely.geometry.box(*gf["center"].buffer(1).total_bounds)
        gf["polygon"] = gf.apply(
            lambda x: shapely.affinity.scale(x["center"], x["width"], x["height"]),
            axis=1,
        )
        gf = gf.set_geometry("polygon")
        geopoly = gf["polygon"].to_json()

        g1 = geojson.loads(geopoly)
        gh = g1[0].geometry
        g2 = shape(gh)

        # Create GeoJSON
        wow3 = geojson.dumps(g2)
        wow4 = json.loads(wow3)

        gd_feat = dict(
            kommune="A" + str(int(row.end_quadkey)), polygons=wow4["coordinates"]
        )

        shape_file.append(gd_feat)

    if save_dir != False:
        full_path = save_dir + city.title() + "tile_geojson.json"
        with open(full_path, "w") as f:
            json.dump(shape_file, f)
    if file_return:
        return shape_file


if __name__ == "__main__":
    create_shape_file_tile(
        country="Nigeria",
        # country="Kenya",
        city="Federal Capital Territory",
        # city='Lagos'
        # city="Nairobi",
        save_dir="/Users/oliver/Data_Science/09_covid19_africa/covid19_mobility_africa/covid19.compute.dtu.dk/static/data/",
    )

    # create_shape_file(
    #    "Kenya",
    #    adm=2,
    #    save_dir="/Users/oliver/Data_Science/09_covid19_africa/covid19_mobility_africa/covid19.compute.dtu.dk/static/data/",
    # )

