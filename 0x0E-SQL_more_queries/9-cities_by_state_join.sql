-- 9-cities_by_state_join lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id AS id, cities.name AS name, states.name AS name FROM cities, states WHERE cities.state_id=states.id
       ORDER BY cities.id;
