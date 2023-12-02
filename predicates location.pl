% Facts
location(city1, state1).
location(city2, state2).
location(city3, state3).

stays(person1, city1).
stays(person2, city2).
stays(person3, city3).
stays(person4, city1).

% Rules
% Display list of persons with their corresponding state and city
display_persons :-
    write('Persons and their locations:'), nl,
    stays(Person, City),
    location(City, State),
    write(Person), write(' is in '), write(State), write(', '), write(City), nl,
    fail.
display_persons.

% Given person, find the state in which they are staying
find_state(Person, State) :-
    stays(Person, City),
    location(City, State).

input:
1)display_persons.
2)find_state(person2, State).
