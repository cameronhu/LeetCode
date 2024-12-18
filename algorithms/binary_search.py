def binary_search(nums: list[int], value: int) -> int:
    """_summary_

    Args:
        nums (List[int]): sorted list to find the value
        value (int): value to find in the sorted list

    Returns:
        int: Index of the value
    """
    frontIndex: int = 0
    endIndex: int = len(nums) - 1

    while frontIndex <= endIndex:
        middleIndex: int = (frontIndex + endIndex) // 2
        middleValue = nums[middleIndex]
        if middleValue == value:
            return middleIndex
        elif middleValue < value:
            frontIndex = middleIndex + 1
        else:  # middleValue > value
            endIndex = middleIndex - 1

    return -1


if __name__ == "__main__":

    test1 = [1, 2, 3, 4, 5, 6]

    print(binary_search(test1, 3))
    print(binary_search(test1, 2))
    print(binary_search(test1, 1))
    print(binary_search(test1, 6))

    print("Test 2 \n")
    test2 = [1, 3, 5, 7, 8, 9, 10]
    print(binary_search(test2, 7))
    print(binary_search(test2, 8))
    print(binary_search(test2, 9))
