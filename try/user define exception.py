class InvalidAgeException(Exception):
    def __init__(self,age,message="Age must be a non-negative integer"):
        self.age=age
        super().__init__(message)

def process_data(age):
        if not isinstance(age,int):
            raise InvalidAgeException(age,"Age must be an integer.")
        if age<0:
            raise InvalidAgeException(age)

        print(age)


try:
    process_data(30)
    process_data(-5)
    process_data("twenty")
except InvalidAgeException as e:
    print(f"Error: {e} (Provided age: {e.age})")

    
