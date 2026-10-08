def find_min_drops(floors: int) -> int:
    covered_floors = 0
    for drops in range(1, floors + 1):
        covered_floors += drops
        if covered_floors >= floors:
            return drops
    return floors


def find_critical_floor(total_floors: int = 100, critical_floor: int = 67) -> tuple[int, int]:
    k = find_min_drops(total_floors)
    drops = 0
    previous_floor = 0
    step = k

    while previous_floor + step <= total_floors:
        current_floor = previous_floor + step
        drops += 1

        if current_floor >= critical_floor:
            for f in range(previous_floor + 1, current_floor + 1):
                drops += 1
                if f >= critical_floor:
                    return drops, f
        else:
            previous_floor = current_floor
            step -= 1

    return drops, -1


if __name__ == "__main__":
    floors = 100
    target_floor = int(input("Enter the critical floor (1-100): "))  # Hidden
    total_drops, found = find_critical_floor(floors, target_floor)

    print("Number of floors:", floors)
    print("Critical floor:", found)
    print("Total drops:", total_drops)
