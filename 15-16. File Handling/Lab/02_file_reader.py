import os

FILE_NAME = "numbers.txt"
WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(WORKING_DIRECTORY, FILE_NAME)

try:
    file = open(FILE_PATH, "r")
    file_sum = 0
    for line in file.readlines():
        file_sum += int(line)
    print(file_sum)
    file.close()

except FileNotFoundError:
    print("File not found")
