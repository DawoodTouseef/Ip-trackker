"""
pip install webbrowser
pip install geocoder
pip install folium
"""
import webbrowser
import geocoder
import folium
#insert ip(Internet Protocol) address to search
A=int("Enter the IP adress:")
g=geocoder.ip(A)
#to find the latitude and longitude of ip address
myaddress=g.latlng
my_map1=folium.Map(location=myaddress,
                    zomm_stat=12,)
folium.CircleMarker(location=myaddress,
                    radius=55,popup='yorkshire').add_to(my_map1)
folium.Marker(myaddress,
            popup='Yorkshire').add_to(my_map1)
#to save the map in HTML format
my_map1.save("my_map2.html")
#to open the map in webbrowser
webbrowser.open("my_map2.html")
