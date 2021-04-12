from store import *

class GroceryStore(Store):
    def __init__(self, total_rev, store_type):
        self.total_rev = total_rev
        self.store_type = store_type

    # def sell_items(self):
    #     self.