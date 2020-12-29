from constants import RECTANGLE_MAX_SIDE_SIZE


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > RECTANGLE_MAX_SIDE_SIZE or self.height > RECTANGLE_MAX_SIDE_SIZE:
            return 'Too big for picture.'

        return (self.width * '*' + '\n') * self.height

    def get_amount_inside(self, shape):
        return (self.width // shape.get_width()) * (self.height // shape.get_height())

    def __str__(self):
        return self._get_shape_info()

    def __repr__(self):
        return self._get_shape_info()

    def _get_shape_info(self):
        return type(self).__name__ + '(width=' + str(self.width) + ', height=' + str(self.height) + ')'
