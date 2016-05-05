import sdl2.ext
import sdl2.mouse
import pymunk
from sdl2pymunk.physics import MovementSystem, Factory as ObjectFactory
from sdl2pymunk.renderer import TextureRenderer
from sdl2pymunk.sprite import Factory as SpriteFactory
from sdl2pymunk.events import *
import ctypes

class App:

    def __init__(self, title, size):
        self.event_handlers = {}
        sdl2.ext.init()
        self.window = sdl2.ext.Window(title, size)
        self.texture_renderer = sdl2.ext.Renderer(self.window)
        self.world = sdl2.ext.World()
        self.world.space = pymunk.Space()
        self.world.space.sleep_time_threshold = 0.3

        self.sprite_renderer = TextureRenderer(self.texture_renderer)

        self.SpriteFactory = SpriteFactory(self.texture_renderer)
        self.ObjectFactory = ObjectFactory(self.world)
        self.world.movement_system = MovementSystem(self.world.space, size[1])
        self.world.add_system(self.world.movement_system)
        self.world.add_system(self.sprite_renderer)

    def show(self):
        self.window.show()

    def Entity(self, sprite):
        entity = sdl2.ext.Entity(self.world)
        entity.sprite = sprite
        return entity

    def get_events(self):
        return sdl2.ext.get_events()

    def add(self, some_object):
        pass

    def run(self):
        self.show()
        running = True
        while running:
            self.world.space.step(0.0016)
            self.texture_renderer.clear()
            self.world.process()
            events = self.get_events()
            for event in events:
                #if event.type == EVT_MOUSEMOTION:
                event_list = self.event_handlers.get(event.type, [])
                for callback in event_list:
                    callback(event)
                if event.type == EVT_QUIT:
                    running = False
                    break
        sdl2.ext.quit()

    def add_event_handler(self, event_type, callback):
        event_list = self.event_handlers.get(event_type, [])
        if not event_list:
            self.event_handlers[event_type] = event_list
        event_list.append(callback)

    def get_mouse_state(self):
        x, y = ctypes.c_int(0), ctypes.c_int(0)
        buttonstate = sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
        x, y = x.value, y.value
        y = self.world.movement_system.flipy(y)
        return buttonstate, (x, y)
