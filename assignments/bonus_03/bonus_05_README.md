
# SI 506: BONUS 05

:exclamation: Utilize the `Ruff` extension to format your code before submitting to Gradescope.

## 1.0 Challenge

__Task__: The U-M campus hosts a number of EV charging stations. Access the U-M station(s) located on Greene Street by employing a `for` loop and a compound conditional statement.

Base your solution on the given list of stations and headers. Use list methods to look up index values and apply filters.

Break the problem into subproblems and solve each in turn, checking your progress by using the built-in `print()` function.

:exclamation: Remember that list methods like `append()` perform in-place operations and return `None`, so carefully consider when to assign values.

__Requirements__

1. Look up the index value for `"station_name"` in `headers` and assign it to `name_idx`.
2. Look up the index value for `"street_address"` in `headers` and assign it to `street_idx`.
3. Replace the `pass` statement with a compound `if` statement to filter on:
   1. U-M owned stations (station name starts with `"U-M"`).
   2. Stations located on "Greene Street".
4. Append each matching station to the `um_stations` list.
5. Uncomment `print()` and `pp.pprint()` to display your results.
6. Uncomment `Assert` when um_stations is complete.

### 1.1 Gradescope submissions

Feel free to submit your code to Gradescope after implementing each `um_stations` requirement.

:exclamation: When submitting your code to Gradescope, be sure to __comment out__ the `assert` statement if it triggers an `AssertionError`. If an exception occurs locally, it will also occur during the autograding process, resulting in a score of `0`.

Once you have implemented all the requirements, uncomment the final `print()` and `pp.pprint()` calls, along with the `assert` statement. Run your code to review your results, then upload your solution to Gradescope.

To earn full points, your `um_stations` list must pass the `assert` statement.
