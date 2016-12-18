# Person

## Description
This class represents a Person in real life.

## Parent class
None

## Attributes
* ```first_name```
  * data type: string
  * description: stores the person's first name
* ```last_name```
  * data type: string
  * description: stores the person's last name
* ```year_of_birth```
  * data type: integer
  * description: stores the person's year of birth
* ```gender```
  * data type: string (male/female/notsure)
  * description: stores the person's gender
* ```energizing```
  * data type: Energizing
  * description: implements the extra class's functions through this variable
* ```behaviour```
  * data type: Behaviour
  * description: implements the extra class's functions through this variable

## Instance methods
### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value

None

### ```check_value_error```
This function checks that parameters are valid.

#### Arguments

None

#### Return value
If the parameters are invalid, it raises a ValueError.
