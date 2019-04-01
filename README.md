# intrv-jam
Get data from A to B

This repo is an exercise (hopefully not in futility) to understand your programming style,
problem solving methodology and expertise in Python. There is no time limit for any of this,
but the primary exercise should be able to be completed in about an hour.

# Exercise

In this repo are two input text files: test1.txt and test2.txt. 

Your program/script should accept a filename as input, parse that file, 
and create a table in an SQLite database.

e.g. `intrv_jam.py test1.txt`

Clone this repo, write your code and then submit a PR.

## Requirements

- Code must be Python3
- Table names should be based on the filename w/o extension, e.g. test1
- Database file should be named `db.sqlite`
- Must use the `pandas` python module
- State which OS system has been tested on (I will use the same)
- The db.sqlite file should not be included in your PR and it should be created by your 
script at runtime if it doesn't exist
- You can assume any python modules you use will be available on the destination system
- Your program/script need not be generic to handle any file types. Only the two files
in this repo will be tested. 

## Assumptions

Anything not clearly outlined in this README is up to your interpretation. We all know requirements
aren't always clear and ambiguity is always present, so for any questions you have, 
you should assume an answer and place that in an `assumptions.txt` file. 
This does not have to be exhaustive. E.g.:

```
Assuming that phone number should have punctuation stripped out
...not loading the empty column in file abc.txt
```
