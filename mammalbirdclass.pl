% Rules defining characteristics of mammals and birds
mammal(X) :-
    has_hair(X),
    gives_birth_to_live_young(X).

bird(X) :-
    has_feathers(X),
    flies(X).

% Facts about specific animals
has_hair(dog).
has_hair(cat).
has_hair(human).
has_hair(bat).

gives_birth_to_live_young(dog).
gives_birth_to_live_young(cat).
gives_birth_to_live_young(human).
gives_birth_to_live_young(bat).

has_feathers(sparrow).
has_feathers(eagle).
has_feathers(penguin).

flies(sparrow).
flies(eagle).

% Query to check if an animal is a mammal
is_mammal(X) :-
    mammal(X),
    write(X), write(' is a mammal.').

% Query to check if an animal is a bird
is_bird(X) :-
    bird(X),
    write(X), write(' is a bird.').
