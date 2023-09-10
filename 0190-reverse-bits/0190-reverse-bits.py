class Solution:
    def reverseBits(self, n: int) -> int:
        bit = bin(n)[2:]
        bit = "0" * (32 - len(bit)) + bit
        return int(bit[::-1], 2)