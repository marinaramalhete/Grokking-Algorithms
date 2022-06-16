class BinarySearch():

    def search_iterative(self, list, item):
        # low and high keep track of which part of the list you'll search in
        low = 0
        high = len(list) - 1

        # while you haven't narrowed it down to one element
        while low <= high:

            # check the middle element
            middle = (low+high) // 2
            guess = list[middle]

            # found the item
            if guess == item:
                return middle
            # the guess was too high
            elif guess > item:
                high = middle - 1
            # the guess was too low
            else:
                low = middle + 1

        # item doesn't exist
        return None

    def search_recursive(self, list, low, high, item):
        # check base case
        if high >= low:

            middle = (low+high) // 2
            guess = list[middle]

            # if element is present at the middle itself
            if guess == item:
                return middle
            # if element is smaller than  middle, then it can only
            # be present in left subarray
            elif guess > item:
                return self.search_recursive(list, low, middle - 1, item)
            # else the element can only be present in right subarray
            else:
                return self.search_recursive(list, middle + 1, high, item)

        else:
            # element is not present in the array
            return None


if __name__ == "__main__":
    # we must initialize the class to use the methods of this class
    bs = BinarySearch()
    my_list = [1, 3, 5, 7, 9]

    print(bs.search_iterative(my_list, 3))
    print(bs.search_iterative(my_list, -1))
