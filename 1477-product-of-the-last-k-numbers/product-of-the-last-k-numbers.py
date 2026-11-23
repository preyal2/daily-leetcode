class ProductOfNumbers:

    def __init__(self):
        # Initialize with 1 as a neutral base for multiplication
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset prefix products since any future product including this 0 will be 0
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k reaches past the last reset (0), the product is 0
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-k - 1]