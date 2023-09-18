class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = [None] * len(mat)
        for idx, row in enumerate(mat):
            arr[idx] = (sum(row), idx)

        arr.sort(key=lambda x: x[0])
        return [arr[i][1] for i in range(k)]