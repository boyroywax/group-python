from universal_object import UniversalObject


def main():
    """
    Main function
    """
    print('Initializing Tests')


class UniversalObjectTests():
    """
    A class that represents a universal object test suite
    """

    def __init__(self):
        """
        Initializes the test suite
        """
        print('Initializing Universal Object Tests')

    def create_obj(self) -> UniversalObject:
        """
        Tests the creation of a new object
        """

        # Create a new object
        return UniversalObject(
            name='test',
            description='test',
            nonce=[0],
            owner=["test"],
            creds=["test"],
            data={
                    'title': 'Test Group',
                    'link': '0x0',
                    'schema': '{"test_string": "string", "test_int": "int", '
                    '"test_bool": "bool", "test_list": "list"}',
            }
        )

    def test_obj_validity(self, obj: UniversalObject):
        """
        Tests the validity of the object
        """
        # Check if the object is valid
        if obj.is_valid() is True:
            print('Object is valid - PASSED')

        # Print the object
        print(obj)

        # Print the object's JSON representation
        print(obj.__json__())

        # Print the object's string representation
        print(str(obj))

        # Print the object's representation
        print(repr(obj))

        # Print the object's hash
        print(hash(obj))

    def test_obj_data(self, obj: UniversalObject):
        """
        Tests the object's data
        """
        # Check if the object contains data
        if obj.contains_data() is True:
            print('Object contains data - PASSED')

            # Get the object's data value
            print(obj.get_data())

            # Reset the object's data
            obj.set_data({
                'title': 'Test Group',
                'link': '0x0',
                'schema': '{"test_string": "string", "test_int": "int", '
                        '"test_bool": "bool", "test_list": "list"}',
            })

            # verify that the object's data was reset
            if obj.contains_data() is True:
                print('Object contains data - PASSED')

                # Get the object's data value
                print(obj.get_data())

            # Check if the object's data contains a schema
            if obj.data_contains_schema() is True:
                print('Object contains schema - PASSED')

                # Get the object's schema
                print(obj.get_schema())


if __name__ == '__main__':
    main()

    # Universal Object Tests
    test_suite = UniversalObjectTests()
    test_obj = test_suite.create_obj()
    test_suite.test_obj_validity(test_suite.create_obj())
    test_suite.test_obj_data(test_suite.create_obj())
