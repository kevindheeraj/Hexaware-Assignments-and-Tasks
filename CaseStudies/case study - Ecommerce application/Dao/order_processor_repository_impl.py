# dao/order_processor_repository_impl.py
from datetime import datetime

from assignments.ecommer.dao.order_processor_repository import OrderProcessorRepository
from assignments.ecommer.entity.customer import Customer
from assignments.ecommer.entity.product import Product
from assignments.ecommer.entity.cart import Cart
from assignments.ecommer.entity.order import Order
from assignments.ecommer.entity.orderitem import OrderItem
from assignments.ecommer.util.DBConnection import get_connection

class OrderProcessorRepositoryImpl(OrderProcessorRepository):
    def create_product(self) -> bool:
        cursor = None
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))
        product_description = input("Enter product description: ")
        stock_quantity = int(input("Enter product stock quantity: "))
        values = (product_name, product_price, product_description, stock_quantity)
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = "INSERT INTO products (name, price, description, stockQuantity) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, values)
            print("product created successfully")
            connection.commit()
            return True
        except Exception as e:
            print(f"Error creating product: {e}")
            return False
        finally:
            if cursor:
                connection.close()

    def create_customer(self) -> bool:
        cursor = None
        customer_name = input("Enter customer name: ")
        customer_email = input("Enter customer email: ")
        customer_password = input("Enter customer password: ")
        values = (customer_name, customer_email, customer_password)

        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = "INSERT INTO customers (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, values)
            print("customer registered successfully")
            connection.commit()
            return True
        except Exception as e:
            print(f"Error creating customer: {e}")
            return False
        finally:
            if cursor:
                connection.close()

    def delete_product(self, product_id: int) -> bool:
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor()
            product_query = "SELECT * FROM products WHERE product_id = %s"
            cursor.execute(product_query, (product_id,))
            existing_product = cursor.fetchone()

            if not existing_product:
                raise Exception(f"Product with ID {product_id} not found")

            query = "DELETE FROM products WHERE product_id = %s"
            cursor.execute(query, (product_id,))
            connection.commit()
            print("Product deleted successfully")
            return True
        except Exception as e:
            print(f"Error deleting product: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

    def delete_customer(self, customer_id: int) -> bool:
        try:
            connection = get_connection()
            cursor = connection.cursor()


            query = "DELETE FROM customers WHERE customer_id = %s"
            cursor.execute(query, (customer_id,))

            connection.commit()
            return True
        except Exception as e:
            print(f"Error deleting customer: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

    def add_to_cart(self) -> bool:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)

        cursor = None
        customer_id = input("Enter customer id: ")
        product_id = int(input("Enter the product ID: "))
        quantity = input("Enter the quantity: ")
        cursor = connection.cursor()
        query = "INSERT INTO cart (customer_id, product_id, quantity) VALUES (%s, %s, %s)"
        values = (customer_id, product_id, quantity)
        try:
            cursor.execute(query, values)
            connection.commit()
            print("product added to cart successfully")
            return True
        except Exception as e:
            print(f"Error adding to cart")
            return False
        finally:
            cursor.close()
            connection.close()

    def remove_from_cart(self, customer: Customer, product: Product) -> bool:
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = "DELETE FROM cart WHERE customer_id = %s AND product_id = %s"
            cursor.execute(query, (customer.customer_id, product.product_id))

            connection.commit()
            return True
        except Exception as e:
            print(f"Error removing from cart: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

    def get_all_from_cart(self) -> list:
        customer_id = int(input("enter the customer ID : "))
        cursor = None
        connection = None
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = "SELECT p.product_id, p.name, p.price, c.quantity FROM cart c JOIN products p ON c.product_id = p.product_id WHERE c.customer_id = %s"
            values = (customer_id,)
            cursor.execute(query, values)
            result = cursor.fetchall()

            cart_items = []
            for row in result:
                print(row)
                product = Cart(row[0], row[1], row[2], row[3])
                cart_items.append(product)


            return cart_items
        except Exception as e:
            print(f"Error getting items from cart: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def place_order(self) -> bool:
        customer_id = int(input("enter customer ID :"))
        shippingAddress = input("enter address: ")
        email = 1
        name = 1
        password = 1
        customer = Customer(customer_id, email, name, password)
        try:
            connection = get_connection()
            cursor = connection.cursor()

            # Get cart items for the customer
            cart_query = "SELECT product_id, quantity FROM cart WHERE customer_id = %s"
            cursor.execute(cart_query, (customer.get_customer_id(),))
            cart_items = cursor.fetchall()

            # Calculate total price
            total_price = 0
            order_details = []

            for item in cart_items:
                product_id, quantity = item
                product_query = "SELECT name, price,description,stockQuantity FROM products WHERE product_id = %s"
                cursor.execute(product_query, (product_id,))
                product_info = cursor.fetchone()

                if product_info:
                    product_name, product_price, product_description, product_stock_quantity = product_info
                    total_price = total_price + product_price * quantity

                    product = Product(product_id, product_name, product_price, product_description, 0)
                    order_details.append({'product':product, 'quantity': quantity})

            # Insert into orders table
            order_query = "INSERT INTO orders (customer_id, order_date, total_price, shipping_address) VALUES (%s, %s, %s, %s)"
            values_order = (customer.get_customer_id(), datetime.now(), total_price, shippingAddress)
            cursor.execute(order_query, values_order)
            order_id = cursor.lastrowid

            # Insert into order_items table
            order_item_query = "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)"

            for order_detail in order_details:
                product = order_detail['product']
                quantity = order_detail['quantity']
                p_query = ""
                cursor.execute(order_item_query, (order_id, product.get_product_id(), quantity))

            # Clear the customer's cart after placing the order
            clear_cart_query = "DELETE FROM cart WHERE customer_id = %s"
            cursor.execute(clear_cart_query, (customer.get_customer_id(),))

            # Commit transaction
            connection.commit()
            print("Order placed successfully")
            return True

        except Exception as e:
            print(f"Error placing order: {e}")
            # Rollback transaction on error
            connection.rollback()
            return False

        finally:
            cursor.close()
            connection.close()
    def get_orders_by_customer(self) -> list:
        cursor = None
        connection = None
        customer_id = input("enter customer ID : ")
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = "SELECT o.order_id, o.order_date, o.total_price, oi.product_id, p.name, oi.quantity " \
                    "FROM orders o " \
                    "JOIN order_items oi ON o.order_id = oi.order_id " \
                    "JOIN products p ON oi.product_id = p.product_id " \
                    "WHERE o.customer_id = %s"
            cursor.execute(query, (customer_id,))
            result = cursor.fetchall()

            orders = []
            for row in result:
                print(row)
                order_id, order_date, total_price, product_id, product_name, quantity = row
                product = Product(product_id, product_name, 0.0, 0, 0)
                order_item = OrderItem(product_name, product_id, quantity, quantity)
                orders.append((order_id, order_date, total_price, order_item))

            return orders
        except Exception as e:
            print(f"Error getting orders by customer: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
