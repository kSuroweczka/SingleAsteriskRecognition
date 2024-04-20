from findSingleAsterisk import findSingleAsterisk
from uploadData import upload_data

### ------------------------------------------------------------------------ ###

resources_list = upload_data('testExamples.json')

### ------------------------------------------------------------------------ ###

def test_SingleAsterisk():
    _, resource = resources_list[0]
    assert findSingleAsterisk(resource) == True

def test_DoubleAsterisk():
    _, resource = resources_list[1]
    assert findSingleAsterisk(resource) == True

def test_SingleAsteriskWithResource():
    _, resource = resources_list[2]
    assert findSingleAsterisk(resource) == True

def test_DoubleAsteriskWithResource():
    _, resource = resources_list[3]
    assert findSingleAsterisk(resource) == True

def test_EmptyResource():
    _, resource = resources_list[4]
    assert findSingleAsterisk(resource) == True

def test_EmptyPolicyDocument():
    _, resource = resources_list[5]
    assert findSingleAsterisk(resource) == True

def test_InvalidJson():
    _, resource = resources_list[6]
    assert findSingleAsterisk(resource) == True

def test_NoResource():
    _, resource = resources_list[7]
    assert findSingleAsterisk(resource) == True

def test_SingleAsteriskINTwoOfTwoStatements():
    _, resource = resources_list[8]
    assert findSingleAsterisk(resource) == True

def test_SingleAsteriskINOneOfTwoStatements():
    _, resource = resources_list[9]
    assert findSingleAsterisk(resource) == True