def longest_hike(trail, k):
    start = 0
    max_length = 0

    for end in range(1, trail.length):
        while start < end and trail[end] - trail[end - 1] > k:
            start += 1
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage:
trail = [4, 2, 1, 4, 3, 4, 5, 8, 15]
k = 3
print(longest_hike(trail, k))  # Output: 5


