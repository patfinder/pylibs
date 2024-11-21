"""
This module attempt to extend standard inspect lib.
"""

def dir2(obj):
    """
    Return list of non-system properties and methods.
    """
    if obj is None:
        return None
    
    members = dir(obj)
    return [m for m in members if not m.startswith('__')]
