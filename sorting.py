
class sorting:

    def __init__(self) -> None:
        pass

    def run_sort(self, arr):
        self.bubble_sort(arr[:])
        self.insertion_sort(arr[:])
        self.quick_sort_1(arr[:])
        self.merge_sort(arr[:])
        return

    def bubble_sort(self, arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        
        print(f"Result of bubble sort: {arr}")

    def insertion_sort(self, arr):
        #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(1, len(arr)):
            j = i - 1
            key = arr[i]
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

        print(f"Result of insertion sort: {arr}")

    #with the assumption of last element as the pivot
    def quick_sort_1(self, arr):
        low = 0
        high = len(arr) - 1
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1

        def quick_sort(arr, low, high):
            if low < high:
                pivot_adjusted = partition(arr, low, high)
                quick_sort(arr, low, pivot_adjusted - 1)
                quick_sort(arr, pivot_adjusted + 1, high)

        quick_sort(arr, low, high)
        print(f"Result of quick sort:  {arr}")

    def merge_sort(self, arr):
        
        def merge(arr, left, mid, right):
            left_arr = [arr[i] for i in range(left, mid+1)]
            right_arr = [arr[i] for i in range(mid+1, right+1)]
            left_idx , right_idx = 0, 0
            idx = 0
            while left_idx < len(left_arr) and right_idx < len(right_arr):
                if left_arr[left_idx] < right_arr[right_idx]:
                    arr[idx] = left_arr[left_idx]
                    left_idx += 1
                else:
                    arr[idx] = right_arr[right_idx]
                    right_idx += 1
                idx += 1

            while left_idx < len(left_arr):
                arr[idx] = left_arr[left_idx]
                left_idx += 1
                idx += 1

            while right_idx < len(right_arr):
                arr[idx] = right_arr[right_idx]
                right_idx += 1
                idx += 1

        def divide(arr, left, right):
            
            mid = left + (right - left) // 2
            if left >= right:
                return
            #branching out until the array size becomes one
            divide(arr, left, mid)
            divide(arr, mid+1, right)
            #now merge arrays starting with the arrays of length 1
            merge(arr, left, mid, right)
        
        divide(arr, 0, len(arr)-1)
        print(f"Result of merge sort: {arr}")


    
    #with the assumption that the first element is the pivot
    def quick_sort_2(self, arr):
        pass


if __name__ == "__main__":
    arr = [3, 2, 1]
    s = sorting()
    s.run_sort(arr) 