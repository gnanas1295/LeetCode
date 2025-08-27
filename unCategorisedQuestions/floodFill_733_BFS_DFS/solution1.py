from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        rows = len(image)
        columns = len(image[0])
        originalColour = image[sr][sc]

        if originalColour == color:
            return image

        def fill(r, c):

            if (0 <= r < rows) and (0 <= c < columns) and originalColour == image[r][c]:
                image[r][c] = color
                fill(r + 1, c)
                fill(r - 1, c)
                fill(r, c + 1)
                fill(r, c - 1)

        fill(sr, sc)

        return image
