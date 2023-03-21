#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    
    """ prevent the user to create new instance attributes 
    except if the new instance attributes is 'first_name'.
    """

    __slots__ = ["first_name"]
