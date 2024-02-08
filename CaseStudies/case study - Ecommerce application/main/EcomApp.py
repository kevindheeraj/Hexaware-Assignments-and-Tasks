# app/EcomApp.py
from assignments.ecommer.dao.order_processor_repository_impl import OrderProcessorRepositoryImpl
from assignments.ecommer.entity.product import Product
from assignments.ecommer.entity.customer import Customer


class EcomApp:
    @staticmethod
    def main():
        order_processor_repository = OrderProcessorRepositoryImpl()

        while True:
            print("\nE-commerce Application Menu:")
            print("1. Register Customer.")
            print("2. Create Product.")
            print("3. Delete Product.")
            print("4. Add to cart.")
            print("5. View cart.")
            print("6. Place order.")
            print("7. View Customer Order.")
            print("8. Exit.")

            choice = input("Enter your choice: ")

            if choice == '1':
                # Register Customer
                order_processor_repository.create_customer()

            elif choice == '2':
                # Create Product
                order_processor_repository.create_product()

            elif choice == '3':
                # Delete Product
                product_id = int(input("Enter product ID to delete: "))
                order_processor_repository.delete_product(product_id)

            elif choice == '4':
                order_processor_repository.add_to_cart()

            elif choice == '5':
                order_processor_repository.get_all_from_cart()

            elif choice == '6':

                order_processor_repository.place_order()

            elif choice == '7':
                order_processor_repository.get_orders_by_customer()

            elif choice == '8':
                print("Exiting E-commerce Application.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    EcomApp.main()
