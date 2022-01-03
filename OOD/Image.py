# -*- coding: utf-8 -*-
#
# File name     : Image.py
# Description   : Define a class Image, used to manipulate the image processing.
#

'''
Store the image file 


'''

import os
import pickle

class ImageError(Exception):
    pass

class CoordinateError(ImageError):
    pass

class LoadError(ImageError):
    pass

class SaveError(ImageError):
    pass

class ExportError(ImageError):
    pass

class NoFilenameError(ImageError):
    pass

class Image:
    def __init__(self, width, height, filename = "", background = "#FFFFFF"):
        self.filename = filename
        self.__background = background
        self.__data = {}    # key: the coordinate (x, y)
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}     # value: color string
    
    @property
    def background(self):
        return self.__background
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def colors(self):
        return set(self.__colors)
    
    def __getitem__(self, coordinate):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        return self.__data.get(tuple(coordinate), self.__background)
    
    def __setitem__(self, coordinate, color):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        if color == self.__background:
            self.__data.pop(tuple(coordinate), None)
        else:
            self.__data[tuple(coordinate)] = color
            self.__colors.add(color)
    
    def __delitem__(self, coordinate):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        self.__data.pop(tuple(coordinate), None)
    
    def save(self, filename = None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()
        fh = None
        try:
            data = [self.width, self.height, self.__background, self.__data]
            fh = open(self.filename, "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()
    
    def load(self, filename = None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()
            
        fh = None
        try:
            fh = open(self.filename, "rb")
            data = pickle.load(fh)
            (self.__width, self.__height, self.__background, self.__data) = data
            self.__colors = (set(self.__data.values()) | {self.__background})
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()
    
    def export(self, filename):
        if filename.lower().endswith(".xpm"):
            self.__export_xpm(filename)
        else:
            raise ExportError("unsupported export format: " + os.path.splitext(filename)[1])
            

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import Image

    border_color = "#FF0000"    # red
    square_color = "#0000FF"    # blue
    width, height = 240, 65
    midx, midy = width // 2, height // 2
    # print("midx = {0}".format(midx))
    # print("height // 2 = {0}".format(height // 2))
    # print("height % 2 = {0}".format(height % 2))
    image = Image.Image(width, height, "square_eye.img")
    for col in range(width):
        for row in range(height):
            if col < 5 or col >= width-5 or row < 5 or row >= height-5:
                image[col, row] = border_color
            elif midx - 20 < col < midx + 20 and midy - 20 < row < midy + 20:
                image[col, row] = square_color
    image.save()
    image.export("Square_eye.xpm")