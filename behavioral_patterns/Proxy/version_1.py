#!/usr/bin/python3
# Author: Hovhannes Dabaghyan

from abc import ABCMeta, abstractmethod


class NotHavePermissionException(Exception):
    pass


class Client(object):
    ROLES = (
        ("Administrator", 0),
        ("User", 1),
        ("Guest", 2),
    )

    def __init__(self, name, role):
        self._role = dict(self.ROLES)[role]
        self._name = name

    def get_name(self):
        """
        Get name of the client.

        :rtype: str
        :return: Name first letters capitalized.
        """
        return self._name.title()

    def has_permission(self, role):
        """
        Check if client has permission for given role.

        :type role: str
        :param role: Role keyword.

        :rtype: bool
        :return: Does client has permission for role or not.
        """
        return self._role <= dict(self.ROLES)[role]


class Resource(metaclass=ABCMeta):
    """
    Base resource interface.
    """

    @abstractmethod
    def operation(self, client):
        pass


class ConcreteResource(Resource):
    """
    Concrete resource implementation.
    """

    def operation(self, client):
        """
        Some operation on resource.

        :type client: Client
        :param client: Client information.

        :rtype: void
        :return: void
        """
        print(client.get_name() + " performed action...")


class ConcreteResourceProxy(Resource):
    """
    Proxy for resource.
    """

    def operation(self, client):
        """
        Some operation on resource.

        :type client: Client
        :param client: Client information.

        :raises: NotHavePermissionException

        :rtype: void
        :return: void
        """
        if client.has_permission("Administrator"):
            return ConcreteResource().operation(client)
        raise NotHavePermissionException(client.get_name() + " doesn't have permission for this operation.")


def main():
    print("**************************************************")
    print()

    admin = Client("Hovhannes Dabaghyan", "Administrator")
    user = Client("Jack London", "User")

    print("Hovhannes Dabaghyan tries to do some action: ")
    ConcreteResourceProxy().operation(admin)

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    print("Jack London tries to do some action: ")
    ConcreteResourceProxy().operation(user)

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
