from functools import partial
from itertools import islice
from statistics import mean


class Order:
    def __init__(self, orderdata, discount=0):
        self.orderdata = orderdata
        self.discount = discount


Orderlist = []


class test:
    def __init__(self, order_list):
        self.order_list = order_list

    def isAQualified(self, order):
        return True

    def A(self, order):
        return 1

    def isBQualified(self, order):
        return True

    def B(self, order):
        return 1

    def isCQualified(self, order):
        return True

    def C(self, order):
        return 1

    def GetOrderwithDiscountForOneRule(self, order, rule):
        Qualify = rule["QualifyingCondition"](order)
        if Qualify:
            discount = rule["GetDiscount"](order)
        return discount

    def GetOrderwithDiscount(self, Rules, order):
        discount = mean(islice(list(map(partial(self.GetOrderwithDiscountForOneRule, order), Rules)), 3))
        new_order = Order(order.orderdata)
        new_order.discount = discount
        return new_order

    def GetDiscountRules(self):
        DiscountRules = [
            {"QualifyingCondition": self.isAQualified, "GetDiscount": self.A},
            {"QualifyingCondition": self.isBQualified, "GetDiscount": self.B},
            {"QualifyingCondition": self.isCQualified, "GetDiscount": self.C},
        ]
        return DiscountRules

    @property
    def get_discount(self):
        OrderwithDiscount = list(map(partial(self.GetOrderwithDiscount, self.GetDiscountRules()), self.order_list))
        return OrderwithDiscount


Orderlist.append(Order(1))
Orderlist.append(Order(2))
Orderlist.append(Order(2))

t = test(Orderlist)
orders = t.get_discount
print(orders[1].discount)
