class Point:
    def __init__(self, X=0, Y=0):
        # Constructor to initialize the Point object with x and y coordinates
        self.__X = X
        self.__Y = Y

    def get_X(self):
        # Getter method to retrieve the x-coordinate of the Point
        return self.__X

    def get_Y(self):
        # Getter method to retrieve the y-coordinate of the Point
        return self.__Y

    def set_X(self, X):
        # Setter method to set the x-coordinate of the Point
        self.__X = X

    def set_Y(self, Y):
        # Setter method to set the y-coordinate of the Point
        self.__Y = Y

    def distance(self, newpoint):
        # Method to calculate the Euclidean distance between two points
        D = ((newpoint.get_X() - self.__X) ** 2 + (newpoint.get_Y() - self.__Y) ** 2) ** 0.5
        return D

    def norm(self):
        # Method to calculate the Euclidean norm of the Point
        N = (self.__X ** 2 + self.__Y ** 2) ** 0.5
        return N
