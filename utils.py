'''The Module with the logic of plot boundaries on the map'''
import folium
from rosreestr2coord import Area


def draw_map(cadastre_number: str) -> str:
    '''Creates a page with a map and borders of the object by cadastrу number'''
    area = Area(cadastre_number, with_proxy=True)
    points = [coords_list[::-1] for coords_list in area.xy[0][0]]
    map_ = folium.Map(location=(area.center["y"], area.center["x"]),
                             tiles="OpenStreetMap",
                             zoom_start=20)
    folium.Polygon(locations=points, color="yellow").add_to(map_)
    return map_._repr_html_()
