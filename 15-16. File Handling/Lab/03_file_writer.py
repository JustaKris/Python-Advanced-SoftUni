import os

FILE_NAME = "my_first_file.txt"
WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(WORKING_DIRECTORY, FILE_NAME)

with open(FILE_PATH, 'w') as f:
    f.write('I just created my first file!')

# with open(FILE_PATH, 'r') as f:
#     print(f.read())
