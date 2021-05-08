class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

  # Use range loop to draw out rectangle
    def get_picture(self):
        if self.width > 50 or self.height > 50:
          return "Too big for picture."
        else:
          output = ""
          for x in range(self.height):
            output = output + ("*" * self.width) + "\n"
          return output

    # area divided by another shape area
    def get_amount_inside(self, shape):
      parent = self.get_area()
      child = shape.get_area()

      times = int(parent / child)
      return times

    def __str__(self):
      string = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
      return string  


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
      self.width = side
      self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.width = height
        self.height = height

    def __str__(self):
      string = "Square(side=" + str(self.width) + ")"
      return string  


