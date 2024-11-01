class CallableDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Decorator action before the function is called.")
        result = self.func(*args, **kwargs)
        print("Decorator action after the function is called.")
        return 

@CallableDecorator
def my_function():
    print("Function is called.")

print(my_function())