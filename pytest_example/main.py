from pytest_example.hello_world import HelloWorld
from pytest_example.hello_world_impl import HelloWorldImpl


hello:HelloWorld = HelloWorldImpl()

print(hello.getString())
