import unittest
from unittest.mock import patch
from assignments.ecommer.dao.order_processor_repository_impl import OrderProcessorRepositoryImpl
from assignments.ecommer.entity.customer import Customer
from assignments.ecommer.entity.product import Product

class TestOrderProcessorRepositoryImpl(unittest.TestCase):

    @patch('builtins.input', side_effect=['19', '33', '2'])
    def test_add_to_cart_success(self, mock_input):
        order_processor_repository = OrderProcessorRepositoryImpl()
        # Add the product to the cart
        result = order_processor_repository.add_to_cart()
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['19', '123 Main St, City'])
    def test_place_order_success(self, mock_input):
        order_processor_repository = OrderProcessorRepositoryImpl()
        result = order_processor_repository.place_order()
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['bars', '555.50', 'Heavy steel', '10'])
    def test_create_product_success(self, mock_input):
        order_processor_repository = OrderProcessorRepositoryImpl()
        result = order_processor_repository.create_product()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
