#!/usr/bin/env python
# coding: utf-8

'''
This file is used to throw custom errors
'''

class ArgumentError(Exception):
    """This error is raised when invalid arguments are passed in"""
    def __init__(self, message):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
