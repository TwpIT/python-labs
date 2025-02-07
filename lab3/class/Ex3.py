import Ex2 


class Rectangle(Ex2.Shape):
    def __init__(self, length : int, width : int) -> None:
        self.__length = length
        self.__width = width
    def area(self):
        print(self.__length * self.__width)

def main():
    rec = Rectangle(length = int(input()), width = int(input()))
    rec.area()

if __name__ == "__main__":
    main()