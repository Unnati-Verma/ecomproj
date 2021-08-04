class Basket():
    """
    A base Basket class, providing some default behaviors that can be inherited or overridden, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product):
        """
        Adding and updating the users basket session data
        """
        product_id = product.id

        if product_id not in self.basket:  # if the product exist in the basket
            self.basket[product_id] = {'price': str(product.price)}  # add new data in the basket

            # save this session
            self.session.modified = True  # we have modified the session
