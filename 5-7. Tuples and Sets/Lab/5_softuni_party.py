number_of_guests = int(input())

reservations = set()

for _ in range(number_of_guests):
    reservations.add(input())

while True:
    guest_number = input()
    if guest_number == "END":
        break
    if guest_number in reservations:
        reservations.remove(guest_number)

print(len(reservations))
print(*sorted(reservations), sep="\n")
