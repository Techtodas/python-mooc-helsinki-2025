# Write your solution here
def create_tuple(x: int, y: int, z: int):
    least = min(x, y, z)
    greatest = max(x, y, z)
    sum = (x+y+z)
    result = (least, greatest, sum)

    return result


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))