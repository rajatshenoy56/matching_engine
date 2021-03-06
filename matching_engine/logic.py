from matching_engine import app, db
from matching_engine.models import Stock, Trade
#  stop and stop limit order test case:
'''
order1 = Stock(order_id=1, stock_code="AMZ", trade_type="Bid", price=50, quantity=10, order_type='market',flavor = 'partial',username="Neha")
order2 = Stock(order_id=2, stock_code="AMZ", trade_type="Bid", price=45, quantity=15, order_type='limit',flavor = 'partial',username="A")
order3 = Stock(order_id=3, stock_code="AMZ", trade_type="Ask", price=47, quantity=15, order_type='market',flavor = 'allornone',username="B")
'''
#order4 = Stock(order_id=4, stock_code="AMZ", trade_type="Ask", quantity=5, order_type='stop',flavor = 'allornone',username="D",trigger_price =44)
#order5 = Stock(order_id=5, stock_code="AMZ", trade_type="Ask", price =43, quantity=5, order_type='stoplimit',flavor = 'allornone',username="e",trigger_price =42)

# order1 = Stock(order_id=1, stock_code="AMZ", trade_type="Bid", price=45, quantity=10, order_type='market',flavor = 'allornone',username="A")
# order2 = Stock(order_id=2, stock_code="AMZ", trade_type="Ask", price=46, quantity=5, order_type='market',flavor = 'allornone',username="B")
# order3 = Stock(order_id=3, stock_code="AMZ", trade_type="Ask", price=47, quantity=10, order_type='market',flavor = 'allornone',username="C")
# order4 = Stock(order_id=4, stock_code="AMZ", trade_type="Ask", price=48, quantity=5, order_type='market',flavor = 'allornone',username="D")
# order5 = Stock(order_id=5, stock_code="AM", trade_type="Ask", price=48, quantity=5, order_type='market',flavor = 'allornone',username="E")
# order6 = Stock(order_id=6, stock_code="AM", trade_type="Bid", price=48, quantity=5, order_type='market',flavor = 'allornone',username="F")
# order7 = Stock(order_id=7, stock_code="AM", trade_type="Bid", price=46, quantity=5, order_type='market',flavor = 'allornone',username="G")
# order8 = Stock(order_id=8, stock_code="AMZ", trade_type="Bid", price=45, quantity=5, order_type='market',flavor = 'partial',username="H")
# order9 = Stock(order_id=9, stock_code="AMZ", trade_type="Ask", price=46, quantity=5, order_type='market',flavor = 'partial',username="I")
# order10 = Stock(order_id=10, stock_code="AMZ", trade_type="Bid", price=47, quantity=10, order_type='market',flavor = 'partial',username="J")
# order11 = Stock(order_id=11, stock_code="AMZ", trade_type="Ask", price=48, quantity=5, order_type='market',flavor = 'partial',username="K")
# order12 = Stock(order_id=12, stock_code="AM", trade_type="Bid", price=48, quantity=5, order_type='market',flavor = 'partial',username="L")
# order13 = Stock(order_id=13, stock_code="AM", trade_type="Ask", price=48, quantity=5, order_type='market',flavor = 'partial',username="M")
# order14 = Stock(order_id=14, stock_code="AM", trade_type="Bid", price=46, quantity=5, order_type='market',flavor = 'partial',username="N")


# order1 = Stock(order_id=1, stock_code="AMZ", trade_type="Bid", price=46, quantity=5, order_type='limit',flavor = 'allornone',username="A")
# order2 = Stock(order_id=2, stock_code="AMZ", trade_type="Ask", price=46, quantity=5, order_type='limit',flavor = 'allornone',username="B")
# order3 = Stock(order_id=3, stock_code="AMZ", trade_type="Ask", price=47, quantity=10, order_type='limit',flavor = 'allornone',username="C")
# order4 = Stock(order_id=4, stock_code="AMZ", trade_type="Ask", price=48, quantity=5, order_type='limit',flavor = 'allornone',username="D")
# order5 = Stock(order_id=5, stock_code="AM", trade_type="Ask", price=48, quantity=5, order_type='limit',flavor = 'allornone',username="E")
# order6 = Stock(order_id=6, stock_code="AM", trade_type="Bid", price=48, quantity=5, order_type='limit',flavor = 'allornone',username="F")
# order7 = Stock(order_id=7, stock_code="AM", trade_type="Bid", price=46, quantity=5, order_type='limit',flavor = 'allornone',username="G")
# order8 = Stock(order_id=8, stock_code="AMZ", trade_type="Bid", price=45, quantity=5, order_type='limit',flavor = 'partial',username="H")
# order9 = Stock(order_id=9, stock_code="AMZ", trade_type="Ask", price=46, quantity=5, order_type='limit',flavor = 'partial',username="I")
# order10 = Stock(order_id=10, stock_code="AMZ", trade_type="Bid", price=47, quantity=10, order_type='limit',flavor = 'partial',username="J")
# order11 = Stock(order_id=11, stock_code="AMZ", trade_type="Ask", price=46, quantity=5, order_type='limit',flavor = 'partial',username="K")
# order12 = Stock(order_id=12, stock_code="AM", trade_type="Bid", price=48, quantity=5, order_type='limit',flavor = 'partial',username="L")
# order13 = Stock(order_id=13, stock_code="AM", trade_type="Ask", price=48, quantity=5, order_type='limit',flavor = 'partial',username="M")
# order14 = Stock(order_id=14, stock_code="AM", trade_type="Bid", price=46, quantity=5, order_type='limit',flavor = 'partial',username="N")

