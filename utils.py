import folium
from rosreestr2coord import Area


def draw_map(cadastre_number: str) -> None:
    '''Creates a page with a map and borders of the object by cadastrу number'''
    area = Area(cadastre_number, with_proxy=True)
    points = [coords_list[::-1] for coords_list in area.xy[0][0]]
    m = folium.Map(location=(area.center["y"], area.center["x"]),
                             tiles="OpenStreetMap",
                             zoom_start=20)
    folium.Polygon(locations=points, color="yellow").add_to(m)
    m.save(f"templates/map.html")

