# import pathlib
# import sys
# from colorama import init, Fore

# init()


# def inside(path):
#         if path.is_dir():
#            items =  path.iterdir()
#            for item in items:
#                print(f'{Fore.BLUE}--{item} {Fore.LIGHTMAGENTA_EX} is a directory')
#                inside(item)      

#         elif path.is_file():
#             print(f'{Fore.GREEN}-----{path} {Fore.LIGHTMAGENTA_EX} is a file')

# def display_directory_structure():
#     if len(sys.argv)<2:
#         user_input = ''
#     else:
#         user_input= sys.argv[1]    

#     path = pathlib.Path(user_input)

#     if path.exists():
#        inside(path)

#     else:
#         print(f"{Fore.RED}{path.absolute()} not exist")    


# if __name__ == "__main__":
#     display_directory_structure()



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



