# Programs-for-practice

## Tricky Lists

> A function checkList(inList) that takes in a list that contains already filled values, similar to the ones given below.
You need to write a function whether the list contains, numbers in a sequence or not, if the sequence is not followed it should return the inner list that does not follow the sequence or
It should return True.

The sequence could be either odd or even numbers as shown below.

Note: only one level of depth is expected to be handled.
Sample inputs which are correctly filled are given below:

```sh
Input1: [[0], [2, 4]]
Input2: [[1], [3, 5], [7, 9, 11]]
Input3: [[1], [3, 5], [7, 9, 11], [13, 15, 17, 19], [21, 23, 25, 27, 29]]
InPut4: [[0], [2, 4], [6, 8, 10], [12, 14, 16, 18]]
```
## Strings without library

> Created Python class myStringCls that accepts strings as parameters. Implemented the
following methods which perform the action required by the functions.
Note: You are not allowed to use any of the string library methods to perform these
operations. 

### You need to implement your own.

```sh
a. len(myString)
b. addStr(str1, str2)
c. cmpStr(str1, str2) # returns True or False
d. isItNullStr(str)
```

## Dictionaries

> A nested dictionary class named as nestedDict with two nested levels, to the existing
dictionary given below. Provide access methods to add and delete a particular element in the
dictionary.

Note: your deleteElem(value) method need to search for the element in the dictionary and
delete it if found in the dictionary.

```sh
qDict = {'a':{'A'}, 'b':{'bb': 'BB'}, 'c': {'C'}, ‘d’{‘dd’: ‘’}}
```

## Nested Lists

>Assume a nested list similar to the ones below which are pre-filled with numbers ranging from 1 to 4. You will be given a prefilled random nested matrix which will only have integers in the given range.

Write a function that counts number of 1’s, 2’s, 3’s and 4’s in the list and prints out the count at the end. Any number of integers may be there in a list.
Note: No need to check for matrix having any other values or types.

*testMat1 = [ [1, 2, 3, 2, 4], [4, 3, 1], [[[2, 1, 4, 2, 3, 3, 1]]] ]*

```sh
Output1:
No. of 1’s: 4
No. of 2.s: 4
No. of 3’s: 4
No. of 4’s: 3
```

*testMat2 = [[[[[3, 2, 1]], [[[4,2]], [], [2]]]]]*

```sh
Output2:
No. of 1’s: 1
No. of 2.s: 3
No. of 3’s: 1
No. of 4’s: 1
```
