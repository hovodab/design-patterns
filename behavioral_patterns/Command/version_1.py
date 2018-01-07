#!/usr/bin/python3
# Author: Hovhannes Dabaghyan

from abc import ABCMeta, abstractmethod


class Request(object):
    """
    Represents request from the client.
    """

    def __init__(self, destination, token):
        # Handler could be an object of a custom class which str representation will give complete response.
        # But to keep it simple will use just a standard text.
        self.handler = "404 Not Found"
        self.destination = destination
        self.token = token


class Server(object):
    """
    Server which can handle requests.
    """

    def __init__(self, middlewares):
        self._middlewares = middlewares

    def handle_request(self, request):
        """
        Receives requests and guess what it does...

        :type request: Request
        :param request: Request object.

        :rtype: str
        :return: Response of the processed request.
        """
        for middleware in self._middlewares:
            request = middleware().process_request(request)
        return str(request.handler)


class Middleware(object, metaclass=ABCMeta):

    @abstractmethod
    def process_request(self, request):
        """
        Process request.

        :type request: Request
        :param request: Request object.

        :rtype: Request
        :return: Request after processing.
        """
        raise NotImplementedError()


class CSRFMiddleware(Middleware):
    """
    Check CSRF token to be present and be valid in the request object.
    """

    def process_request(self, request):
        """
        Process request.

        :type request: Request
        :param request: Request object.

        :rtype: Request
        :return: Request after processing.
        """
        # Check if CSRF exists in the body. Token should be specific in some time, and should be updated,
        # but for simplicity will use constant value.
        if request.token != '10101010':
            raise Exception("Invalid CSRF token.")
        return request


class RouterMiddleware(Middleware):
    """
    Route request to the destination handler.
    """

    def process_request(self, request):
        """
        Process request.

        :type request: Request
        :param request: Request object.

        :rtype: Request
        :return: Request after processing.
        """
        # Send request to the appropriate view.
        if request.destination == "Users":
            request.handler = "UsersHandler"
        elif request.handler == "Cars":
            request.handler = "CarsHandler"

        return request


def main():
    print("**************************************************")
    print()

    server = Server([CSRFMiddleware])
    print("Handling request for `Users` with CSRF middleware only: ",
          server.handle_request(Request("Users", "10101010")))
    print()
    server = Server([CSRFMiddleware, RouterMiddleware])
    print("Handling request for `Users` with CSRF and Router middlewares: ",
          server.handle_request(Request("Users", "10101010")))

    print("Both middlewares and wrong token: ",
          server.handle_request(Request("Users", "andromeda")))
    # server = Server([CSRFMiddleware, RouterMiddleware])

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
