from sdl2pymunk.app import App
from sdl2pymunk.colors import *
from sdl2pymunk.events import *
import math

class MyApp(App):

    def run(self):
        self.applying_force_shape = None
        self.world.space.gravity = (0, -10)

        # List of static rectangles
        walls = [
            {'size': (800, 20), 'color': WHITE, 'fill_color': RED, 'position': (0, 0)},
            {'size': (800, 20), 'color': WHITE, 'fill_color': GREEN, 'position': (0, 780)},
            {'size': (20, 760), 'color': WHITE, 'fill_color': BLUE, 'position': (0, 20)},
            {'size': (20, 760), 'color': WHITE, 'fill_color': YELLOW, 'position': (780, 20)},
            # Middle lines
            {'size': (300, 20), 'color': WHITE, 'fill_color': GREEN, 'position': (300, 600)},
            {'size': (300, 20), 'color': WHITE, 'fill_color': RED, 'position': (400, 400)},
        ]

        # Place static walls
        for wall in walls:
            kwargs = {}
            for keyname in ['size', 'color', 'fill_color']:  # Select the sprite specific attributes
                kwargs[keyname] = wall[keyname]
            rectangle_sprite = self.SpriteFactory.Rectangle(**kwargs)
            rectangle_object = self.ObjectFactory.StaticRectangle(self.world, rectangle_sprite, wall['position'])


        circle_sprite = self.SpriteFactory.Circle(radius=20, color=YELLOW, fill_color=MAGENTA)
        circle_object = self.ObjectFactory.Circle(self.world, circle_sprite, (500, 500), 20)
        pointer_sprite = self.SpriteFactory.Circle(radius=5, color=YELLOW, fill_color=RED)
        pointer_sprite.depth = 20  # Keep it on top of physical objects

        self.pointer_object = self.Entity(pointer_sprite)

        self.add_event_handler(EVT_MOUSEMOTION, self.OnMouseMotion)
        self.add_event_handler(EVT_MOUSEBUTTONDOWN, self.OnMouseButtonDown)
        self.add_event_handler(EVT_MOUSEBUTTONUP, self.OnMouseButtonUp)
        super(MyApp, self).run()

    def OnMouseMotion(self, event):
        if self.applying_force_shape:
            delta_x = self.applying_force_shape.body.position.x - event.motion.x
            delta_y = self.world.movement_system.flipy(self.applying_force_shape.body.position.y) - event.motion.y
            length = math.sqrt(delta_x ** 2 + delta_y ** 2)
            angle = math.atan2(delta_y, delta_x)
            if length > 40:
                delta_x = 40*math.cos(angle)
                delta_y = 40*math.sin(angle)
            self.pointer_object.sprite.x = self.applying_force_shape.body.position.x - delta_x - 5
            self.pointer_object.sprite.y = self.world.movement_system.flipy(self.applying_force_shape.body.position.y) - delta_y - 5

    def OnMouseButtonDown(self, event):
        state, mouse_position = self.get_mouse_state()
        shape = self.world.space.point_query_first(mouse_position)
        if shape:
            self.applying_force_shape = shape

    def OnMouseButtonUp(self, event):
        if self.applying_force_shape:
            delta_x = self.pointer_object.sprite.x - self.applying_force_shape.body.position.x
            delta_y = self.pointer_object.sprite.y - self.world.movement_system.flipy(self.applying_force_shape.body.position.y)
            self.applying_force_shape.body.apply_impulse((-delta_x*2, delta_y*2))
            self.pointer_object.sprite.x, self.pointer_object.sprite.x = -100, -100
            self.applying_force_shape = None

if __name__ == "__main__":
    MyApp("Hello World", size=(800, 800)).run()
