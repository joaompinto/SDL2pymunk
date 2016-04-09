import sdl2.ext
import pymunk
from sdl2pymunk.physics import MovementSystem, Factory as ObjectFactory
from sdl2pymunk.renderer import TextureRenderer
from sdl2pymunk.sprite import Factory as SpriteFactory
from sdl2pymunk.events import *

class App:

    def __init__(self, title, size):
        sdl2.ext.init()
        self.window = sdl2.ext.Window(title, size)
        self.texture_renderer = sdl2.ext.Renderer(self.window)
        self.world = sdl2.ext.World()
        self.world.space = pymunk.Space()
        self.world.space.sleep_time_threshold = 0.3

        self.sprite_renderer = TextureRenderer(self.texture_renderer)

        self.SpriteFactory = SpriteFactory(self.texture_renderer)
        self.ObjectFactory = ObjectFactory(self.world)
        self.world.add_system(MovementSystem(size[1], self.world.space))
        self.world.add_system(self.sprite_renderer)

    def show(self):
        self.window.show()

    def get_events(self):
        return sdl2.ext.get_events()

    def add(self, some_object):
        pass

    def run(self):
        running = True
        while running:
            self.world.space.step(0.0016)
            self.texture_renderer.clear()
            self.world.process()
            events = self.get_events()
            for event in events:
                if event.type == EVT_QUIT:
                    running = False
                    break
        sdl2.ext.quit()
