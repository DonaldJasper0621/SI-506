
# SI 506: BONUS 02

:exclamation: Utilize the `Ruff` extension to format your code before submitting to Gradescope.

## 1.0 Challenge 01

__Task__: The _Spam and More_ eatery is under new management and is basing its new menu on the
Pythons' beloved Bromley cafe menu. Construct a new menu based on the multiline string constant
named `MENU` per management's set of requirements. Employ string and list method calls to accomplish
the task.

Base the new menu on the multiline string constant named `MENU`. Assign all values returned by the
various method calls to a variable named `new_menu`.

Take your time. Break the problem into subproblems. Solve each subproblem in turn by calling the
appropriate `str` or `list` method. Call the built-in `print()` function after each change and check
your progress.

:exclamation: Recall that certain list method calls perform in-place operations and return `None` to
the caller. So consider carefully whether or not to assign the return value of a list method call
to `new_menu`. You might inadvertently assign `None`.

__Requirements__

:exclamation: The six (`6`) requirements are listed in no particular order. You will need to consider
carefully the operations to be performed and the order in which they need to occur.

:bulb: Consider dividing the requirements into two groups. Group 01 are requirements that involve
calling `str` methods (e.g., `str.lower()` etc.). Group 02 are requirements that involve calling
`list` methods (e.g., `list.append()`). This approach should help in determining the order in which
the requirements are to be implemented.

* Replace "sausage" with "toast" __and__ a trailing
  [Serial or Oxford comma](https://en.wikipedia.org/wiki/Serial_comma) (e.g. "sausage" >> "toast,").
* Append the `new_item` ("belgian waffles, whipped cream, fruit, and spam") to the list.
* Convert all characters to lowercase.
* Convert the multiline string to a list.
* Replace every _third_ helping of "spam" featured in a menu item with "oatmeal".
* Remove the "lobster thermidor ..." menu item from the list.

### 1.1 Gradescope submissions

Feel free to submit your code to Gradescope after each `new_menu` requirement that you implement.

:exclamation: When submitting your code to Gradescope be sure to __comment out__ the `assert`
statement if it is triggering an `AssertionError`. If you trigger an exception locally the auto
grader will also trigger the exception, resulting in `0` points earned.

Once you have implemented all requirements uncomment the final `print()` and `ppprint()` calls along
with the `assert` statement, run your code, review your work, and upload your code to Gradescope.

To earn full points, the `new_menu` you create _must_ pass the `assert` statement.
