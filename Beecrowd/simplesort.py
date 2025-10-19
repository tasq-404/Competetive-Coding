a, b, c = map(int, input().split())

# Store the original inputs
original_inputs = [a, b, c]

# Sorting the inputs
sorted_inputs = sorted(original_inputs)

# Printing the sorted values
for value in sorted_inputs:
    print(value)

print("")  # Adding a blank line between the two outputs

# Printing the original values
for value in original_inputs:
    print(value)