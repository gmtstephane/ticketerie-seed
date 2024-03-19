DELETE FROM team;
DELETE FROM championship;
DELETE FROM sport;
DELETE FROM location;

\COPY location(id, name, address, city, state, country, zipcode, latitude, longitude) FROM './output/1-locations.csv' WITH (FORMAT csv, HEADER true);
\COPY sport(id, name, sport_type ) FROM './output/2-sports.csv' WITH (FORMAT csv, HEADER true);
\COPY championship(id, name, sport_id,icon) FROM './output/3-championships.csv' WITH (FORMAT csv, HEADER true);
\COPY team(id, name, sport_id,championships,location_id,icon) FROM './output/4-teams.csv' WITH (FORMAT csv, HEADER true);
