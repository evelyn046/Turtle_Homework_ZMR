import turtle

def graphic(length):
    turtle.forward(60)
    turtle.left(180)
    turtle.circle(-length,180,20)
    turtle.left(120)
    turtle.forward(length)
    turtle.right(60)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(60)
    turtle.forward(length)
    turtle.left(120)
    turtle.circle(-length,180,20)
    turtle.right(180)
    turtle.forward(60)


def draw(length):
    
    for count,color in zip(range(5),['aliceblue','powderblue','lightblue','skyblue','lightskyblue']):
        turtle.begin_fill()
        turtle.fillcolor(color)
        graphic(length)
        turtle.right(72)
        turtle.end_fill()
   
    length = length/2
   
    if length > 10:
 
        draw(length)


draw(80)
