import datetime
import enum

"""
steps: 
1- configure (creat: order,customer ,select choices)
2-get the invoice path functions
3-get the avilability path functions
4-send them to AdjustCost to calculate the cost on the order
5-happy ending
"""


def calcInvoice1(o):
    invoice = Invoice()
    invoice.cost = o.cost * 1.1
    return invoice


def calcInvoice2(o):
    invoice = Invoice()
    invoice.cost = o.cost * 1.2
    return invoice


def calcInvoice3(o):
    invoice = Invoice()
    invoice.cost = o.cost * 1.3
    return invoice


def calcShipping1(i):
    s = Shipping()
    s.shipperID = 1 if (i.cost > 1000) else 2
    s.cost = i.cost
    return s


def calcShipping2(i):
    s = Shipping()
    s.shipperID = 1 if (i.cost > 1100) else 2
    s.cost = i.cost
    return s


def calcShipping3(i):
    s = Shipping()
    s.shipperID = 1 if (i.cost > 1200) else 2
    s.cost = i.cost
    return s


def calcShipping4(i):
    s = Shipping()
    s.shipperID = 1 if (i.cost > 1300) else 2
    s.cost = i.cost
    return s


def calcShipping5(i):
    s = Shipping()
    s.shipperID = 1 if (i.cost > 1400) else 2
    s.cost = i.cost
    return s


def calcFreightCost1(s):
    f = Freight()
    f.cost = s.cost * 0.25 if (s.shipperID == 1) else s.cost * 0.5
    return f


def calcFreightCost2(s):
    f = Freight()
    f.cost = s.cost * 0.25 if (s.shipperID == 1) else s.cost * 0.52
    return f


def calcFreightCost3(s):
    f = Freight()
    f.cost = s.cost * 0.28 if (s.shipperID == 1) else s.cost * 0.53
    return f


def calcAvailability1(o):
    a = Availability()
    a.date = o.date.replace(day=o.date.day + 3)
    return a


def calcAvailability2(o):
    a = Availability()
    a.date = o.date.replace(day=o.date.day + 2)
    return a


def calcShippingDate1(a):
    s = ShippingDate()
    s.date = a.date.replace(day=a.date.day + 1)
    return s


def calcShippingDate2(a):
    s = ShippingDate()
    s.date = a.date.replace(hour=a.date.hour + 21)
    return s


def calcShippingDate3(a):
    s = ShippingDate()
    s.date = a.date.replace(day=a.date.day + 2)
    return s


def calcShippingDate4(a):
    s = ShippingDate()
    s.date = a.date.replace(day=a.date.day + 4)
    return s


class ProcessConfiguration:
    def __init__(self):
        self.invoiceChoice = InvoiceChoice
        self.shippingChoice = ShippingChoice
        self.freightChoice = FreightChoice
        self.availabilityChoice = AvailabilityChoice
        self.shippingDateChoice = ShippingDateChoice


class InvoiceChoice(enum.Enum):
    Inv1 = 0
    Inv2 = 1
    Inv3 = 2


class ShippingChoice(enum.Enum):
    Sh1 = 0
    Sh2 = 1
    Sh3 = 2
    Sh4 = 3
    Sh5 = 5


class FreightChoice(enum.Enum):
    fr1 = 0
    fr2 = 1
    fr3 = 2


class ShippingDateChoice(enum.Enum):
    SD1 = 0
    SD2 = 1
    SD3 = 2
    SD4 = 3


class AvailabilityChoice(enum.Enum):
    AV1 = 0
    AV2 = 1


class Order:
    def __init__(self):
        self.date = datetime
        self.cost = 0
        self.customer = None


class Customer:
    pass


class Invoice:
    def __init__(self):
        self.cost = 0


class Shipping:
    def __init__(self):
        self.cost = 0
        self.shipperID = 0


class Availability:
    def __init__(self):
        self.date = datetime


class ShippingDate:
    def __init__(self):
        self.date = datetime


class Freight:
    def __init__(self):
        self.cost = 0


class InvoicingPath:
    def __init__(self):
        self.InvoiceFunctions = [
            (InvoiceChoice.Inv1, calcInvoice1),
            (InvoiceChoice.Inv2, calcInvoice2),
            (InvoiceChoice.Inv3, calcInvoice3),
        ]
        self.ShippingFunctions = [
            (ShippingChoice.Sh1, calcShipping1),
            (ShippingChoice.Sh2, calcShipping2),
            (ShippingChoice.Sh3, calcShipping3),
            (ShippingChoice.Sh4, calcShipping4),
            (ShippingChoice.Sh5, calcShipping5),
        ]
        self.frieghtFunctions = [
            (FreightChoice.fr1, calcFreightCost1),
            (FreightChoice.fr2, calcFreightCost2),
            (FreightChoice.fr3, calcFreightCost3),
        ]


class AvailabilityPath:
    def __init__(self):
        self.AvailabilityFunctions = [
            (AvailabilityChoice.AV1, calcAvailability1),
            (AvailabilityChoice.AV2, calcAvailability2),
        ]
        self.ShippingDateFunctions = [
            (ShippingDateChoice.SD1, calcShippingDate1),
            (ShippingDateChoice.SD2, calcShippingDate2),
            (ShippingDateChoice.SD3, calcShippingDate3),
            (ShippingDateChoice.SD4, calcShippingDate4),
        ]


order = Order()


def setConfiguration():
    processConfiguration = ProcessConfiguration()
    customer = Customer()
    processConfiguration.invoiceChoice = InvoiceChoice.Inv3
    processConfiguration.shippingChoice = ShippingChoice.Sh2
    processConfiguration.freightChoice = FreightChoice.fr3
    processConfiguration.availabilityChoice = AvailabilityChoice.AV2
    processConfiguration.shippingDateChoice = ShippingDateChoice.SD4
    order.customer = customer
    order.date = datetime.datetime(2021, 3, 16)
    order.cost = 2000
    return (order, processConfiguration)


def InvoicePathFunc(conf, ip):
    inv = list(filter(lambda x: x[0] == conf[1].invoiceChoice, ip.InvoiceFunctions))[0][1]
    ship = list(filter(lambda x: x[0] == conf[1].shippingChoice, ip.ShippingFunctions))[0][1]
    frei = list(filter(lambda x: x[0] == conf[1].freightChoice, ip.frieghtFunctions))[0][1]
    p = lambda o: frei(ship(inv(o)))
    return p


def AvailabilityPathFunc(conf, ap):
    av = list(filter(lambda x: x[0] == conf[1].availabilityChoice, ap.AvailabilityFunctions))[0][1]
    shd = list(filter(lambda x: x[0] == conf[1].shippingDateChoice, ap.ShippingDateFunctions))[0][1]
    p = lambda o: shd(av(o))
    return p


def CalcAdjustedCostofOrder(conf, InvoicingPath, AvailabilityPath):
    return lambda x: AdjustCost(x, InvoicePathFunc(conf, InvoicingPath), AvailabilityPathFunc(conf, AvailabilityPath))


def AdjustCost(r, calcFreigt, calcShippingDate):
    f = calcFreigt(r)
    s = calcShippingDate(r)
    cost = f.cost + 1000 if (s.date.day == "Monday") else f.cost + 500
    return cost


invoicepath = InvoicingPath()
availabilitypath = AvailabilityPath()
configrations = setConfiguration()
CostOfOrder = CalcAdjustedCostofOrder(configrations, invoicepath, availabilitypath)
print(CostOfOrder(order))
