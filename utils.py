import folium
from rosreestr2coord import Area

def draw_map(cadastre_number: str) -> None:
    area = Area(cadastre_number)
    points = [coords_list[::-1] for coords_list in area.xy[0][0]]
    m = folium.Map(location=(area.center["y"], area.center["x"]),
                             tiles="OpenStreetMap",
                             zoom_start=20)
    folium.Polygon(locations=points, color="yellow").add_to(m)
    m.save(f"templates/map.html")

