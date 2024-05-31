#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):

    # Get the length of the list
    length = len(list_of_integers)

    # Check if the list is empty
    if length == 0:
        return None

    # Initialize the start and end indices
    start = 0
    end = length - 1

    # Perform binary search
    while start < end:
        # Calculate the middle index
        mid = (start + end) // 2

        # Compare the middle element with its neighbors
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid

    # Return the peak element
    return list_of_integers[start]
