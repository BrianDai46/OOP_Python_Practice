from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(canvas_height, canvas_width, colors[canvas_color.lower()])

while True:
    # Ask for option which shape to be draw
    shape_type = input("What shape do you like to draw? (rectangle or square) Enter quit to quit: ")
    if shape_type.lower() == "quit":
        break
    x = int(input("Enter x"))
    y = int(input("Enter y"))
    red = int(input("How much red of RGB? "))
    green = int(input("How much green of RGB? "))
    blue = int(input("How much blue of RGB? "))
    color = (red, green, blue)
    if shape_type.lower() == "square":
        side = int(input("Enter length of sides: "))
        s = Square(x=x, y=y, side=side, color=color)
        # Draw square to canvas
        s.draw(canvas)
    elif shape_type.lower() == "rectangle":
        height = int(input("Enter length of height: "))
        width = int(input("Enter length of width: "))
        r = Rectangle(x=x, y=y, height=height, width=width, color=color)
        # Draw rectangle to canvas
        r.draw(canvas)


canvas.make('canvas.png')
