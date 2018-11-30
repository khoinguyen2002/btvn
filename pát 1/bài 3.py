from turtle import*

shape("turtle")
color("red")

for i in range(6):
    for j in range(5):
        for k in range(3):
            forward(50)
            left(90)
        forward(50)
        backward(50)
        left(90)
    forward(50)
    right(90)
    forward(250)
    left(90)

mainloop()