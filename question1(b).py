def rotate_char(c, direction):
    # Rotate character clockwise
    if direction == 1:
        return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
    # Rotate character counter-clockwise
    elif direction == 0:
        return chr((ord(c) - ord('a') - 1) % 26 + ord('a'))

def apply_shifts(s, shifts):
    # Convert string to list for easy manipulation
    s = list(s)
    
    # Apply each shift in the given list of shifts
    for start, end, direction in shifts:
        for i in range(start, end + 1):
            s[i] = rotate_char(s[i], direction)
    
    # Convert the list back to a string
    return ''.join(s)

# Example usage
s = "hello"
shifts = [[0, 1, 1], [2, 3, 0], [0, 2, 1]]
result = apply_shifts(s, shifts)
print(result)  # Output: "jglko"
