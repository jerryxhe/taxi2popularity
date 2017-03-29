/* only pickups from Theatre district or dropoffs in Theatre district */
DELETE FROM trips WHERE (pickup_nyct2010_gid NOT IN (21, 901, 902, 1162, 1163, 1283, 1699)) AND (dropoff_nyct2010_gid NOT IN (21, 901, 902, 1162, 1163, 1283, 1699)) AND (pickup_location_id NOT IN (48, 50, 164, 230)) AND (dropoff_location_id NOT IN (48, 50, 164, 230)); 

CREATE TABLE ambassador_theatre_pickups_by_lat_long_hour AS
SELECT                                                                                                 
  EXTRACT(year from pickup_datetime) AS pickup_year,
  EXTRACT(month from pickup_datetime) AS pickup_month,
  EXTRACT(hour from pickup_datetime) AS pickup_hour,
  ROUND(pickup_longitude, 4) AS pickup_long,
  ROUND(pickup_latitude, 4) AS pickup_lat,
  COUNT(*) AS vehicle_count,
  AVG(passenger_count) AS avg_passenger_per_taxi
FROM trips WHERE
  ST_DWithin(pickup, ST_SetSRID(ST_Point(-73.9849902287, 40.76123555), 4326), 400)
 GROUP BY
  pickup_year,pickup_month,pickup_hour,pickup_long,pickup_lat;

CREATE TABLE theatre_trips_2010 AS
SELECT trips.* FROM trips,custom_locations AS loc 
WHERE
(pickup_datetime >= '2010-01-01') AND 
(pickup_datetime < '2011-01-01') AND 
(ST_DWithin(pickup, ST_SetSRID(ST_MakePoint(loc.lon, loc.lat), 4326), 400) OR ST_DWithin(dropoff, ST_SetSRID(ST_MakePoint(loc.lon, loc.lat), 4326), 400)) 
GROUP BY trips.id;

CREATE TABLE theatre_pickups_by_lat_long_2010 AS
SELECT
  EXTRACT(month FROM pickup_datetime) AS pickup_month,
  EXTRACT(hour FROM pickup_datetime) AS pickup_hour,
  ROUND(pickup_longitude, 4) AS pickup_lon,
  ROUND(pickup_lattitude, 4) AS pickup_lat,
  COUNT(*) AS vehicle_count,
  AVG(passenger_count) AS avg_passenger_per_taxi,
  AVG(total_amount) AS avg_fare,
  AVG(dropoff_datetime - pickup_datetime) AS avg_ride_duration
FROM theatre_trips_2011
GROUP BY
  pickup_month,pickup_hour,pickup_lon,pickup_lat
  
CREATE TABLE ambassador_theatre_dest_summary_by_location_id AS
SELECT dropoff_location_id,
 EXTRACT(year from pickup_datetime) AS pickup_year,
 
 EXTRACT(hour from pickup_datetime) AS pickup_hour,
 COUNT(*) AS vehicle_count,
 AVG(passenger_count) AS avg_passenger_per_taxi,
 AVG(total_amount) AS avg_fare,
 AVG(dropoff_datetime - pickup_datetime) AS avg_ride_duration
FROM trips WHERE (dropoff_location_id IS NOT NULL)
GROUP BY pickup_year,pickup_month,pickup_hour,dropoff_location_id;
  
 
CREATE TABLE theatre_weather_dest_2009 AS
SELECT 
    date_trunc('week', pickup_datetime) AS week_start,
    EXTRACT(hour FROM pickup_datetime) AS pickup_hour,
    dropoff_location_id, 
    CASE WHEN (w.precipitation+w.snow_depth+w.snowfall) > 5 
        THEN 'bad_weather' 
        ELSE 'good_weather' 
    END AS weather_condition, 
    ROUND(pickup_longitude, 4) AS pickup_lon, 
    ROUND(pickup_latitude, 4) AS pickup_lat, 
    COUNT(*) AS vehicle_count,
    AVG(passenger_count) AS avg_passenger_per_taxi,
    AVG(total_amount) AS avg_fare,
    AVG(dropoff_datetime - pickup_datetime) AS avg_ride_duration
FROM theatre_trips_2009,central_park_weather_observations w
WHERE w.date = date(pickup_datetime)
GROUP BY 1,2,3,4,5,6
ORDER BY 1,3,6;

DELETE FROM theatre_weather_dest_2009 WHERE week_start < '2009-01-01'


