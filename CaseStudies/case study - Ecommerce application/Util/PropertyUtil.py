# util/PropertyUtil.py

class PropertyUtil:
    @staticmethod
    def get_property_string():
        # Read your property file to get connection details
        # For simplicity, you can hardcode the values here
        # Replace these values with your actual database connection details
        connection_string = (
            'localhost',
            'ecom',
            'root',
            'Kevink25*',
            '3306'
        )
        return connection_string
