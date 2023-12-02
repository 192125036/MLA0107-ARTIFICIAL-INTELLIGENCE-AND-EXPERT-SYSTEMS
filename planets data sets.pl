% Facts about planets
planet(mercury, distance_sun(0.39), mass(0.0553)).
planet(saturn, orbital_period(29.5), day_length(10.7)).

% Rule to find distance between two planets based on their positions from the Sun
distance_between(X, Y, Distance) :-
    planet(X, distance_sun(DistX), _),
    planet(Y, distance_sun(DistY), _),
    Distance is abs(DistX - DistY).

% Query to find the distance between Venus and Jupiter
?- distance_between(venus, jupiter, Distance).
