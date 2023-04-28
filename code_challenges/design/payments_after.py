"""
SOLID

S: Single Responsability:
Classes and methods with single responsability.
We want high cohesion between the code contained
in a class, method, or function.

In this example: We split the Order class into two
classes: Order and Payment Processor. Then, we split
the pay method into pay_debit and pay_credit methods.

O: Open/Closed: Open to extension, closed to modification.
This means that when we extend the software, we should
increase the amount of methods or classes and not modifiy
the existing code.

In this example: We refactor the PaymentProcessor by
transforming it into an abstract class. If we want to
support new types of payments, we should implement this
abstract class.

L: Liskov Substitution: If we have a parent class "P" and
a subclass "S" of "P", and we develope software features
using the "S" interface, then, we can substitute the "S"
objects with "P" objects of any type without modifying
the coupling.

In this example: We should apply the same interface to
the different process payments. We will use the same
inputs for DebitPaymentProcessor, CreditPaymentProcessor,
and PaypalPaymentProcessor.

I: Interface-segregation: It is better to have several
specific interfaces instead of a general one.

D: Dependency Inversion
"""

from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):
    """Open/Close principle"""

    def __init__(self, security_code):
        """Liskon substitution principle"""
        self.security_code = security_code

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print("Processing Paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    processor = PaypalPaymentProcessor("email@email.com")
    print(order.total_price())
    processor.pay(order)


if __name__ == "__main__":
    main()
