import os

while True:
    line = input()
    if line == 'End':
        break

    command, filename, *args = line.split('-')

    if command == 'Create':
        open(filename, 'w').close()
    elif command == 'Add':
        with open(filename, 'a') as f:
            f.write(f'{args[0]}\n')
    elif command == 'Replace':
        try:
            with open(filename, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print('An error occurred')
        else:
            with open(filename, 'w') as f:
                content = content.replace(args[0], args[1])
    elif command == 'Delete':
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print('An error occurred')

'''
Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End
'''
