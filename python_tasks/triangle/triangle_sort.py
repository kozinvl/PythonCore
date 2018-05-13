"""Sorting triangles

The Program takes name and triangle's sides.
After adding a new triangle will be calculated area.
If the user doesn't want to add triangle, he has to answer "y" or "yes"
will be shown sorted area result of all triangles.

"""


class Triangle(object):
    def __init__(self, name: str, a: float, b: float, c: float) -> None:
        self.__name = name
        self.__a = a
        self.__b = b
        self.__c = c
        self.__square = 0.0

    @staticmethod
    def is_validated(a, b, c) -> bool:
        """Validation of user arguments"""
        try:
            float(a)
            float(b)
            float(c)
        except ValueError:
            return False
        if (float(a) + float(b) > float(c) and
            float(a) + float(c) > float(b) and
            float(b) + float(c) > float(a)) and \
                min(float(a), float(b), float(c)) > 0:
            return True
        else:
            return False

    def calc_square(self) -> float:
        """Calculation of triangle square"""
        p = (self.__a + self.__b + self.__c) / 2
        self.__square = round(((p * (p - self.__a) * (p - self.__b)
                                * (p - self.__c)) ** 0.5), 3)
        return self.__square

    def get_sq(self) -> float:
        return self.__square

    def __repr__(self):
        return "{} : {}".format(self.__name, self.__square)


def select_process():
    user_arg = input("Do you want to continue? ")
    if user_arg.lower() in ('y', 'yes'):
        return True
    else:
        return False


def main():
    triangles_list = []
    is_continue = True
    while is_continue:
        get_arg = input("Input data of triangle with comma ")
        triangle_data = get_arg.split(",")
        if len(triangle_data) == 4 and \
                Triangle.is_validated((triangle_data[1]),
                                      (triangle_data[2]),
                                      triangle_data[3]):
            new_triangle = Triangle(
                str(triangle_data[0]),
                float(triangle_data[1]),
                float(triangle_data[2]),
                float(triangle_data[3]))
            new_triangle.calc_square()
            triangles_list.append(new_triangle)
            print("Triangle has been added")
        else:
            print("Invalid arguments have been entered")

        is_continue = select_process()

    print("=====Triangle list:=====")
    sort_triangles = sorted(triangles_list,
                            key=lambda i: i.get_sq(), reverse=True)
    for triangle in sort_triangles:
        print(triangle, end="\n")


if __name__ == '__main__':
    main()
