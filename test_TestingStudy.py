#Testing with Pytest Examples

#importing Lib
import pytest

#import Mock library
from mock import Mock

#to mimic the result of some function to save time for example
someFunction=Mock(return_value=1)



#create a fixture (if for example we have attribute that we want to initialize once
#it can be done as  the fixture here we initializing   for_passing_to
#it could be also costly connect to mysql connector we need to use in several functions
#this replaces setup and teardown script

@pytest.fixture()
def fixtureexample():
    print("running fixture")
    for_passing_to=2
    return  for_passing_to

#mark test to have sort of hashtag "good" so if we want to run test wtih this hashtag:
#py.test -m good
@pytest.mark.good
def sum(x,y):
    return x+y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x//y


def test_sum():
    total=sum(1,2)
    assert total==3

SkipVAl=0

#if we want to run if some condition
@pytest.mark.skipif(SkipVAl==1,reason="do not want MAN")
def test_divide():
    total=divide(1,1)
    assert total==1

#if we just want to skip
@pytest.mark.skip(reason="do not want MAN")
def test_multiply():
    total=multiply(1,2)
    assert total==2

#the function that recieves the attribute from the init function
def test_multiply_withfixture(fixtureexample):
    total=multiply(1,2)
    assert total==fixtureexample

#test the function that mock have mimiced
def test_mocking():
       assert someFunction(1)==1