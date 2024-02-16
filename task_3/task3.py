
from pathlib import Path
import sys
from colorama import init, Fore

init()


def inside(path):
        dirpath = Path(path)
        items =  dirpath.iterdir()

        for item in items:
            if item.is_dir():
               print(f'{Fore.BLUE}--{item.name} {Fore.LIGHTMAGENTA_EX} is a directory')
               inside(item)      

            elif item.is_file():
                print(f'{Fore.GREEN}-----{item.name} {Fore.LIGHTMAGENTA_EX} is a file')

def display_directory_structure():
    if len(sys.argv)<2:
        user_input = ''
    else:
        user_input= sys.argv[1]    

    try:
       inside(user_input)

    except Exception as e:
        print(f"{Fore.RED} {e}")    


if __name__ == "__main__":
    display_directory_structure()    



