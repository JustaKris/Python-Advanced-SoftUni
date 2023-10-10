class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    number = float(input())
    if number < 0:
        raise ValueCannotBeNegative

'''
1
4
-5
3
10
'''
