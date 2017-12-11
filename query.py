class Query:
    __data = []

    def __init__(self, var_list):
        self.__data = var_list

    def facts(self, q):
        for char in self.__data:
            for c in q[0]:
                if char == c:
                    print char, "has a value of", self.__data[char]
