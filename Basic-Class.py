class MyClass:
    def __init__(self, value):
        # self refers to the instance of the class
        # constuctor \/\/\/\/
        self.value = value

    def show_value(self):
        # Accessing instance variables using self
        print(f"The value is: {self.value}")

# Create an instance
my_instance = MyClass(10)
# Call the method
my_instance.show_value()
