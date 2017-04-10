/* creating database index to speedup queries */
CREATE INDEX idx_pickup_date ON trips ((pickup_datetime::DATE))

CREATE INDEX idx_dropoff_date ON trips ((dropoff_datetime::DATE))
