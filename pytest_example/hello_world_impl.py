from pytest_example.hello_world import HelloWorld


class HelloWorldImpl(HelloWorld):
    hello_string = "Hello World"

    def getString(self) -> str:
        return self.hello_string
