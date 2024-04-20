def findSingleAsterisk(resource):
    """
    Returns True if the resource contains a single asterisk, False otherwise.
    
    """
    if None in resource:
        return True
    for res in resource:
        count = res.count("*")
        if count != 1:
            return True
    return False