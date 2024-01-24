--->https://my.newtonschool.co/playground/code/gah0x2wuvq2w


def count_elimination_ways(row):
    segments = []
    current_color = row[0]
    current_length = 1

    for i in range(1, len(row)):
        if row[i] == current_color:
            current_length += 1
        else:
            segments.append((current_length, current_color))
            current_color = row[i]
            current_length = 1

    segments.append((current_length, current_color))

    m = len(segments)

    # Criteria 1: The total number of segments m is odd
    if m % 2 == 0:
        return 0

    middle_index = m // 2

    # Criteria 2: The number of balls in the middle segment should be at least 2
    if segments[middle_index][0] == 1:
        return 0

    # Criteria 3: Check all pairs of segments symmetrically
    for i in range(1, middle_index + 1):
        left_index = middle_index - i
        right_index = middle_index + i

        if (
            left_index >= 0 and right_index < m and
            (segments[left_index][0] + segments[right_index][0] >= 3)and
            segments[left_index][1] == segments[right_index][1]
        ):
            continue
        else:
            return 0

    return segments[middle_index][0] + 1

# Input
row = input().strip()

# Output
result = count_elimination_ways(row)
print(result)
