% Facts
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(strawberry, red).
fruit_color(blueberry, blue).
fruit_color(watermelon, green).
fruit_color(pineapple, yellow).

% Rules
is_red_fruit(Fruit) :- fruit_color(Fruit, red).
is_yellow_fruit(Fruit) :- fruit_color(Fruit, yellow).
is_purple_fruit(Fruit) :- fruit_color(Fruit, purple).
is_orange_fruit(Fruit) :- fruit_color(Fruit, orange).
is_blue_fruit(Fruit) :- fruit_color(Fruit, blue).
is_green_fruit(Fruit) :- fruit_color(Fruit, green).




input:
1)is_red_fruit(Fruit).
2)fruit_color(banana, Color).