'''
# limit order test case
order8 = Stock(order_id=8, stock_code="AMZ", trade_type="Bid",
                price=45, quantity=5, order_type='limit', flavor='allornone')
order9 = Stock(order_id=9, stock_code="AMZ", trade_type="Ask",
                price=46, quantity=5, order_type='limit', flavor='allornone')
order10 = Stock(order_id=10, stock_code="AMZ", trade_type="Bid",
                 price=47, quantity=5, order_type='limit', flavor='allornone')
order11 = Stock(order_id=11, stock_code="AMZ", trade_type="Ask",
                 price=48, quantity=5, order_type='limit', flavor='allornone')
order12 = Stock(order_id=12, stock_code="AM", trade_type="Bid",
                 price=48, quantity=5, order_type='limit', flavor='allornone')
order13 = Stock(order_id=13, stock_code="AM", trade_type="Ask",
                 price=48, quantity=5, order_type='limit', flavor='allornone')
order14 = Stock(order_id=14, stock_code="AM", trade_type="Bid",
                 price=46, quantity=5, order_type='limit', flavor='allornone')
'''

class Order_Queue(object):

    def __init__(self):
        self.active_list = {}
        self.inactive_list = {}

    # Adding a new order.
    def enqueue(self, order):
        if order.order_type.lower() == "market" or order.order_type.lower() == "limit":
            
            if order.stock_code not in self.active_list.keys():
                self.active_list[order.stock_code] = {'Bid': [], 'Ask': []}
                print('Heellllooo')
            self.active_list[order.stock_code][order.trade_type].append(order)
        else:
            if order.stock_code not in self.inactive_list.keys():
                self.inactive_list[order.stock_code] = []
            self.inactive_list[order.stock_code].append(order)

    #Pass a dict cmp of 5 current market prices of 5 companies
    def activate(self,cmp):
        to_be_activated=[]
        for stock_code,orders in self.inactive_list.items():

            to_be_activated1 = [x for x in orders if x.trigger_price >= cmp[stock_code] and x.trade_type == 'Ask']
            to_be_activated2 = [x for x in orders if x.trigger_price <= cmp[stock_code] and x.trade_type == 'Bid']
            to_be_activated = to_be_activated1+to_be_activated2
            for order in to_be_activated:
                self.inactive_list[stock_code].remove(order)
                if order.order_type == 'stoplimit':#default set for market price
                    order.order_type = "limit"
                else:
                    order.order_type = "market"
                self.enqueue(order)
        return to_be_activated
                

    # Wrapper function for matching orders.
    def match(self, order):

        # Perform the appropriate matching.
        match_list=None
        if order.order_type.lower() == "market":
            match_list = self.match_market(order)
        elif order.order_type.lower() == "limit":
            match_list = self.match_limit(order)
        if match_list is not None:
            for m in match_list:
                if m[0].trade_type=='Bid':
                    buyer=m[0].username
                    seller=m[1].username
                else:
                    buyer=m[1].username
                    seller=m[0].username
                entry=Trade(buyer_name=buyer,seller_name=seller,quantity=m[3],price=m[2],stock_code=m[0].stock_code)
                db.session.add(entry)
            db.session.commit()
        # If the returned list is not null , then the matching was successful and remove this order from the list.
        if match_list is not None and order.flavor == "allornone" :
            if order.order_type != "market":
                self.active_list[order.stock_code][order.trade_type].remove(order)
            return match_list
        elif match_list is not None and order.flavor == "partial":
            return match_list
        # Return an empty list indicating that there were no matches against this order.
        return []

    # Matching only market orders.
    def match_market(self, mo):
        # Get the list of orders we are supposed to match against.

        if mo.trade_type == 'Bid':
            target_order_list = self.active_list[mo.stock_code]['Ask']
            target_order_sorted = list(target_order_list)
            target_order_sorted.sort(key=lambda x: x.price)
        else:
            target_order_list = self.active_list[mo.stock_code]['Bid']
            target_order_sorted = list(target_order_list)
            target_order_sorted.sort(key=lambda x: x.price, reverse=True)
        # Match!
        match_list = []
        # trade_type_new='Bid' if mo.trade_type=='Ask' else 'Ask'
        for o in target_order_sorted:
            if mo.username!=o.username:
                if mo.flavor == "allornone" and o.flavor == "allornone":
                    if mo.quantity == o.quantity :
                        match_list.append([o,mo,o.price,o.quantity])
                        target_order_list.remove(o)
                        # target_order_list=[x for x in target_order_list if x!=o]
                        # self.active_list[mo.stock_code][trade_type_new].remove(o)
                        break
                elif mo.flavor == "partial" and o.flavor == "allornone":
                    if mo.quantity >= o.quantity:
                        match_list.append([o,mo,o.price,o.quantity])
                        mo.quantity = mo.quantity - o.quantity
                        target_order_list.remove(o)
                        # target_order_list=[x for x in target_order_list if x!=o]
                        # self.active_list[mo.stock_code][trade_type_new].remove(o)
                        if mo.quantity == 0:
                            self.active_list[mo.stock_code][mo.trade_type].remove(mo)
                            break
                elif mo.flavor == "allornone" and o.flavor == "partial":
                    if mo.quantity <= o.quantity:
                        match_list.append([o,mo,o.price,mo.quantity])
                        o.quantity = o.quantity - mo.quantity
                        if o.quantity == 0:
                            target_order_list.remove(o)
                            # target_order_list=[x for x in target_order_list if x!=o]
                            # self.active_list[mo.stock_code][trade_type_new].remove(o)
                            #target_order_list=[x for x in target_order_list if x!=o]
                        break
                elif mo.flavor == "partial" and o.flavor == "partial":
                    if mo.quantity <= o.quantity:
                        match_list.append([o,mo,o.price,mo.quantity])
                        o.quantity = o.quantity - mo.quantity
                        if o.quantity == 0:
                            target_order_list.remove(o)
                            # target_order_list=[x for x in target_order_list if x!=o]
                            # self.active_list[mo.stock_code][trade_type_new].remove(o)
                            #target_order_list=[x for x in target_order_list if x!=o]
                        self.active_list[mo.stock_code][mo.trade_type].remove(mo)
                        break
                    else:
                        match_list.append([o,mo,o.price,o.quantity])
                        mo.quantity = mo.quantity - o.quantity
                        target_order_list.remove(o)
                        # target_order_list=[x for x in target_order_list if x!=o]
                        # self.active_list[mo.stock_code][trade_type_new].remove(o)
                        #target_order_list=[x for x in target_order_list if x!=o]

        # Return null on unsuccessful matching
        if mo in self.active_list[mo.stock_code][mo.trade_type]:
            self.active_list[mo.stock_code][mo.trade_type].remove(mo)
        return match_list if len(match_list) > 0 else None

    # Matching only limit orders.
    def match_limit(self, lo):
        # Get the list of orders we are supposed to match against.
        if lo.trade_type == 'Bid':
            target_order_list = self.active_list[lo.stock_code]['Ask']
            target_order_sorted = list(target_order_list)
            target_order_sorted.sort(key=lambda x: x.price)
        else:
            target_order_list = self.active_list[lo.stock_code]['Bid']
            target_order_sorted = list(target_order_list)
            target_order_sorted.sort(key=lambda x: x.price, reverse=True)

        # Match!
        #match_list = []
        '''if lo.trade_type == 'Bid':
            for o in target_order_list:
                if lo.quantity == o.quantity and o.price<=lo.price:
                    match_list.append([o,lo,o.quantity,o.price])
                    target_order_list.remove(o)
                    break
        else:
            for o in target_order_list:
                if lo.quantity == o.quantity and o.price>=lo.price:
                    match_list.append([o,lo,o.quantity,lo.price])
                    target_order_list.remove(o)
                    break
        '''
        # Return null on unsuccessful matching

        # Match!
        #print(target_order_list)
        match_list = []
        # trade_type_new='Bid' if lo.trade_type=='Ask' else 'Ask'
        for o in target_order_sorted:
            if lo.username!=o.username:
                if lo.flavor == "allornone" and o.flavor == "allornone":
                    if lo.quantity == o.quantity and (lo.price>=o.price if lo.trade_type=='Bid' else lo.price<=o.price):
                        # print("LL")
                        price_to_return=lo.price if lo.price<=o.price else o.price
                        match_list.append([o,lo,price_to_return,o.quantity])
                        # target_order_list=[x for x in target_order_list if x!=o]
                        # self.active_list[lo.stock_code][trade_type_new].remove(o)
                        target_order_list.remove(o)
                        #print(self.active_list[lo.stock_code][trade_type_new])
                        # print("list",target_order_list)
                        # print("dic",self.active_list)
                        break

                elif lo.flavor == "partial" and o.flavor == "allornone":
                    if lo.quantity >= o.quantity and (lo.price>=o.price if lo.trade_type=='Bid' else lo.price<=o.price):
                        price_to_return=lo.price if lo.price<=o.price else o.price
                        match_list.append([o,lo,price_to_return,o.quantity])
                        lo.quantity = lo.quantity - o.quantity
                        # target_order_list=[x for x in target_order_list if x!=o]
                        target_order_list.remove(o)
                        # self.active_list[lo.stock_code][trade_type_new].remove(o)
                        if lo.quantity == 0:
                            self.active_list[lo.stock_code][lo.trade_type].remove(lo)
                            break
                        # print("list",target_order_list)
                        # print("dic",self.active_list)
                elif lo.flavor == "allornone" and o.flavor == "partial":
                    if lo.quantity <= o.quantity and (lo.price>=o.price if lo.trade_type=='Bid' else lo.price<=o.price):
                        price_to_return=lo.price if lo.price<=o.price else o.price
                        match_list.append([o,lo,price_to_return,lo.quantity])
                        o.quantity = o.quantity - lo.quantity
                        # print("kill",o.quantity)
                        if o.quantity == 0:
                            target_order_list.remove(o)
                            # target_order_list=[x for x in target_order_list if x!=o]
                            # self.active_list[lo.stock_code][trade_type_new].remove(o)
                        # print("list",target_order_list)
                        # print("dic",self.active_list)
                        break
                elif lo.flavor == "partial" and o.flavor == "partial":
                    if lo.quantity <= o.quantity:
                        if lo.price>=o.price if lo.trade_type=='Bid' else lo.price<=o.price:
                            price_to_return=lo.price if lo.price<=o.price else o.price
                            match_list.append([o,lo,price_to_return,lo.quantity])
                            o.quantity = o.quantity - lo.quantity
                            if o.quantity == 0:
                                target_order_list.remove(o)
                                # target_order_list=[x for x in target_order_list if x!=o]
                                # self.active_list[lo.stock_code][trade_type_new].remove(o)

                            self.active_list[lo.stock_code][lo.trade_type].remove(lo)
                            break
                    else:
                        price_to_return=lo.price if lo.price<=o.price else o.price
                        match_list.append([o,lo,price_to_return,o.quantity])
                        lo.quantity = lo.quantity - o.quantity
                        target_order_list.remove(o)
                        # target_order_list=[x for x in target_order_list if x!=o]
                        # self.active_list[lo.stock_code][trade_type_new].remove(o)
                    # print("list",target_order_list)
                    # print("dic",self.active_list)
        return match_list if len(match_list) > 0 else None


'''
order_queue = Order_Queue()
order_queue.enqueue(order1)
print(order_queue.match(order1))

order_queue.enqueue(order2)
print(order_queue.match(order2))

order_queue.enqueue(order3)
print(order_queue.match(order3))

order_queue.enqueue(order4) # only enqueue stop and stop loss ;dont match them

# print(order_queue.match(order4))

order_queue.enqueue(order5)
order_queue.activate({"AMZ":40})
# print(order_queue.match(order5))

# order_queue.enqueue(order6)
# print(order_queue.match(order6))

# order_queue.enqueue(order7)
# print(order_queue.match(order7))

# order_queue.enqueue(order8)
# print(order_queue.match(order8))

# order_queue.enqueue(order9)
# print(order_queue.match(order9))

# order_queue.enqueue(order10)
# print(order_queue.match(order10))

# order_queue.enqueue(order11)
# print(order_queue.match(order11))

# order_queue.enqueue(order12)
# print(order_queue.match(order12))

# order_queue.enqueue(order13)
# print(order_queue.match(order13))

# order_queue.enqueue(order14)
# print(order_queue.match(order14))
'''