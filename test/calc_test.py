from calc import square
# import pytest

def test_square_pos():
    assert(square(2)) == 4
    assert(square(3)) == 9

def test_square_neg():
    assert(square(-2)) == 4
    assert(square(-3)) == 9

def test_square_zero():
    assert(square(0)) == 0

#pytest 


# region OldTestingMechanism
# def main():
#     test_square()

# def test_square():
    # try:
    #     assert(square(2)) == 4
    # except AssertionError:
    #     print("Not correct 2")
    # try:
    #     assert(square(3)) == 9
    # except AssertionError:
    #     print("Not correct 3")
    # try:
    #     assert(square(-3)) == 9
    # except AssertionError:
    #     print("Not correct -3")
    # try:
    #     assert(square(0)) == 0
    # except AssertionError:
    #     print("Not correct 0")
    

# if __name__ == "__main__":
#     main()
# endregion
