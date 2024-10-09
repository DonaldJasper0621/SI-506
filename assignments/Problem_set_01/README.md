
# SI 506: Problem Set 01

## This week's Problem Set

This week's problem set focuses on statements and expressions, variable assignments, built-in
functions, a user-defined function, and basic string operations.

:bulb: In order to check your work, try utilizing the built-in function `print()` to print
the passed in argument to the screen.

:exclamation: Utilize the `Ruff` extension to format your code. Prior to submitting your work to
Gradescope, hover over anywhere in the `problem_set_01.py` code file within VS Code, then right click and select the "Format
Document" option from the drop-down menu.

## Background

This week's problem set utilizes data on the diverse range of tantalizing restaurants and eateries
located in Ann Arbor, and features some of Central Campus' most popular spots.

## 1.0 Problem 01

**Task:** Identify and create valid variable assignments for some of the popular
restaurants located in Ann Arbor.

1. You have been provided with ten (10) commented out lines of code that attempt
   to assign a restaurant's name to a variable. Only some of the lines contain
   valid variable assignments. Uncomment the statements that contain valid
   variable assignments.

2. Create a new variable called `cottage_inn` and assign to it a string representation of
   the place **Cottage Inn Pizza**.

   :exclamation: Make sure that you treat the restaurant name as a title
   (i.e., capitalize the first letter of every word).

3. Similarly, create a new variable called `madras_masala` and assign to it a string
   representation of the place **Madras Masala**.

   :exclamation: Make sure that you treat the restaurant name as a title
   (i.e., capitalize the first letter of every word).

## 2.0 Problem 02 (30 Points)

**Task:** Leverage several string methods that exhibit the requested behaviors in order to return a
modified version of each string indicated below.

1. Call the appropriate `str` method to return a version of the string assigned to `hopcat` that
   converts all its characters to **_lower_** case. Assign the return value to a new variable named
   `hopcat_all_lower`.

2. Call the appropriate `str` method to return a version of the string assigned to `jerk_pit` that
   converts all its characters to **_upper_** case. Assign the return value to a new variable named
   `jerk_pit_all_upper`.

3. Call the appropriate `str` method that can sum the number of times the letter `"m"` appears in
   the string assigned to `madras_masala`. Assign the return value to a new variable named
   `madras_masala_count_m`.

4. Call the appropriate `str` method that can be used to check whether the string assigned to
   `fleetwood_diner` ends with `"Diner"`. Assign the return value to a new variable named
   `has_diner`.

5. Call the appropriate `str` method to check whether the string assigned to `hola_seoul` starts
   with `"Seoul"`. Assign the return value to a new variable named `starts_seoul`.

6. Call the appropriate `str` method that returns a version of the string `comment` which
   substitutes the character `"&"` with the substring `" and "`. Assign the return value to a new
   variable named `updated_comment`.

   :bulb: Ensure you are passing the correct argument to the string method in order to account for
   any spacing errors in the original `comment` variable.

## 3.0 Problem 03 (10 Points)

**Task:** Leverage some of Python's built-in functions that exhibit the behaviors specified below in
order to complete the requested tasks.

1. Count the total number of characters in the string assigned to the variable `updated_comment` and
   assign it to a new variable called `num_chars`.

    :bulb: Utilize the built-in Python function that will help you determine the length of the string.

2. A food critic would like to visit each of the most popular restaurants in Ann Arbor. They
   collected the restaurant names and stored them in a list variable called `restaurants`. Call the built-in Python
   `print()` function and pass to it the following argument: an expression that involves calling another
   built-in Python function that returns the data type of the object assigned to the variable
   `restaurants`.

3. Please also help the food critic count how many restaurants are listed in the `restaurants` list.
   Assign the return value to a new variable called `num_restaurants`.

   :bulb: You should utilize the built-in Python function that will help you count.

## 4.0 Problem 04

**Task:** Perform various arithmetic operations to assist the food critic in calculating the total
bill for a meal with a group of their friends.

1. The food critic would like to invite six (6) of their friends to the restaurant, New York Pizza
   Depot. Before they visit the restaurant, the critic checks the menu online. Below is a table that
   shows the popular dishes the restaurant offers:

   | Food & Drinks        | Price  |
   | -------------------- | ------ |
   | Plain Cheese Pizza   | $18.99 |
   | Garlic Knots         | $6.99  |
   | Soda                 | $7.00  |
   | Oreo Cookie Shake    | $10.49 |
   | White Pizza          | $22.25 |
   | Mozzarella Sticks    | $17.99 |

   The food critic orders the following items for the group:

   * four (4) Plain Cheese Pizzas
   * five (5) orders of Garlic Knots
   * two (2) Sodas
   * five (5) Oreo Cookie Shakes
   * one (1) White Pizza
   * and two (2) orders of Mozzarella Sticks for the group

   <br />

   Calculate the total price of the order. Assign the return value to a variable
   called `total_price`.

   :exclamation: **Do not** consider taxes and tips for this problem.

