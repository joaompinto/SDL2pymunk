import sdl2.ext

def draw_circle(target, x0, y0, radius, color):
    """
    https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
    """
    x = radius
    y = 0
    decisionOver2 = 1 - x  # Decision criterion divided by 2 evaluated at x = r, y = 0
    while y <= x:
        target.draw_point((x + x0, y + y0), color)    # Octant 1
        target.draw_point((y + x0, x + y0), color)    # Octant 2
        target.draw_point((-x + x0, y + y0), color)   # Octant 4
        target.draw_point((-y + x0, x + y0), color)   # Octant 3
        target.draw_point((-x + x0, -y + y0), color)  # Octant 5
        target.draw_point((-y + x0, -x + y0), color)  # Octant 6
        target.draw_point((x + x0, -y + y0), color)   # Octant 7
        target.draw_point((y + x0, -x + y0), color)   # Octant 8
        y += 1
        if decisionOver2 <= 0:
            decisionOver2 += 2 * y + 1
        else:
            x -= 1
            decisionOver2 += 2 * (y - x) + 1


class Factory(object):

    def __init__(self, renderer):
        self.factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)

    def Circle(self, radius, color):
        circ_sprite = self.factory.create_software_sprite(size=(radius * 2 + 1, radius * 2 + 1),
                                                     masks=(0xFF000000,  # red channel
                                                            0x00FF0000,  # green channel
                                                            0x0000FF00,  # blue channel
                                                            0x000000FF))  # alpha channel
        circle_renderer = sdl2.ext.Renderer(circ_sprite)
        draw_circle(circle_renderer, radius, radius, radius, color)
        return self.factory.from_surface(circ_sprite.surface)


    def Rectangle(self, size, color):
        circ_sprite = self.factory.create_software_sprite(size=size,
                                                          masks=(0xFF000000,  # red channel
                                                                 0x00FF0000,  # green channel
                                                                 0x0000FF00,  # blue channel
                                                                 0x000000FF))  # alpha channel
        renderer = sdl2.ext.Renderer(circ_sprite)
        renderer.draw_rect((0, 0, size[0], size[1]), color=color)
        return self.factory.from_surface(circ_sprite.surface)
