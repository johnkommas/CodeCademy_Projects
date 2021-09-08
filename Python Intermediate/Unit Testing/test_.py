"""
Sam's Surf Shop

Welcome to Sam’s Surf Shop! This project will exercise your knowledge of errors and unit testing practices in Python.
It will also give you a small taste of testing a full application.

You’ve been hired to create a handful of tests for the shopping cart software at the surf shop.
Once that is done, you’ll implement some improvements for these tests using more advanced unit testing features
(skipping, parameterization, and expected failures).
Finally, you’ll have the opportunity to fix bugs that were exposed by your tests.

The shopping cart software for Sam’s Surf Shop lives inside of the file called surfshop.py.
Look over the files and familiarize yourself with their contents. Most of our work will take place in test_.py.

Let’s get started!

1.
Let’s get some basic setup out of the way.
First, import both the surfshop and unittest modules in test_.py.

2.
Next, create a class which will contain all of your tests.
The class can be named whatever you’d like, but it should inherit from unittest.TestCase.

3.
The features you need to test have been implemented in the surfshop.ShoppingCart class.
In order to test the inner workings of a class, you will need to create a new instance of the shopping cart.
Don’t worry - you will handle that in the next tasks!
For now, it’s important that every test has a new ShoppingCart object to work with so that way the test always
starts on a clean slate.

In your class, create a setup fixture that runs before every test.
It should instantiate a new ShoppingCart object and assign it to an instance variable called self.cart.
Your tests can then use self.cart to reference your instance of the ShoppingCart class.

4.

It’s time to create your first test! Let’s test the add_surfboards() method of the cart.

The ShoppingCart.add_surfboards() method takes an integer as its only argument and updates the number of surfboards in the cart.
Define a test method that calls this function with an argument of 1 and checks that 'Successfully added 1 surfboard to cart!' is returned.

5.
Let’s test another input for the .add_surfboardsmethod.
Create another test method which calls ShoppingCart.add_surfboards(), but this time, passes an argument of 2.
It should test that the return value is 'Successfully added 2 surfboards to cart!'

6.
The shopping cart has a limit of 4 surfboards per customer.
Create a test to check that a surfshop.TooManyBoardsError (a custom exception) is raised when
ShoppingCart.add_surfboards() is called with an argument of 5.
"""

import surfshop
import unittest


class SurfShopTests(unittest.TestCase):

    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboards(self):
        message = self.cart.add_surfboards(1)
        self.assertEqual(message, 'Successfully added 1 surfboard to cart!')

    # def test_add_two_surfboards(self):
    #     n = self.cart.add_surfboards(2)
    #     self.assertEqual(n, 'Successfully added 2 surfboards to cart!')

    def test_TooManyBoardsError(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)


if __name__ == '__main__':
    unittest.main()
