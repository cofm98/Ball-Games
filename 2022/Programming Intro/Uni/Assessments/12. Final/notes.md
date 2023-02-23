# Program Goals and Marking Guide
## Objective

## Aims
- ++Any created class (that is not required by application.py) should have multiple
objects.
- ++Every class has an initialiser. Initialiser takes responsibility for ensuring
all instance variables are created.
- +Hiding members whenever possible.
- +Built-in exceptions raised.
- +All exceptions handled; messages shown use the message from exception objects
- +Parameters (other than ‘self’ and ‘cls’) in some/all methods. Values returned by
some methods (other than the default value).
- +Accessor methods created and used as shown in latter IIEs.
- +Mutator methods created and used as shown in latter IIEs.
- +Object-oriented methods created and used as appropriate.
- +Non-object-oriented methods created and used as appropriate.
- +Uses function annotations for all parameters and return values of every method
    - (except ‘self’, ‘cls’ and return type of ‘init’).
- +Uses the ‘open’ function along with .readline to read data from files. Uses the
‘open’ function along with .write to write data to files.
## Avoid
- ------Did not include sample user input file for testing full program
(test_case.txt)
- ------Frontend code runs automatically upon import or shows interface before the
message in application.py
- ------Backend code runs automatically upon import
- -For each code concept that has been overused (e.g. modules, classes, functions,
methods, variables, etc.)
- -For each code concept has been underused (e.g. modules, classes, functions,
methods, variables, etc.)
- --For each line of code outside of class blocks excluding ‘import’ statements
(does not apply to application.py)
- --For each line of code outside of def blocks (excluding ‘class’, ‘import’ and
justified class-variables) statements (does not apply to application.py)
- --“Backend” code takes inputs via keyboard (e.g. stdin, input, etc.)
- --“Backend” code produces outputs (e.g. stdout, stderr, print, etc.)
- --“Front end” has knowledge of other classes (e.g. “Student”) used by “backend”
code.
- ----“Backend” has knowledge of “front end” classes and/or members.
- -A variable holds data of different data types at different times (None type
permitted).
- -A list contains items of mixed data types (None type permitted).
- -A parameter expects a list of a specific length.
- -“Front end” does not communicate with the “back end” using only built-in int,
float and str types or lists.
- -A constructor does not take parameters for crucial initial values of the object.
- -Screen outputs do not exclusively use sys.stdout.write or sys.stderr.write
- -Keyboard inputs do not exclusively use sys.stdin.readline
- -Does not follow coding conventions for identifiers.
- -Non-descriptive identifier names (e.g. arbitrary or abbreviated names, etc.
when more descriptive names suitable)
- -Confusing identifier names (e.g. name or student number in the file name, etc.)
- ----Did not contain a list of objects in the required class as per design
patterns shown in Course-wide Lectorials (E.g. list of Student objects).
- -Uses non-list data structures (I.e. dictionaries, tuples, etc.)
- -Does not use if/elif/else-statements exclusively for non-repeating conditional
execution.
- -Does not use while-loops exclusively when repetition required (e.g. no for-
loops, recursion, etc.).
- -Compound conditions written without 'or' and/or 'and'
- -For each type of restricted operator used: 'in' (containment), bitwise operators,
'is' (identity), 'not' (logical negation), shift operators, '@' matrix
manipulation, slicing and similar operators not shown in Course-wide Lectorials.
- -For each unique use of the following Python keywords: await, pass, break,
continue, as (but permitted to use with ‘except’), from, nonlocal, assert, global,
with, async, yield
- -Uses something other than double quotes " to enclose strings. (Tip: Triple double-
quotes or triple single-quotes, which are typically used for multi-line strings,
are not allowed).
- -For each instance of nested def blocks.
- -Uses ‘return’ before the last line of a function.
- -Multiple values returned from a function or values of different data types
returned from a function. (Returning one list is acceptable).
- -Uses exit-like operations (e.g. sys.exit, os.exit, etc.)
- -Comments added on the same line with code or comments do not use
professional/academic English.
- -Irrelevant or unreachable code+comments included. (E.g. commented out code, non-
justification comments, etc.)
- -Conditions include tautologies or if/else/elif/while constructs have redundant
pathways or unreachable blocks.
- -Too much or too little code inside try..except or uses try..except to hide
deficiencies in code (as opposed to using it to enhance the program)
- -Keeps file objects opened longer than needed.
- ---- Hard coded filenames/paths (does not apply to application.py).
- -String concatenation does not follow approaches shown in class.
- --Sample data file missing or does not have enough records to test features.