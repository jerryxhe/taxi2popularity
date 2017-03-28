theatre_addresses = {
    'Ambassador Theatre':'219 W 49th St, New York, NY 10019',
    'Gershwin Theatre':"222 W 51st St, New York, NY 10019",
    'Richard Rodgers Theatre':'226 W 46th St, New York, NY 10036',
    'Majestic Theatre':'245 W 44th St, New York, NY 10036',
    'Al Hirschfeld Theatre':'302 W 45th St, New York, NY 10036',
    'Lyric Theatre':'213 W 42nd St, New York, NY 10036',
    'Lunt-Fontanne Theatre':'205 W 46th St, New York, NY 10036',
    'Brooks Atkinson Theatre':'256 W 47th St, New York, NY 10036',
    'Samuel J Friedman Theatre':'261 W 47th Street, New York, NY 10036',
    'Walter Kerr Theatre':'219 W 48th St, New York, NY 10036',
    'Winter Garden Theatre':'1634 Broadway, New York, NY 10019',
    'Minskoff Theatre':'200 W 45th St, New York, NY 10036',
    'Imperial Theatre':'249 W 45th St, New York, NY 10036',
    'St James Theatre':'246 W 44th St, New York, NY 10036',
    'Lyceum Theatre':'149 W 45th St, New York, NY 10036',
    'Stephen Sondheim Theatre':'124 W 43rd St, New York, NY 10036',
    'Nederlander Theatre':'208 W 41st St, New York, NY 10036',
    'August Wilson Theatre':'245 W 52nd St, New York, NY 10019',
    'New World Stages':'340 W 50th St, New York, NY 10019',
    'Broadway Theatre':'1681 Broadway, New York, NY 10019',
    'Belasco Theatre':'111 W 44th St, New York, NY 10036',
    'Longacre Theatre':'220 W 48th St, New York, NY 10036'
}

theatres = []
from geopy.geocoders import Nominatim
geolocator = Nominatim()
for name,addr in theatre_addresses.items():
    location = geolocator.geocode(addr)
    print(name, "-> ", location.latitude, location.longitude)
    theatres.append({'name':name, 'address':addr, 'lat':location.latitude, 'lon':location.longitude})

db.query("""CREATE TABLE custom_locations (
  name varchar(31) UNIQUE,
  addr varchar(127),
  type_id int,
  lon double precision,
  lat double precision
);""")

for theatre in theatres:
    db.insert('custom_locations',type_id=0,name=theatre['name'],addr=theatre['address'], lat=theatre['lat'],lon=theatre['lon'])
