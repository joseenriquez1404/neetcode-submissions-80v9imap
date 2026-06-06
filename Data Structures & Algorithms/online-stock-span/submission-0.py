from collections import deque

class StockSpanner:

    def __init__(self):
        self.prices = deque()

    def next(self, price: int) -> int:
        self.prices.append(price)
        span = 0
        lastmin = price
        for i in range(len(self.prices) - 1, -1, -1):
            if self.prices[i] <= lastmin:
                span += 1
            else:
                break
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


"""
Span -> Numero maximo de dias consecutivos 
desde ese dia para atras donde el precio de la accion era menor o igual
"""