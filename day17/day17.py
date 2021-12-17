import sys

expected_velocity_range = range(-200, 200)


def read_file() -> ((int, int), (int, int)):
    with open("input.txt") as fp:
        line = fp.readline().rstrip()
        _, line = line.split(": ")
        x, y = line.split(", ")
        _, x = x.split("=")
        x_start, x_end = x.split("..")
        _, y = y.split("=")
        y_start, y_end = y.split("..")
        return (int(x_start), int(x_end)), (int(y_start), int(y_end))


def step(current: (int, int), x_velocity: int, y_velocity: int) -> ((int, int), int, int):
    x, y = current
    x += x_velocity
    y += y_velocity
    if x_velocity > 0:
        x_velocity -= 1
    elif x_velocity < 0:
        x_velocity += 1
    y_velocity -= 1
    return (x, y), x_velocity, y_velocity


def is_in_target_area(current, target) -> bool:
    x, y = current
    target_x, target_y = target
    x_start, x_end = target_x
    y_start, y_end = target_y
    return x_start <= x <= x_end and y_start <= y <= y_end


def is_outside(current, target) -> bool:
    x, y = current
    target_x, target_y = target
    x_start, x_end = target_x
    y_start, y_end = target_y
    return x > x_end or y < y_start


def get_max_y(trajectory: list) -> int:
    max_y = -sys.maxsize
    for p in trajectory:
        x, y = p
        if y > max_y:
            max_y = y
    return max_y


def part1(target: (int, int)) -> int:
    max_y = -sys.maxsize
    for x in expected_velocity_range:
        for y in expected_velocity_range:
            current = (0, 0)  # start
            trajectory = []
            x_velocity = x
            y_velocity = y
            while not is_outside(current, target):
                current, x_velocity, y_velocity = step(current, x_velocity, y_velocity)
                trajectory.append(current)
                if is_in_target_area(current, target):
                    trajectory_max_y = get_max_y(trajectory)
                    if trajectory_max_y > max_y:
                        max_y = trajectory_max_y
    return max_y


def part2(target: (int, int)) -> int:
    valid = []
    for x in expected_velocity_range:
        for y in expected_velocity_range:
            current = (0, 0)  # start
            x_velocity = x
            y_velocity = y
            while not is_outside(current, target):
                current, x_velocity, y_velocity = step(current, x_velocity, y_velocity)
                if is_in_target_area(current, target):
                    valid.append((x, y))
    return len(set(valid))


if __name__ == "__main__":
    target = read_file()
    print(f"Part 1: {part1(target)}")
    print(f"Part 2: {part2(target)}")
