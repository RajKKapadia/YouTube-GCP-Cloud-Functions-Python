import functions_framework
import flask

@functions_framework.http
def hello(request: flask.Request) -> flask.typing.ResponseReturnValue:
    return 'Hello, World!'
