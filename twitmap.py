import folium
from Zubyk_lab3_ex1 import findall
from flask import Flask

def locational(adress):
    """
    (str) -> (tuple)
    :return: latitude and longitude of a location
    """
    import os
    os.environ["GOOGLE_API_KEY"] = "AIzaSyD6BtwMAgrGbnX3rQy71SzM8ZQ_SeysNvc"
    import geocoder
    geo = geocoder.google(adress)
    latlong = geo.latlng
    if latlong:
        return tuple(latlong)
    else:
        return None

print(locational("Boston, MA"))

maps = folium.Map(location=[49.84441000000004, 24.02543000000003],
           tiles='stamenwatercolor',
           zoom_start=3)

fg = folium.FeatureGroup(name="followers")

users = findall("location")
print(users)


for el in users:
    try:
        fg.add_child(folium.Marker(location=locational(el[-1]),
                             popup=str(el[0]),
                             icon=folium.Icon(icon="cloud")))
        print("finished {0}".format(users.index(el)))
    except:
        continue

maps.add_child(fg)

maps.add_child(folium.LayerControl())


maps.save("Olha_zubyk_twitmap.html")



