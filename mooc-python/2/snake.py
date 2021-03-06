import turtle 

def drawSnack(rad,angle,len,neckrad):  
    for i in range(len):  
        turtlecolor = ['red','#3B9909', 'orange', 'yellow', '#000000','red','#3B9909', 'orange', 'yellow', '#000000']
        turtle.circle(rad,angle)
        turtle.pencolor(turtlecolor[i]) 
        turtle.circle(-rad,angle)
        turtle.pencolor(turtlecolor[6-i])
    turtle.circle(rad,angle/2)  
    turtle.fd(rad)  
    turtle.circle(neckrad+1,180)  
    turtle.fd(rad*2/3)  
  
def main():  
    turtle.setup(1300,800,0,0)  
    pythonsize=1  
    turtle.pensize(pythonsize)  
    turtle.pencolor("black")  
    turtle.seth(-40)  
    drawSnack(40,80,5,pythonsize/2)  
  
main()  
