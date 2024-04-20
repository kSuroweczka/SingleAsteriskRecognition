import json
import numpy as np

def findSingleAsterisk(resource):
    """
    Returns False if the resource contains a single asterisk, True otherwise.
    
    """
    if None in resource:
        return True
    
    for res in resource:
        count = res.count("*")
        if count == 1:
            return False
        
    return True