from collections import deque

food_supplies = [int(food) for food in input().split(', ')]
stamina = deque(int(x) for x in input().split(', '))

peaks = {
    80: 'Vihren',
    90: 'Kutelo',
    100: 'Banski Suhodol',
    60: 'Polezhan',
    70: 'Kamenitza'
}

conquered_peaks = []

while food_supplies and stamina:
    food = food_supplies.pop()
    current_stamina = stamina.popleft()
    result = food + current_stamina
    current_peak_value = list(peaks.keys())[0]

    if result >= current_peak_value:
        conquered_peaks.append(peaks[current_peak_value])
        del peaks[current_peak_value]
        if len(conquered_peaks) >= 5:
            print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
            break
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks:")
    for peak in conquered_peaks:
        print(peak, end='\n')

'''Test input 1
40, 40, 40, 40, 40, 40, 40
40, 50, 60, 20, 30, 5, 2
'''
''' Test input 2
10, 20, 34, 26, 12, 10, 45
30, 28, 17, 17, 13, 10, 10
'''