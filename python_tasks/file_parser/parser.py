"""FileParser

The program's working with two ways:
1. Reads the number of occurrences of a string in a text file.
2. Makes changing a string to another in the specified file.
The program accepts input arguments at startup:
1. <path to file> <string for counting>
2. <path to file> <string to search> <string to replace>

"""

import sys


class FileParser(object):
    def __init__(self, file_name) -> None:
        self.__file_name = file_name

    def count_text(self, str_count) -> str:
        """counting required strings"""
        with open(self.__file_name, 'r') as file:
            this_file = file.read()
            count_text = this_file.count(str_count)
        return "\'{}\': has been found {} times".format(
            str_count, count_text)

    def preparing_replace(self, str_delete, str_change):
        """finding required string"""
        try:
            with open(self.__file_name, 'r') as file:
                this_file = file.read()
            this_file = this_file.replace(str_delete, str_change)
            return this_file
        except FileNotFoundError:
            print("File hasn't been found!")
            quit()

    def replace_text(self, this_file):
        """replacing required string"""
        try:
            with open(self.__file_name, 'w') as file:
                file.write(this_file)
            print("Text has been changed")
        except FileNotFoundError:
            print("File hasn't been found")


def main():
    if len(sys.argv) == 3:
        new_parser = FileParser(sys.argv[1])
        print(new_parser.count_text(sys.argv[2]))
    elif len(sys.argv) == 4:
        new_parser = FileParser(sys.argv[1])
        change_lines = new_parser.preparing_replace(sys.argv[2], sys.argv[3])
        new_parser.replace_text(change_lines)
    else:
        print("Invalid data has been entered")


if __name__ == '__main__':
    main()
