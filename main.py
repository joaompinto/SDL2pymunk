from sdl2pymunk.app import App
from sdl2pymunk.colors import *

def main():
    app = App("Hello World", size=(800, 800))
    app.show()
    app.world.space.gravity = (0, -10)

    # List of static rectangles
    walls = [
        {'size': (800, 20), 'color': WHITE, 'fill_color': RED, 'position': (0, 0)},
        {'size': (800, 20), 'color': WHITE, 'fill_color': GREEN, 'position': (0, 780)},
        {'size': (20, 760), 'color': WHITE, 'fill_color': BLUE, 'position': (0, 20)},
        {'size': (20, 760), 'color': WHITE, 'fill_color': YELLOW, 'position': (780, 20)},
        # Middle line
        {'size': (300, 20), 'color': WHITE, 'fill_color': GREEN, 'position': (300, 600)},
    ]

    # Place static walls
    for wall in walls:
        kwargs = {}
        for keyname in ['size', 'color', 'fill_color']:  # Select the sprite specific attributes
            kwargs[keyname] = wall[keyname]
        rectangle_sprite = app.SpriteFactory.Rectangle(**kwargs)
        rectangle_object = app.ObjectFactory.StaticRectangle(app.world, rectangle_sprite, wall['position'])

    # Place dynamic circles
    for place_x in range(100, 700, 50):
        circle_sprite = app.SpriteFactory.Circle(radius=20, color=YELLOW, fill_color=MAGENTA)
        circle_object = app.ObjectFactory.Circle(app.world, circle_sprite, (place_x, 50), 20)
        circle_object.body.velocity = (10, 0)

    # Run the app
    app.run()

if __name__ == "__main__":
    main()
