# SI 506 Week 04: Iteration and Control Flow, Part I

## Python 3.x Glossary

## 1.0 New for this week

* __accumulator pattern__. A design pattern that employs a variable to accumulate or aggregate
  values. The accumulator pattern is often used in conjunction with a loop to iterate over a
  sequence of values.

* __flow of execution__. The order in which statements in a program are executed. Also referred to
   as _control flow_.

* __conditional statement__. A statement that controls the flow of execution based on a condition.
  The `if`, `elif`, and `else` statements are examples of conditional statements.

* __range__. The `range` type is not a function but an immutable sequence type like a string,
  list, or tuple. When instantiated (i.e., created) the `range` object represents a sequence of
  numbers that can be looped over.

## 1.0 Environment

* __Python_interpreter__. The "engine" that parses, compiles, and executes Python code.

* __Python_interactive console__. Also known as the Python shell, the interactive console is a
  command line interpreter or REPL (Read-Evaluate-Print-Loop) that executes Python code on a
  line-by-line basis. The interactive console is especially useful for testing snippets of code,
  debugging, performing quick calculations, or learning Python.

## 2.0 Basic syntax and semantics

* __comment__. Explanatory text embedded in code with no impact on the runtime
  characteristics of the program or script. Single line comments are delineated by prefacing
  the line with a hash (`#`) character.

* __expression__. An accumulation of values, operators, and/or function calls that return a value.
  `len(< some_sequence >)` is considered an expression.

* __immutable__. A characteristic of certain object types that renders them incapable of change.
  Strings and tuples are examples of an immutable type.

* __index__. Numeric position of an element or item contained in an ordered sequence. Python
  indexes are _zero-based_, i.e., the first element's index value is `0` not `1`.

* __iterable__. An object capable of returning its members one at a time. Strings, lists, tuples,
  and dictionaries are examples of an iterable.

* __mutable__. A characteristic of certain object types that render them modifiable. Lists and
  dictionaries are examples of a mutable type.

* __object__. A data [abstraction](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
  that possesses, at a minimum, an identity, type, and value. An object's attributes may also include
  defined behaviors (known as _methods_) that can be accessed by a user.

* __operator__. A [symbol](https://www.w3schools.com/python/python_operators.asp) for performing
  operations on values and variables. The assignment operator (`=`) and arithmetic operators
  (`+`, `-`, `*`, `/`, `**`, `%`, `//`).

* __sequence__. An [iterable](https://docs.python.org/3/glossary.html#term-iterable) such as a
  `str`, `list`, `tuple`, or `set` whose members (e.g., characters, elements, items) can be
  accessed individually or in groups by employing integer indices in the case of sequences or keys
  in the case of dictionaries.

* __slice__. A subset of a sequence. A slice is created using the slice notation operator `[]` with
  colons separating numbers when several are given, such as in `variable_name[1:3:5]`. The bracket
  notation uses slice objects internally.

* __statement__. An instruction that the Python interpreter can execute. For example, assigning a
  variable to a value such as `name = "arwhyte"` is considered a statement. A statement can be
  composed of one or more expressions (the reverse is not true).

* __subscript operator__. Square brackets (`[]`) appended to a sequence that enclose either an
  index value or a slicing expression. The resulting expression is used to access individual or
  groups of characters, elements, or items.

* __variable__. A name, label or pointer that refers to an object in memory.

* __value__. Data attached to an object. Data can range from a "primitive" type such as a
  number or boolean to more complex data types such as sequences, maps, date, and time, or even a
  the absence of a value as represented by `None`.

## 3.0 Data types

A data type (or type) is a data structure that contains a value or values. Each data type also
possess attributes that determine the operations that can be performed on it.

* __boolean__. A [truth value](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
  type ([`bool`](https://docs.python.org/3/library/functions.html#bool)) or expression that
  evaluates to `True` or `False`.

* __float__. A numeric type ([`float`](https://docs.python.org/3/library/functions.html#float))
  that references a floating point number.

* __integer__. A numeric type ([`int`](https://docs.python.org/3/library/functions.html#int))
  that references a whole number.

* __list__. A _mutable_ [sequence](https://docs.python.org/3/glossary.html#term-sequence) type
  ([`list`](https://docs.python.org/3/library/stdtypes.html#list)) of object references
  (i.e., elements) that can be _mutated_ after creation. A list is delineated by the use of square
  braces (`[]`) as in `["arwhyte", "csev", "cteplovs"]`. List elements can be accessed either
  individually or in groups by employing integer indices.

* __string__. An _immutable_ [sequence](https://docs.python.org/3/glossary.html#term-sequence) type
  ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) of character references. Strings
  are delineated by the use of double (`""`) or single quotes (`''`) as in `"SI 506"`. Individual
  characters can be accessed either individually or in groups employing integer indices.

* __tuple__. A _immutable_ [sequence](https://docs.python.org/3/glossary.html#term-sequence) type
  ([`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)) of item references. Tuples are
  delineated by the use of parentheses (`()`) as in `("Ann Arbor", "MI")`. Tuple items can be
  accessed individually or in groups employing integer indices. Single item tuples _must_ include a
  trailing comma (`,`) as in `("Go Blue",)` or the expression will be treated as a string.

## 4.0 Functions

* __built-in function__. A [function](https://docs.python.org/3/library/functions.html) defined by
  the Standard Library that is always available for use in your code. The `print()` function is an
  example of a built-in function.

* __argument__. A value passed to a function or method that corresponds to a parameter defined for
  the function or method.

* __caller__. The act of invoking or calling a function via an expression or statement.

* __keyword argument__. Argument passed to a function or object method that is assigned a specified
  parameter name (i.e., `< keyword >=< argument >`). A keyword argument is not subject to positional
  ordering as is the case with an unnamed argument. Keyword arguments also tend to enhance code
  readability.

* __method__. A function defined by and _bound to_ a particular object. Dot notation (`.`) is
  employed to call an object method. For example the `str` type is provisioned with a number of
  methods including `str.lower()`, `str.split()`, and `str.strip()`.

* __parameter__. A named entity in a function or method definition that specifies an argument that
  the function or method can accept from a caller.

## 5.0 Operations

* __concatenation__. Joining one object value to another in order to create a new object. Combining
  two strings together (e.g., `greeting = "Hello " + "SI 506"`) to create a new string is an example
  of string concatenation.

* __formatted string literal (f-string)__. An [f-string](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals)
  provides an economical syntax for constructing a string literal based on some combination of
  alphanumeric characters, object references (i.e., variables), spaces, and escape sequences. A
  formatted string literal is prefixed with `f` or `F` as in `f"email = {uniqname}@umich.edu"`.

* __slicing__. Accessing a subset of a sequence. A slice is created using the slice operator `[]`
  to define a `stop` index, and optionally, `start` and/or `step` indices, as in
  `some_sequence[1:10:2]` or by calling the built-in function
  [`slice()`](https://docs.python.org/3/library/functions.html#slice).

* __variable assignment__. Assigning a variable to an object (e.g. `uniqname = "arwhyte"`).
  A variable is nothing more than a name, label, or pointer to an object containing a value. It can
  be reassigned to another object at any time.
