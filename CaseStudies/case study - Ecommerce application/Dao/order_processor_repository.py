# dao/order_processor_repository.py

from abc import ABC, abstractmethod
from assignments.ecommer.entity.customer import Customer
from assignments.ecommer.entity.product import Product

class OrderProcessorRepository(ABC):
    @abstractmethod
    def create_product(self) -> bool:
        pass

    @abstractmethod
    def create_customer(self) -> bool:
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> bool:
        pass

    @abstractmethod
    def delete_customer(self, customer_id: int) -> bool:
        pass

    @abstractmethod
    def add_to_cart(self, customer: Customer, product: Product, quantity: int) -> bool:
        pass

    @abstractmethod
    def remove_from_cart(self, customer: Customer, product: Product) -> bool:
        pass

    @abstractmethod
    def get_all_from_cart(self, customer: Customer) -> list:
        pass

    @abstractmethod
    def place_order(self, customer: Customer, order_details: list, shipping_address: str) -> bool:
        pass

    @abstractmethod
    def get_orders_by_customer(self, customer_id: int) -> list:
        pass
