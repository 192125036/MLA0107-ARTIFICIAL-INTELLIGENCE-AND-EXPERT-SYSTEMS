% Predicate to convert Celsius to Fahrenheit
celsius_to_fahrenheit(Celsius, Fahrenheit) :-
    Fahrenheit is (Celsius * 9/5) + 32.

% Predicate to check if a temperature is below freezing
below_freezing(Temperature) :-
    Temperature < 0.



input:
1)celsius_to_fahrenheit(20, Fahrenheit).
2)below_freezing(-5).
