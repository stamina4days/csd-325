# Name: Prince Hubbard
# Date: August 16, 2026
# Course: CSD325 Advanced Python
# Assignment: Module 1.3 Assignment
# Program: On the Wall
# Purpose: Ask the user how many bottles of beer are on the wall,
#          pass that number to a function, count backward to 1,
#          and remind the user to buy more beer.


def countdown(bottles):
    """Count backward from the starting number of bottles to 1."""

    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print("Take one down and pass it around.")

        bottles -= 1

        if bottles == 1:
            print("1 bottle of beer on the wall.\n")
        else:
            print(f"{bottles} bottles of beer on the wall.\n")

    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around.")
    print("No more bottles of beer on the wall.\n")


def main():
    bottles = int(input("How many bottles of beer are on the wall? "))

    countdown(bottles)

    print("Time to buy more beer!")


if __name__ == "__main__":
    main()
