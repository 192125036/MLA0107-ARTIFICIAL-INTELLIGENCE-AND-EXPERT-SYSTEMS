% Facts
male(john).
male(bob).
female(anna).
female(lisa).

has_child(john, lisa).
has_child(john, bob).
has_child(anna, lisa).
has_child(anna, bob).

% Rules
parent(X, Y) :- has_child(X, Y), male(X).
parent(X, Y) :- has_child(X, Y), female(X).


input:
1)parent(john, Child).
2)parent(anna, Child).
3)parent(bob, Child).
