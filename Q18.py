
def reverse_subsegment(arr, start, end):

    # Reverse the selected segment in-place
    while start < end:

        # Swap the elements
        arr[start], arr[end] = arr[end], arr[start]

        # Move both pointers inward
        start += 1
        end -= 1

    return arr


arr = list(map(int, input("Enter the array: ").split()))

start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

reverse_subsegment(arr, start, end)

print("Modified array:", arr)
