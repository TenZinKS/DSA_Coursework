def most_utilized_class(n, classes):
    #Sort classes by start time and then by number of students if they have the same start time
    classes.sort(key=lambda x: (x[0], -x[2]))
    
    #Initialize lists to track room availability and room usage
    room_end_time = [0] * n  # When each room will be free
    room_count = [0] * n     # Number of classes each room handles
    
    #Process each class
    for start, end, students in classes:
        # Find the earliest available room
        earliest_room = 0
        for i in range(1, n):
            if room_end_time[i] < room_end_time[earliest_room]:
                earliest_room = i
        
        # If the room is free by the start time, assign the class to that room
        if room_end_time[earliest_room] <= start:
            room_end_time[earliest_room] = end
        else:
            # Delay the class until the room is free
            room_end_time[earliest_room] += (end - start)
        
        # Update the room usage count
        room_count[earliest_room] += 1
    
    #Determine the most utilized room
    max_classes = max(room_count)
    for i in range(n):
        if room_count[i] == max_classes:
            return i

# Example Usage
n1 = 2
classes1 = [[0, 10, 30], [1, 5, 25], [2, 7, 20], [3, 4, 10]]
print(most_utilized_class(n1, classes1))  # Output: 0

n2 = 3
classes2 = [[1, 20, 30], [2, 10, 25], [3, 5, 20], [4, 9, 15], [6, 8, 10]]
print(most_utilized_class(n2, classes2))  # Output: 1


