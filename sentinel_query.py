import json
from datetime import datetime
from sentinelhub import SHConfig, SentinelHubCatalog, DataCollection, BBox, CRS

def query_sentinel_scenes(start_date, end_date, aoi_wkt, max_cloud_cover=30):
    config = SHConfig()
    config.sh_client_id = "cdse"  # Copernicus Data Space Ecosystem
    config.sh_client_secret = ""

    bbox = BBox(bbox=aoi_wkt, crs=CRS.WGS84)
    catalog = SentinelHubCatalog(config=config)

    search_iterator = catalog.search(
        DataCollection.SENTINEL2_L2A,
        bbox=bbox,
        time=(start_date, end_date),
        query={"eo:cloud_cover": {"lt": max_cloud_cover}},
        fields={"include": ["id", "properties.datetime", "properties.eo:cloud_cover"]}
    )

    results = []
    for scene in search_iterator:
        results.append({
            "id": scene["id"],
            "datetime": scene["properties"]["datetime"],
            "cloud_cover": scene["properties"]["eo:cloud_cover"]
        })

    return results

if __name__ == "__main__":
    scenes = query_sentinel_scenes("2024-01-01", "2024-01-31", "POLYGON((101.4 2.9, 101.9 2.9, 101.9 3.4, 101.4 3.4, 101.4 2.9))")
    print(json.dumps(scenes, indent=2))