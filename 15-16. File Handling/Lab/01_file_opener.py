import os

FILE_NAME = "text.txt"
WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(WORKING_DIRECTORY, FILE_NAME)

try:
    file = open(FILE_PATH, "r")
    print("Found")
    # print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found")
