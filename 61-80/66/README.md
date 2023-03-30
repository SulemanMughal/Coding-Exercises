# Exercise No. 66

Two lists are part of the same zipper if the ending is identical. The identical section can be thought of as being "zipped-up". Below, [2, 2, 4] is "zipped-up".

-   List 1: [3, 5, 8, 9, 2, 2, 4]
-   List 2: [1, 7, 2, 2, 4]

Create a Python program that takes in two lists. Return False if none of the list is "zipped." Return True if the lists are identical. Otherwise, return a list with the first index in each list where the zipper diverges.