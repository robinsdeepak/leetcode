class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {k: i for i, k in enumerate(order)}
        freq = Counter(s)
        keys = sorted(freq.keys(), key=lambda x: order_dict.get(x, 100))
        return "".join([(key * freq.get(key)) for key in keys])
