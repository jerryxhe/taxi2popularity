theatre_addresses = {
    'Ambassador':'219 W 49th St, New York, NY 10019',
    'Gershwin':"222 W 51st St, New York, NY 10019",
    'Richard Rodgers':'226 W 46th St, New York, NY 10036',
    'Majestic':'245 W 44th St, New York, NY 10036',
    'Al Hirschfeld':'302 W 45th St, New York, NY 10036',
    'Lyric':'213 W 42nd St, New York, NY 10036',
    'Lunt-Fontanne':'205 W 46th St, New York, NY 10036',
    'Brooks Atkinson':'256 W 47th St, New York, NY 10036',
    'Friedman':'261 W 47th Street, New York, NY 10036',
    'Walter Kerr':'219 W 48th St, New York, NY 10036',
    'Winter Garden':'1634 Broadway, New York, NY 10019',
    'Minskoff':'200 W 45th St, New York, NY 10036',
    'Imperial':'249 W 45th St, New York, NY 10036',
    'St James':'246 W 44th St, New York, NY 10036',
    'Lyceum':'149 W 45th St, New York, NY 10036',
    'Stephen Sondheim':'124 W 43rd St, New York, NY 10036',
    'Nederlander':'208 W 41st St, New York, NY 10036',
    'August Wilson':'245 W 52nd St, New York, NY 10019',
    'New World Stages':'340 W 50th St, New York, NY 10019',
    'Broadway':'1681 Broadway, New York, NY 10019',
    'Belasco':'111 W 44th St, New York, NY 10036',
    'Longacre':'220 W 48th St, New York, NY 10036',
    'Jacobs':'242 W 45th St, New York, NY 10036',
    'Schoenfeld':'236 W 45th St, New York, NY 10036',
    'Golden':'252 W 45th St, New York, NY 10036',
    'Booth':'222 W 45th St, New York, NY 10036',
    'Broadhurst':'235 W 44th St, New York, NY 10036',
    'Neil Simon':'250 W 52nd St, New York, NY 10019',
    'Marquis':'210 W 46th St, New York, NY 10036',
    'Palace':'1564 7th Ave & W 47th Street, New York, NY 10036',
    'New Amsterdam':'214 W 42nd St, New York, NY 10036', 
    'Studio 54':'254 W 54th St, New York, NY 10019',
    'Helen Hays':'240 W 44th St, New York, NY 10036',
    'Barrymore':'243 W 47th St, New York, NY 10036',
    'Eugene O'Neill':'230 W 49th St, New York, NY 10019',
    'Cort':'138 W 48th St, New York, NY 10036',
    'Music Box':'239 W 45th St, New York, NY 10036',
    'American Airlines':'227 W 42nd St, New York, NY 10036',
    'Vivian Beaumont':'50 Lincoln Center Plaza #1, New York, NY 10023' 
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
