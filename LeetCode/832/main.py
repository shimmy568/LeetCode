class Solution:

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for x in range(len(A)):
            A[x].reverse()
            A[x] = list(map(lambda a: int(not a), A[x]))
        return A
