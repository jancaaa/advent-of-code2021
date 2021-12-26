from copy import deepcopy


def read_file(name: str = "input.txt") -> (str, list):
    with open(name) as fp:
        line = fp.readline()
        algorithm = line.rstrip()
        fp.readline()  # empty line
        line = fp.readline()
        image = []
        while line:
            line = line.rstrip()
            image.append(list(line))
            line = fp.readline()
        return algorithm, image


class Image:

    def __init__(self, image: list, background: str):
        self.image = image
        self.background = background

    def adjust_image(self) -> list:
        size_x = len(self.image[0])

        self.image.insert(0, [self.background for _ in range(size_x)])
        self.image.append([self.background for _ in range(size_x)])

        size_y = len(self.image)
        for y in range(size_y):
            self.image[y].insert(0, self.background)
            self.image[y].append(self.background)

    def enhance_image(self, algorithm: str) -> list:
        new_image = deepcopy(self.image)
        size_x = len(self.image[0])
        size_y = len(self.image)
        for y in range(size_y):
            for x in range(size_x):
                new_image[y][x] = self._enhance_pixel(x, y, algorithm)
        self.image = new_image

        # enhance background
        # ... ... ... -> 000 000 000 -> 0
        # ### ### ### -> 111 111 111 -> 511
        index = 0 if self.background == "." else 511
        self.background = algorithm[index]

    def _enhance_pixel(self, x: int, y: int, algorithm: str) -> str:
        max_x = len(self.image[0]) - 1
        max_y = len(self.image) - 1
        pixels = ""
        # first line (N)
        if y != 0:
            pixels += self.image[y - 1][x - 1] if x != 0 else self.background  # NW
            pixels += self.image[y - 1][x]  # N
            pixels += self.image[y - 1][x + 1] if x != max_x else self.background  # NE
        else:
            pixels += self.background * 3

        # second line (W, center, E)
        pixels += self.image[y][x - 1] if x != 0 else self.background  # W
        pixels += self.image[y][x]  # center
        pixels += self.image[y][x + 1] if x != max_x else self.background  # E

        # third line (S)
        if y != max_y:
            pixels += self.image[y + 1][x - 1] if x != 0 else self.background  # SW
            pixels += self.image[y + 1][x]  # S
            pixels += self.image[y + 1][x + 1] if x != max_x else self.background  # SE
        else:
            pixels += self.background * 3
        pixels = pixels.replace(".", "0")
        pixels = pixels.replace("#", "1")
        index = int(pixels, 2)
        return algorithm[index]

    def count_lighting_pixels(self) -> int:
        count = 0
        size_x = len(self.image[0])
        size_y = len(self.image)
        for y in range(size_y):
            for x in range(size_x):
                if self.image[y][x] == "#":
                    count += 1
        return count


def tests():
    algorithm, image = read_file("example.txt")
    assert part1(algorithm, image) == 35
    assert part2(algorithm, image) == 3351


def part1(algorithm: str, image: list) -> int:
    image = Image(image, ".")
    for _ in range(2):
        image.adjust_image()
        image.enhance_image(algorithm)

    return image.count_lighting_pixels()


def part2(algorithm: str, image: list) -> int:
    image = Image(image, ".")
    for _ in range(50):
        image.adjust_image()
        image.enhance_image(algorithm)

    return image.count_lighting_pixels()


if __name__ == "__main__":
    tests()
    algorithm, image = read_file()
    print(f"Part 1: {part1(algorithm, image)}")
    print(f"Part 2: {part2(algorithm, image)}")
