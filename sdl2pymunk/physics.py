#!/usr/bin/python
import pymunk
from pymunk import Body, Shape  # We will use them as SDL2 Entity components
import sdl2.ext



class MovementSystem(sdl2.ext.Applicator):
    """
      The 'MovementSystem' ties the physical simulation and object's graphical representation.
      It updates SDL2's entities sprite positions from their associated pymunk's simulation body.
    """

    def __init__(self, space, height):
        super(MovementSystem, self).__init__()
        self.height = height
        self.componenttypes = Body, Radius, sdl2.ext.Sprite
        self.space = space

    def process(self, world, componentsets):
        """ Adjust position for entities with body an radius (circles) """
        for body, radius, sprite in componentsets:
            sprite.x, sprite.y = body.position.x-radius.r, self.flipy(body.position.y)-radius.r


    def flipy(self, y):
        return -y + self.height

class Radius:
    def __init__(self, r):
        self.r = r


class Factory:

    def __init__(self, world):
        self.world = world
        subclasses = self._subclass_container()
        self.StaticRectangle = subclasses[0]
        self.Circle = subclasses[1]

    def _subclass_container(self):
        _parent_class = self

        class StaticRectangle(sdl2.ext.Entity):

            def __init__(self, world, sprite, position):
                self.world = _parent_class.world
                x, y = position
                y = self.world.movement_system.flipy(y)
                w, h = sprite.size
                static_body = Body()
                static_lines = [pymunk.Segment(static_body, (x, y), (x + w, y), 0.0),
                                pymunk.Segment(static_body, (x + w, y), (x + w, y - h), 0.0),
                                pymunk.Segment(static_body, (x + w, y - h), (x, y - h), 0.0),
                                pymunk.Segment(static_body, (x, y - h), (x, y), 0.0),
                                ]
                for line in static_lines:
                    line.elasticity = 0.85
                    line.friction = 0.6
                world.space.add(static_lines)
                self.sprite = sprite
                self.sprite.position = x, self.world.movement_system.flipy(y)
                self.sprite.angle = 0

        class Circle(sdl2.ext.Entity):

            def __init__(self, world, sprite, position, radius):
                self.world = _parent_class.world
                x, y = position
                y = self.world.movement_system.flipy(y)
                self.body = Body(1, moment=66)
                self.radius = Radius(radius)
                self.shape = pymunk.Circle(body=self.body, radius=radius)
                self.shape.elasticity = 0.6
                self.shape.friction = 0.6
                self.sprite = sprite
                self.sprite.depth = 10  # Keep circles on top
                self.sprite.position = x-radius, self.world.movement_system.flipy(y)-radius
                self.body.position = x, y
                self.sprite.angle = 0
                self.world.space.add(self.body, self.shape)
        return [StaticRectangle, Circle]