def example_function(lst):
    """
    This function takes in a list of integers and performs various operations.
    """
    # Check if the list is empty
    if not lst:
        return None
    # Calculate the sum of the list
    total = sum(lst)


    # Find the maximum value in the list
    max_value = max(lst)

    # Find the minimum value in the list
    min_value = min(lst)

    # Calculate the average of the list
    avg = total / len(lst)

    # Create a new list with only even numbers
    even_nums = [num for num in lst if num % 2 == 0]

    # Create a new list with only odd numbers
    odd_nums = [num for num in lst if num % 2 != 0]

    # Return a dictionary with all the calculated values
    return {
        "sum": total,
        "max": max_value,
        "min": min_value,
        "average": avg,
        "even_nums": even_nums,
        "odd_nums": odd_nums
    }
