from pytest_example.hello_world_impl import HelloWorldImpl


def test_hello_world_impl():
    assert HelloWorldImpl().getString() == "Hello World"
