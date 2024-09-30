import heapq

class Order:
    def __init__(self, order_id, side, price, quantity):
        self.order_id = order_id
        self.side = side  # 'buy' or 'sell'
        self.price = price
        self.quantity = quantity

    def __lt__(self, other):
        # Used for comparing orders in the heap
        if self.side == 'buy':
            return self.price > other.price  # Max-heap for buys
        else:
            return self.price < other.price  # Min-heap for sells

class OrderBook:
    def __init__(self):
        self.buy_orders = []  # Max-heap for buy orders
        self.sell_orders = []  # Min-heap for sell orders
        self.order_id_counter = 0  # Unique order ID generator

    def add_order(self, side, price, quantity):
        self.order_id_counter += 1
        order = Order(self.order_id_counter, side, price, quantity)

        if side == 'buy':
            heapq.heappush(self.buy_orders, order)
        else:
            heapq.heappush(self.sell_orders, order)

        return order

    def match_orders(self):
        while self.buy_orders and self.sell_orders:
            best_buy = self.buy_orders[0]
            best_sell = self.sell_orders[0]

            # If the best buy price is higher than or equal to the best sell price, a match is made
            if best_buy.price >= best_sell.price:
                quantity = min(best_buy.quantity, best_sell.quantity)
                
                print(f"Matched Order: Buy {quantity} @ {best_sell.price}")
                
                best_buy.quantity -= quantity
                best_sell.quantity -= quantity

                # Remove the completed order from the heap
                if best_buy.quantity == 0:
                    heapq.heappop(self.buy_orders)
                if best_sell.quantity == 0:
                    heapq.heappop(self.sell_orders)
            else:
                break

class OrderMatchingEngine:
    def __init__(self):
        self.order_book = OrderBook()

    def place_order(self, side, price, quantity):
        order = self.order_book.add_order(side, price, quantity)
        print(f"Placed Order: {side.capitalize()} {quantity} @ {price}")
        self.order_book.match_orders()

# Example usage
if __name__ == "__main__":
    engine = OrderMatchingEngine()

    # Place buy and sell orders
    engine.place_order('buy', 100, 10)
    engine.place_order('sell', 95, 5)
    engine.place_order('sell', 100, 8)
    engine.place_order('buy', 105, 7)
