# -*- coding: utf-8 -*-

# version 1.1
# 16.1.2011
# Michal Horejsek

import re


MAXINT = 2147483647
COLOR = 'color'
BGCOLOR = 'background'



class ColorError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)



class ColoredText:

    __string = ''
    __formater = {}

    __currentColor = None
    __currentBackground = None

    __colors = {
        'black': (0, 30),
        'red': (0, 31),
        'green': (0, 32),
        'brown': (0, 33),
        'blue': (0, 34),
        'purple': (0, 35),
        'cyan': (0, 36),
        'light gray': (0, 37),

        'dark gray': (1, 30),
        'light red': (1, 31),
        'light green': (1, 32),
        'yellow': (1, 33),
        'light blue': (1, 34),
        'light purple': (1, 35),
        'light cyan': (1, 36),
        'white': (1, 37),

        'dark black': (2, 30),
        'dark red': (2, 31),
        'dark green': (2, 32),
        'gold': (2, 33),
        'dark blue': (2, 34),
        'dark purple': (2, 35),
        'dark cyan': (2, 36),
        'gray': (2, 37),
    }

    __backgroundColors = {
        'black': 40,
        'red': 41,
        'green': 42,
        'brown': 43,
        'blue': 44,
        'purple': 45,
        'cyan': 46,
        'gray': 47,
    }

    def __init__(self, string, color=None, background=None, part=None):
        self.__setString(string)
        self.set(color, background, part)

    def __call__(self, string):
        self.setString(string)

    def __setString(self, string):
        if self.__isNotSet(string): return
        self.__string = str(string)
        self.__clearFormater()
        return self

    def __clearFormater(self):
        self.__formater = {}
        for x in range(0, len(self.__string)):
            self.__formater[x] = {
                COLOR: None,
                BGCOLOR: None,
            }

    def set(self, color=None, background=None, part=None):
        self.setColor(color, part)
        self.setBackground(background, part)

    def setColor(self, color, part=None):
        if self.__isNotSet(color):
        	return
        if self.__isColor(color):
            for s in self.__slices(part):
                self.__addColor(s, color=color)
        else:
        	raise ColorError('Color \'%s\' you can\'t use!' % color)

    def setBackground(self, background, part=None):
        if self.__isNotSet(background):
        	return
        if self.__isBackground(background):
            for s in self.__slices(part):
                self.__addColor(s, background=background)
        else:
        	raise ColorError('Background color \'%s\' you can\'t use' % background)

    def setCurrent(self, color, background):
        self.setCurrentColor(color)
        self.setCurrentBackground(background)

    def setCurrentColor(self, color):
        if self.__isNotSet(color): return
        if self.__isColor(color):
            self.__currentColor = color
        else: raise ColorError('Color \'%s\' you can\'t use' % color)

    def setCurrentBackground(self, background):
        if self.__isNotSet(background):
        	return
        if self.__isBackground(background):
            self.__currentBackground = background
        else:
        	raise ColorError( 'Background color \'%s\' you can\'t use' % background)

    def __isNotSet(self, value):
        return not self.__isSet(value)

    def __isSet(self, value):
    	return True if value else False

    def __slices(self, part):
        if part is None:
            yield self.__defaultSlice()
        elif isinstance(part, slice):
            yield part
        elif isinstance(part, str):
            for f in re.finditer(part, self.__string):
                yield slice(f.start(), f.end())

    def __defaultSlice(self):
        return slice(0, MAXINT)

    def __isColor(self, color):
        return self.__colors.has_key(color)

    def __isBackground(self, color):
        return self.__backgroundColors.has_key(color)

    def __addColor(self, key, color=None, background=None):
        start = max(0, key.__getattribute__('start'))
        stop = min(len(self.__string), key.__getattribute__('stop'))
        for x in range(start, stop):
            self.__addToFormater(x, color, background)

    def __addToFormater(self, x, color=None, background=None):
        if color:
            self.__formater[x][COLOR] = color
        if background:
            self.__formater[x][BGCOLOR] = background

    def __str__(self):
        return self.get()

    def get(self):
        string = ''
        previous = {
            COLOR: None,
            BGCOLOR: None,
        }
        for x, colors in self.__formater.iteritems():
            string += self.__character(x, colors, previous)
            previous = colors
        if self.__isEndSet():
            string += self.__getCurrentColor()
        return string

    def __character(self, x, colors, previous):
        changeColor = self.__isDifferent(colors[COLOR], previous[COLOR])
        changeBackground = self.__isDifferent(colors[BGCOLOR], previous[BGCOLOR])
        if changeColor or changeBackground:
            sequence = self.__createSequence(colors)
        else: sequence = ''
        return sequence + self.__string[x]

    def __isDifferent(self, foo, bar):
    	return foo != bar

    def __createSequence(self, colors):
        color = colors[COLOR] or self.__currentColor
        background = colors[BGCOLOR] or self.__currentBackground
        if color != None and background != None:
            return '\033[%i;%i;%im' % (self.__colors[color][0], self.__colors[color][1], self.__backgroundColors[background])
        elif color != None:
            return '\033[%i;%im' % self.__colors[color]
        elif background != None:
            return '\033[%im' % self.__backgroundColors[background]
        else:
            return '\033[0m'

    def __isEndSet(self):
        maxID = len(self.__formater) - 1
        end = self.__formater[maxID]
        if end[COLOR] == None and end[BGCOLOR] == None:
            return False
        return True

    def __getCurrentColor(self):
        return self.__createSequence({
            COLOR: None,
            BGCOLOR: None,
        })

if __name__ == '__main__':
	print ColoredText('Colored Text!', 'blue', part='^[^ ]*')

