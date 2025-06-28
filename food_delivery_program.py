import time
order_list=['Panipuri','Bhel puri','samosa']
def display():
    print('Available')
    for x in order_list:
        print(x)
        time.sleep(1)
class delivery_boy():
    display()
def ordering(self):
    order_req=input('Enter the food name: ')
    return order_req
b=delivery_boy()
delivery_collector= b.ordering()
print(delivery_collector)
class admin():
    def accepting_order(self,food):
        if food in order_list:
            print(food,'Avaliable')
        else:
            print(food,'Not Available')
a=admin()
a.accepting_order(delivery_collector)