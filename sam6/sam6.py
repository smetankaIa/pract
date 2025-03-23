class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        if self.width <= 0 or self.height <= 0:
            return None  # Или можно поднять исключение ValueError("Width and height must be positive")
        return self.width * self.height