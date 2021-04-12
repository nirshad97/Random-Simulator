import turtle
import random
from start_sim import InitialPos


def get_midpoint(turtle1, turtle2):
    x1 = turtle1.get_position()[0]
    x2 = turtle2.get_position()[0]
    y1 = turtle1.get_position()[1]
    y2 = turtle2.get_position()[1]
    return (x1+x2)/2, (y1+y2)/2


def goto_position(turt):
    while True:
        rand_choice = random.choice(choices)
        if rand_choice == 1 or rand_choice == 2:
            new_pos = get_midpoint(turt, t1)
            recurring_turtle = InitialPos(new_pos, 0.25)
            return goto_position(recurring_turtle)
        elif rand_choice == 3 or rand_choice == 4:
            new_pos = get_midpoint(turt, t2)
            recurring_turtle = InitialPos(new_pos, 0.25)
            return goto_position(recurring_turtle)
        elif rand_choice == 5 or rand_choice == 6:
            new_pos = get_midpoint(turt, t3)
            recurring_turtle = InitialPos(new_pos, 0.25)
            return goto_position(recurring_turtle)


choices = [1, 2, 3, 4, 5, 6]  # This resembles the dice rollings

t1 = InitialPos((250, -150), 0.25)  # 1 , 2
t2 = InitialPos((-250, -150), 0.25)  # 3, 4
t3 = InitialPos((0, 200), 0.25)  # 5, 6

# Initialization process, we start at a random point.
starting_x, starting_y = random.randint(-250, 250), random.randint(-150, 200)
t4 = InitialPos((starting_x, starting_y), 0.25)
print(t4.get_position())

goto_position(t4)

turtle.mainloop()

