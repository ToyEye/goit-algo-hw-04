import pathlib
import sys
from colorama import init, Fore

init()


def display_directory_structure():
    if len(sys.argv)<2:
        user_input = ''
    else:
        user_input= sys.argv[1]    

    path = pathlib.Path(user_input)

    if path.exists():
        if path.is_dir():
           items =  path.iterdir()
           for item in items:
               print(f'{Fore.BLUE}{item}')


        else:
            print(f'{Fore.RED}{path} is a file')
    else:
        print(f"{Fore.RED}{path.absolute()} not exist")    


if __name__ == "__main__":
    display_directory_structure()