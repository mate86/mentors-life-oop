# Student

## Description
This class represents a student in real life. It should inherit all properties from the Person class.

## Parent class
Person class

## Attributes

* ```knowledge_level```
  * data type: integer
  * description: stores the knowledge level of the student in programming
* ```energy_level```
  * data type: integer
  * description: current energy level

## Instance methods
### ``` __init__```
calls the Person's constructor.
Set's the attributes above.
Raise an error, if any is empty.

#### Arguments

* ```first_name```
  * description: inherted from Person class
* ```last_name```
  * description: inherted from Person class
* ```year_of_birth```
  * description: inherted from Person class
* ```gender```
  * description: inherted from Person class

## Class methods

### ``` create_by_csv```

Creates a ```create_by_csv``` object the csv contains all the data needed to instantiate a student object
Gets a csv file path as an argument.

#### Arguments
None

#### Return value
gives back a list of students

