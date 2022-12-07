import re
from typing import Optional


outputs = open("shell.txt", "r").read()

class File:
    def __init__(self):
        self.__size = 0


class Directory:
    def __init__(self, name):
        self.__name: str = name
        self.__parent: Optional[Directory] = None
        self.__files: list[File] = []
        self.__sub_directories: list[Directory] = []
        
    def get_contents_size() -> int:
        return 0
    
    def name(self):
        return self.__name
    
    def parent(self):
        return self.__parent
    
    def sub_dirs(self):
        return self.__sub_directories

def main():
    current_directory: Directory = Directory("/")
    root_directories: list[Directory] = []
    
    for _, output in enumerate(outputs.split('\n')):
        match = re.search(r"\$ cd (\w|\/|\.+)", output)
        if match:
            dir_name = match.group(1)
            
            
            if dir_name == current_directory.name():
                continue
            elif dir_name == "..": # move up to parent dir
                current_directory = current_directory.parent()
            elif dir_name:
                dir = next((obj for obj in root_directories if obj.name == dir_name), Directory(dir_name))
                
                current_directory.sub_dirs().append(dir)
                current_directory = dir
            
            
            
    
    
    
if __name__ == "__main__":
    main()