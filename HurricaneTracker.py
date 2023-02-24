import turtle
import tkinter as tk
from tkinter import simpledialog
import os

def storm_setup():

    import tkinter
    turtle.setup(965, 600)  

    wn = turtle.Screen()
    wn.title("Hurricane Tracker")

    
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)



def storm():
    """Animates the path of hurricane 
    """
    (t, wn, map_bg_img) = storm_setup()
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring(title="Storm", prompt="Enter the name of the storm:")

    
    
    file_name = "data/"+user_input+".csv"
    if not os.path.exists(file_name):
        print("File does not exist")
        exit()
    with open(file_name, 'r') as input_file:      
        datapoints = [line.strip() for line in input_file.readlines()]
        datapoints[0] = datapoints[1] 
        t.penup()
        t.goto(float(datapoints[0].split(",")[3]), float(datapoints[0].split(",")[2])) 
        t.pendown()
        for line in datapoints:
            line = line.split(",")
            longitude = float(line[3])
            latitude = float(line[2])
            windval = int(line[4])                        
            t.goto(longitude, latitude)

            if windval >= 157: 
                t.color("red")
                t.write('Cat 5')
            elif windval >= 130: 
                t.color("orange")
                t.write('Cat 4')
            elif windval >= 110: 
                t.color("yellow")
                t.write('Cat 3')
            elif windval >= 96: 
                t.color("green")
                t.write('Cat 2')
            elif windval >= 74:
                t.color("blue")
                t.write('Cat 1')
            else:
                t.color("white")
                t.write('Insignificant')
            t.width(windval/10)

        turtle.done()



    return (t, wn, map_bg_img)

if __name__ == "__main__":
    (t, wn, map_bg_img) = storm()
    wn.exitonclick()
