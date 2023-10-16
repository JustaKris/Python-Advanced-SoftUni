from collections import defaultdict


def accommodate_new_pets(capacity, max_weight_per_pet, *pets):

    accommodated_pets = defaultdict(int)  # Dict to keep track of accommodated pets
    result = ''  # String to return

    # Attempt to accommodate all pets
    for pet in pets:
        # Break if hotel is at full capacity
        if not capacity:
            result += "You did not manage to accommodate all pets!"
            break

        # Populate hotel if pet passes weight check
        pet_type, pet_weight = pet
        if pet_weight <= max_weight_per_pet:
            accommodated_pets[pet_type] += 1
            capacity -= 1

    else:
        result += f"All pets are accommodated! Available capacity: {capacity}."

    # Final additions to result
    result += '\nAccommodated pets:'
    for pet_type, count in sorted(accommodated_pets.items()):
        result += f"\n{pet_type}: {count}"

    return result


def main():
    # Test 1
    print(accommodate_new_pets(10, 15.0, ("cat", 5.8), ("dog", 10.0), ))
    # Test 2
    print(accommodate_new_pets(10, 10.0, ("cat", 5.8), ("dog", 10.5), ("parrot", 0.8), ("cat", 3.1), ))
    # Test 3
    print(accommodate_new_pets(2, 15.0, ("dog", 10.0), ("cat", 5.8), ("cat", 2.7), ))


if __name__ == '__main__':
    main()
