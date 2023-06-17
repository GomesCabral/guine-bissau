import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title('U.S states Game')

image = "guine.gif"
my_screen.addshape(image)

turtle.shape(image)

#HOW TO KNOW THE COORDENATES BY CLICKING THE MAP
def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)



#READ THE CSV
data = pandas.read_csv("city.csv")
cities = data.city.to_list()

guessed_cities = []

while len(cities) > 0:
    user_answer = my_screen.textinput(title=f"{len(guessed_cities)}/{len(cities)}", prompt="Guess the City? ").title()

    if user_answer == 'exit':
        break

    if user_answer in cities:
        guessed_cities.append(user_answer)
        heni = turtle.Turtle()
        heni.hideturtle()
        heni.penup()
        all_data = data[data.city == user_answer]
        heni.goto(int(all_data.x), int(all_data.y))
        heni.color('red')
        heni.write(all_data.city.item())
        cities.remove(all_data.city.item())
