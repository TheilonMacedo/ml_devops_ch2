def nearest_square(num):
    """
    Find the nearest square number to num
    """
    root = 0
    while (root + 1) ** 2 <= num:
        root += 1
    return root ** 2