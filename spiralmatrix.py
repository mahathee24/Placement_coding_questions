matrix = [
    [1, 2, 3, 20],
    [4, 5, 6, 30],
    [7, 8, 9, 40],
    [10,11,12,50]
]

rows = len(matrix)
col = len(matrix[0])

top = 0
bottom = rows - 1
left = 0
right = col - 1
res = []

while top <= bottom and left <= right:
    # 1 Left to Right
    for i in range(left, right + 1):
        res.append(matrix[top][i])
    top += 1

    # 2 Top to Bottom
    for i in range(top, bottom + 1):
        res.append(matrix[i][right])
    right -= 1

    # 3. Right to Left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1

    # 4. Bottom to Top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

print(res)
