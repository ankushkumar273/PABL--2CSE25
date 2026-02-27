def spiral_traversal(mat):
    if not mat or not mat[0]:
        return []

    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1

    result = []

    while top <= bottom and left <= right:

        # Traverse from Left to Right
        for col in range(left, right + 1):
            result.append(mat[top][col])
        top += 1

        # Traverse from Top to Bottom
        for row in range(top, bottom + 1):
            result.append(mat[row][right])
        right -= 1

        if top <= bottom:
            # Traverse from Right to Left
            for col in range(right, left - 1, -1):
                result.append(mat[bottom][col])
            bottom -= 1

        if left <= right:
            # Traverse from Bottom to Top
            for row in range(bottom, top - 1, -1):
                result.append(mat[row][left])
            left += 1

    return result
