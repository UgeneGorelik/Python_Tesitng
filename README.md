




Performace_Test_Example.py:
Example of performance testing 

______________________________________________

test_MathTest.py(pytest):
Examples on Using Pytest Module


to run the tesiting after downloading pytest using pip
run in directory of the  test py files locations

the py of the test should start with "test_"


py.test -v

Usefull command line Params examples:
__________________________

show all parametres:
py.test -v -rxs

run only needed test (test that is its name contains some specific string: 
in our example the string is good

py.test -m good


runn to show fixture:

py.test -v --capture=no

