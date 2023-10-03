n = int(input())

car_numbers = set()
for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        car_numbers.add(car_number)
    else:
        if car_number in car_numbers:
            car_numbers.remove(car_number)

if car_numbers:
    print(*car_numbers, sep="\n")

else:
    print("Parking Lot is Empty")

'''
10
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
IN, CA9999TT
IN, CA2866HI
OUT, CA1234TA
IN, CA2844AA
OUT, CA2866HI
IN, CA9876HH
IN, CA2822UU

4
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
OUT, CA1234TA
'''