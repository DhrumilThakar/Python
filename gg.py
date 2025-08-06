def pos(n):
    a = list(range(n))  # Create a list with numbers from 0 to n-1
    a.reverse()  # Reverse the list in place
    print(a)  # Print the reversed list

pos(4)  # Expected output: [3, 2, 1, 0]
