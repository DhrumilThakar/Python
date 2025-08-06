list = [5, 7, 6, 8]
list.sort()  # Sort the list in ascending order
first_element = list[0]  # Get the first element
count = 0  # Initialize the count

for i in list:
    if i > first_element:
        count += 1  # Increment the count if the current element is greater than the first element

print(count)  # Print the count