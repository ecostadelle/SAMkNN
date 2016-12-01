# SAMkNN

#Installing nearest Neighbor library:
Before using SAM you have to install a C++ library for the nearest neighbor calculations.
*Edit nearesNeighbor/setup.py and make sure that the variable "include_dirs" containts the path to your local python2.7 folder as well as the numpy folder.
*Install the C++ library by using the common setup.py script e.g. "python setup.py install --user".

*a
*b
*b

#Using SAM
Afterwards, you can use SAM. A test script can be found in SAMKNN/testSAMKNN.py. Simply execute "python testSAMKNN.py".
Two exemplary datasets "weather" and "moving squares" can be found in the datasets folder.
