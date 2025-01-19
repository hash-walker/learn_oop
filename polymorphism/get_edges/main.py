"""
Get Edges
Remember that with normal "units" we were checking if their (x/y) point was within a rectangle (the Dragon's breath) to see if they were hit by the fire. With a dragon, because they're so big, we're going to check if the dragon's body (a rectangle) is within the fire (also a rectangle). The image below contains an example of fire breath hitting a dragon.

overlap

Assignment
In the next assignment, we'll be writing the overlap method itself, but first you're going to write a method to find the edges of a rectangle.

The coordinates have now been made private members — we added two underscores to them — so we need to write getter methods to access them.

First, let's set up some helper methods to find these edges.

Write the following methods. What they do should be self-explanatory given their names.

get_left_x()
get_right_x()
get_top_y()
get_bottom_y()
Remember that x1 OR x2 could be the "left x" based on its value on the Cartesian plane. The same goes for the y values. You may find Python's built-in min and max functions useful if you'd rather not use the comparison operators.

Note: The __repr__ method will be explained later in this chapter.


Check If Rectangles Overlap
overlap

Assignment
Let's write the overlaps() method. It should check if this rectangle overlaps a given rectangle, rect. Return True if this rectangle overlaps any part of rect, including just touching sides, or False otherwise.

Here are four conditions that must be True if this rectangle (A) overlaps or touches rect (B):

A's left side is on or to the left of B's right side
A's right side is on or to the right of B's left side
A's top side is on or above B's bottom side
A's bottom side is on or below B's top side


"""

class Rectangle:

    def overlaps(self, rect):
        A_left_x = self.get_left_x()
        A_right_x = self.get_right_x()
        A_top_y = self.get_top_y()
        A_bottom_y = self.get_bottom_y()

        B_left_x = rect.get_left_x()
        B_right_x = rect.get_right_x()
        B_top_y = rect.get_top_y()
        B_bottom_y = rect.get_bottom_y()

        if (
            (A_left_x <= B_right_x) and 
            (B_left_x <= A_right_x) and 
            (A_bottom_y <= B_top_y) and 
            (B_bottom_y <= A_top_y)
        ):
            return True
        
        return False


    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        return min(self.__x1,self.__x2)

    def get_right_x(self):
        return max(self.__x1, self.__x2)

    def get_top_y(self):
        return max(self.__y1, self.__y2)

    def get_bottom_y(self):
        return min(self.__y1,self.__y2)

    # don't touch below this line

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
