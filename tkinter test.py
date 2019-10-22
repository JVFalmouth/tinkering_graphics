
width, height = 640, 480


from tkinter import Tk, Canvas, PhotoImage, mainloop


def triangle(a,b,c,colour,img):

    vertices=[a,b,c]

    #Sort the vertcies so they are ordered from left to right
    vertices.sort(key=lambda t: t[0])
    for x in range (vertices[0][0],vertices[1][0]):
        y1 = int((x-vertices[0][0])*(vertices[1][1]-vertices[0][1])/(vertices[1][0]-vertices[0][0])+vertices[0][1])
        y2 = int((x-vertices[0][0])*(vertices[2][1]-vertices[0][1])/(vertices[2][0]-vertices[0][0])+vertices[0][1])
        for y in range(y1,y2):
            img.put(colour,(x,y))
        img.put('#000000',(x,y1))
        img.put('#000000',(x,y2))
        img.put('#000000',(x,y1+1))
        img.put('#000000',(x,y2+1))
    # We have drawn all the points in the triangle with x coordinate between vertices[0][0] and vertices[1][0]
    # Now add something to draw in the rest of the points

######## MAIN CODE FROM HERE ############
window = Tk()                                           # Create a window object
canvas = Canvas(window, width=width, height=height, bg='White')  # Create a blank canvas
canvas.pack()                                           # Put it in the window
my_image = PhotoImage(width=width, height=height)                # Create our image
canvas.create_image((width / 2, width / 2), image=my_image, state="normal") # Put the image on the canvas

# Example drwaing of a line
for x in range (100,300):
    my_image.put("#ff0000",(x,150)) # Draw a red dot at all points (x,150), making a line

# Call our function which should draw a triangle
# Note the code to turn 'normal' numbers into a hexadecimal string
triangle((100,100),(150,50),(350,250),'#%02x%02x%02x' % (0,250,250),my_image)
# Try adding your own triangles below and building a simple picture


mainloop() # This is a call to a function in tkinter that shows and passes control to the winodw.