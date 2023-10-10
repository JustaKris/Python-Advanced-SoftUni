import os

FILE_NAME = "my_first_file.txt"
WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(WORKING_DIRECTORY, FILE_NAME)

# with open(FILE_PATH, 'w') as f:
#     f.write('I just created my first file!')

try:
    os.remove(FILE_PATH)
except FileNotFoundError:
    print("File already deleted!")
