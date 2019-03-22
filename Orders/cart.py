class Cart():
    '''Class for shopping Cart'''
    items={}
    totalQuantity=0
    totalPrice=0

    def copyFromOldCart(self,  oldCart):
        self.items=oldCart.items
        self.totalPrice=oldCart.totalPrice
        self.totalQuantity=oldCart.totalQuantity

    def addProduct(self, item, id):
        storeItem={'quantity': 0, 'price': item.price, 'name': item.name, 'item': item}
        if self.items.get(id)!=None :
            storeItem=self.items[id]
            
        storeItem['quantity']=storeItem['quantity']+1
        storeItem['price']=item.price*storeItem['quantity']
        self.items[id]=storeItem
        self.totalQuantity=self.totalQuantity+1
        self.totalPrice=self.totalPrice+item.price