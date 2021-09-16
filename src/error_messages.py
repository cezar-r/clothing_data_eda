#!/usr/bin/env python
# coding: utf-8

'''
This file is used to throw custom errors through the ArgumentError object
'''

class ArgumentError(Exception):
    def __init__(self, message):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)