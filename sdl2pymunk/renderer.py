import sdl2.ext
from sdl2 import rect, render
from sdl2.ext.compat import isiterable


class TextureRenderer(sdl2.ext.TextureSpriteRenderSystem):

    def __init__(self, renderer):
        super(TextureRenderer, self).__init__(renderer)
        self.renderer = renderer

    def render(self, sprites, x=None, y=None):
        """Overrides the render method of sdl2.ext.TextureSpriteRenderSystem to
        use "SDL_RenderCopyEx" instead of "SDL_RenderCopy" to allow sprite
        rotation:

        http://wiki.libsdl.org/SDL_RenderCopyEx
        """
        r = rect.SDL_Rect(0, 0, 0, 0)
        if isiterable(sprites):
            rcopy = render.SDL_RenderCopyEx
            renderer = self.sdlrenderer
            x = x or 0
            y = y or 0
            for sp in sprites:
                r.x = x + int(sp.x)
                r.y = y + int(sp.y)
                r.w, r.h = sp.size
                if rcopy(renderer, sp.texture, None, r, sp.angle, None, render.SDL_FLIP_NONE) == -1:
                    raise sdl2.ext.error()
        else:
            r.x = sprites.x
            r.y = sprites.y
            r.w, r.h = sprites.size
            if x is not None and y is not None:
                r.x = x
                r.y = y
            render.SDL_RenderCopyEx(self.sdlrenderer,
                                    sprites.texture,
                                    None,
                                    r,
                                    sprites.angle,
                                    None,
                                    render.SDL_FLIP_NONE)
        render.SDL_RenderPresent(self.sdlrenderer)
