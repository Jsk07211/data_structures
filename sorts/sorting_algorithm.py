class SortingAlgorithm:
    def __init__(self, type):
        self.type = type

    def change_type(self, type):
        self.type = type

    def sort(self, nums):
        if self.type == "bubble":
            self.bubble_sort(nums)
        elif self.type == "select":
            self.selection_sort(nums)
        elif self.type == "insert":
            self.insertion_sort(nums)
        elif self.type == "merge":
            self.merge_sort(nums, 0, len(nums))
        
    def bubble_sort(self, nums):
        swap = False

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    swap = True

            # Flag to reduce time spent sorting sorted array
            if not swap:
                break
        return

    def selection_sort(self, nums):
        for i in range(len(nums)):
            min_index = i

            for j in range(i + 1, len(nums)):
                if nums[min_index] > nums[j]:
                    min_index = j

            # Swap step
            temp = nums[i]
            nums[i] = nums[min_index]
            nums[min_index] = temp
        return

    def insertion_sort(self, nums):
        for i in range(1, len(nums)):
            current = nums[i]

            j = i - 1

            while j >= 0 and nums[j] > current:
                nums[j + 1] = nums[j]
                j -= 1
            # Swap step
            nums[j + 1] = current
        return

    # Exclusive of high
    def merge_sort(self, nums, low, high):
        if low >= high - 1:
            return
        mid = (low + high) // 2
        self.merge_sort(nums, low, mid)
        self.merge_sort(nums, mid, high)
        
        self.merge(nums, low, high)

    # O(m + n)
    def merge(self, nums, low, high):
        mid = (low + high) // 2
        sorted_arr = [0] * (high - low + 1)

        i, j, k = low, mid, 0

        while i < mid and j < high:
            if nums[i] <= nums[j]:
                sorted_arr[k] = nums[i]
                i += 1
            else:
                sorted_arr[k] = nums[j]
                j += 1
            k += 1

        # Only one of these while loops will execute 
        # Since one has to be false to break out of the first while loop
        while i < mid:
            sorted_arr[k] = nums[i]
            i += 1
            k += 1

        while j < high:
            sorted_arr[k] = nums[j]
            j += 1
            k += 1
        
        k = 0
        # Overwriting array
        for l in range(low, high):
            nums[l] = sorted_arr[k]
            k += 1