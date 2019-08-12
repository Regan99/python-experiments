# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

a=0
b=0
dire=''
steps=0
while True:
    r = input("enter the direction step: ")
    if not r:
      break
    
    try:
        dire, steps = r.split(' ')
        steps = int(steps)
    except:
        print("error")

    if dire == "left":
        a = a - steps
    elif dire == "right":
        a = a + steps
    elif dire == "up":
        b = b + steps
    elif dire == "down":
        b = b - steps
    else:
      pass
distance = (a**2 + b**2)**(1/2)
print("the output is: ",int(distance))