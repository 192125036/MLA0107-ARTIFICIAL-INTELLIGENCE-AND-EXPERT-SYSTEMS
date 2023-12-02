% Facts
mammal(human).
mammal(dog).
mammal(cat).
bird(sparrow).
bird(eagle).

% Rules
% An animal is a mammal if it is not a bird.
mammal(X) :- \+ bird(X).

% An animal is a bird if it is not a mammal.
bird(X) :- \+ mammal(X).




input:
1) mammal(human).
2)bird(cat).
