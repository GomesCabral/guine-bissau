import turtle

my_screen = turtle.Screen()
my_screen.title('U.S states Game')

image = "guine.gif"
my_screen.addshape(image)

turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)


#KEEP THE SCREEN OPEN
turtle.mainloop()