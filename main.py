from sdl2pymunk.app import App
from sdl2pymunk.colors import *

def main():
    app = App("Hello World", size=(800, 800))
    app.show()
    app.world.space.gravity = (0, -10)

    # List of static walls
    walls = [
        {'size': (800, 20), 'color': RED, 'position': (0, 0)},
        {'size': (800, 20), 'color': BLUE, 'position': (0, 780)},
        {'size': (20, 760), 'color': GREEN, 'position': (0, 20)},
        {'size': (20, 760), 'color': WHITE, 'position': (780, 20)},
    ]

    # Place static walls
    for wall in walls:
        rectangle_sprite = app.SpriteFactory.Rectangle(wall['size'], wall['color'])
        rectangle_object = app.ObjectFactory.StaticRectangle(app.world, rectangle_sprite, wall['position'])

    # Place dynamic circles
    for place_x in range(100, 500, 50):
        circle_sprite = app.SpriteFactory.Circle(radius=20, color=YELLOW)
        circle_object = app.ObjectFactory.Circle(app.world, circle_sprite, (place_x, place_x), 20)
        circle_object.body.velocity = (10, 0)

    # Run the app
    app.run()

if __name__ == "__main__":
    main()
