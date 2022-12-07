import re
from typing import Optional


outputs = open("shell.txt", "r").read()


class File:
    def __init__(self, size, name):
        self.__size = size
        self.__name = name

    def size(self):
        return self.__size

    def name(self):
        return self.__name


class Directory:
    def __init__(self, name, parent=None):
        self.__name: str = name
        self.__parent: Optional[Directory] = parent

        self.__files: list[File] = []
        self.__sub_dirs: list[Directory] = []

    def get_size(self) -> int:
        return sum(file.size() for file in self.__files) + sum(dir.get_size() for dir in self.sub_dirs())

    def name(self):
        return self.__name

    def parent(self):
        return self.__parent

    def files(self):
        return self.__files

    def sub_dirs(self):
        return self.__sub_dirs


def main():
    current_dir: Directory = Directory("/")

    for _, output in enumerate(outputs.split('\n')):
        cd_match = re.search(r"\$ cd ((.|\/|\.)+)", output)
        file_match = re.search(r"(\d+) ((\w|\/|\.)+)", output)
        dir_match = re.search(r"dir (.+)", output)

        if cd_match:
            cd_name = cd_match.group(1)

            if cd_name == "/":
                continue

            if cd_name == "..":  # move up to parent dir
                current_dir = current_dir.parent()
            else:
                dir = next((dir for dir in current_dir.sub_dirs()
                           if dir.name() == cd_name), None)
                current_dir = dir

        if dir_match:
            dir_name = dir_match.group(1)
            dir = Directory(dir_name, current_dir)
            current_dir.sub_dirs().append(dir)

        if file_match:
            file = File(int(file_match.group(1)), file_match.group(2))
            current_dir.files().append(file)

    root_dir = current_dir.parent()
    print(calculate_size(root_dir))

    required_space = 30000000 - (70000000 - root_dir.get_size())
    print("required size: " + str(required_space))
    print(calculate_delete_size(required_space, root_dir, root_dir.get_size()))


def calculate_size(dir: Directory):
    dirs = 0

    for sub_dir in dir.sub_dirs():
        if sub_dir.get_size() <= 100000:
            dirs += sub_dir.get_size()
        dirs += calculate_size(sub_dir)

    return dirs


def calculate_delete_size(required_space, dir: Directory, proposed_dir_size):
    for sub_dir in dir.sub_dirs():
        if sub_dir.get_size() >= required_space:
            proposed_dir_size = proposed_dir_size if proposed_dir_size < sub_dir.get_size(
            ) else sub_dir.get_size()

            proposed_sub_dir_size = calculate_delete_size(
                required_space, sub_dir, sub_dir.get_size())

            proposed_dir_size = proposed_sub_dir_size if proposed_sub_dir_size < proposed_dir_size else proposed_dir_size

    return proposed_dir_size


if __name__ == "__main__":
    main()
