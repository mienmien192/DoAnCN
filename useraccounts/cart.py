from django.conf import settings
from .models import *

class Cart(object):
    def remove(self, courses):
        """
        Remove a product from the cart.
        """
        coursesId = str(courses.id)
        if coursesId in self.cart:
            del self.cart[coursesId]
            self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True