2. Given that the state sales tax rate for Michigan is 6%, and the diners are
   willing to give the server a 15% tip based on the **total price before taxes**,
   what should be the total amount the group needs to pay for this meal (including tax and tip)? Assign
   the return value to a variable called `total_bill`.

   :exclamation: Please use the variable `total_bill` to calculate the total
   amount they need to pay.

3. The food critic and his six (6) friends decide to split the entire bill
   evenly. What would be the amount that each person pays? Assign the return
   value to a variable called `each_pay`.

   :exclamation: Please use the variable `each_pay` to calculate the amount
   each person must pay and keep all digits after the decimal.

## 5.0 Problem 05 (5 Points)

**Task:** Pass a formatted string literal (f-string) to the built-in Python `print()` function.

1. Utilize an f-string and the variables `updated_comment` and `jerk_pit_all_upper` to print out the
   following sentence:

   ```markdown
   Someone said 'Truly authentic Jamaican food and drinks' on Yelp for the restaurant JAMAICAN JERK
   PIT.
   ```

   :exclamation: The comment **Truly authentic Jamaican food and drinks** in the sentence must be
   surrounded by **single quotes**.

## 6.0 Problem 06

**Task:** Help the food critic analyze the popularity of different dishes at The Jerk Pit by
calculating the percentage of total orders for each dish.

1. The food critic collected data on the number of orders for some popular dishes at The Jerk Pit
   during a busy weekend. Below is the table showing the number of customer orders for each dish:

   | No. | Dish | Customer Orders  |
   | :-- | :--- | :--------------- |
   | 1 | Jerk Pork | 120 |
   | 2 | Coconut Shrimp | 95 |
   | 3 | Jerk Wings | 80 |
   | 4 | Caesar Salad | 45 |
   | 5 | Jerk Tofu | 60 |
   | 6 | Oxtail | 30 |

2. Compute the total number of orders across all dishes. Assign the value to the variable named
   `total_orders`.

3. Define a function named `calc_pct` that is provisioned with two parameters:

   * The number of orders for a specific dish.
   * The total number of orders across all dishes.

   **Requirements**

   1. The function _must_ calculate the percentage of total orders for the specified dish.

   2. The function _must_ round the percentage to _`2` decimal places_ and return the result.

4. After implementing the function, add two blank lines after the function block. Next, create a
   variable for each dish (`6` variables in total). Create the variables in the same order as the
   table rows.

   Each variable name _must_ adhere to the following formatting rules:

   1. Base the variable name on the dish name.

   2. Use only lowercase characters.

   3. Replace each space encountered in the dish name with an underscore (`_`) character.

   4. Add the suffix `_pct` to each variable name.

5. Call the function `calc_pct()` for each dish and pass to it the arguments required to determine
   the dish's percentage share of `total_orders`. Assign the return value of each function call
   to each of the appropriate "dish" variables you created above.

6. After returning all the dish percentages, call the built-in Python `print()` function and pass all six
   (`6`) `*_pct` variables to it as arguments in the same order adopted when creating each variable.
   Separate each argument with a comma (`,`).

7. Right click over `problem_set_01.py` and select the "Format Document" option. Then run your code
   and check the output. You must print the following numbers in the order specified below:

   ```commandline
   27.91 22.09 18.6 10.47 13.95 6.98
   ```

## 7.0 Problem 07

**Task:** Imagine you're reading a lively review of Ann Arbor's own
[Jamaican Jerk Pit](https://jamaicanjerkpit.com/). Your goal is to analyze this review by counting
how many times certain key words are mentioned and identifying sentences that stand out for their
vivid descriptions or unique structure.

One of the review comments is provided below as a multiline string:

```python
review = """First time trying Jamaican Jerk Pit, and it was a lovely experience. There is seating on
the ground floor when you walk in with additional seating downstairs. The waitress welcomed us and
provided thorough and very helpful recommendations to make our first visit well worth it. Ordered
the curry goat and Jamaican chicken and both were packed with flavor with the meat easily
falling off the bones. Mixing in the sauce with the rice was a great idea too. Festivals were
strangely addicting. Very simple in appearance and taste but I couldn't stop eating them. Crispy
on the outside, soft in the inside. I have had fried plantains with sugar before and it was as
expected. I would recommend!
"""
```

1. Use the appropriate `str` method to return the total number of characters in the multiline
   string. Assign the return value to a variable named `total_chars`.

   Uncomment the accompanying `print()` call, run your code, and review the output. The integer
   value _must_ equal `691`.

2. Write a **single-line arithmetic expression** that _sums_ the individual counts of the two
   characters that _terminate_ sentences in `review`. Assign the return value of the expression to a
   variable named `sentence_count`.

   :bulb: Derive each count by calling the appropriate `str` method for each and then adding the two for the final sum.

   Uncomment the accompanying `print()` call, run your code, and review the output. The integer
   value _must_ equal `10`.
