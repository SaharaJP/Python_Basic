from Answers import *

class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam
        elif isinstance(other, Earth):
            return Dirt
        else:
            return NoClass

class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam
        elif isinstance(other, Air):
            return Sparkle
        elif isinstance(other, Earth):
            return Lava
        else:
            return NoClass

class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm
        elif isinstance(other, Fire):
            return Sparkle
        elif isinstance(other, Earth):
            return Dust
        else:
            return NoClass

class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt
        elif isinstance(other, Fire):
            return Lava
        elif isinstance(other, Air):
            return Dust
        else:
            return NoClass