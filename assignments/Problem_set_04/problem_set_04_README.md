# SI 506: Problem Set 04

## This Week's Problem Set

This week's problem set includes seven (7) problems that focus on loops and conditional statements.

## Background

The UMSI Career Fair happens each Fall and Winter term. You can find more information about
employers of interest through Handshake (https://umich.joinhandshake.com/).

For this problem set, you are provided with a list of data that includes basic information about the
employers who attended the Winter 2023 career fair, including names, locations, the total number of
employees, websites, and their industries, respectively. You are going to use `for` loops, `while`
loops, and `conditional statements` to complete the problems below.

## 1.0 Problem 01 (20 points)

**Task:** Implement a function that takes a list of strings and creates a new list of lists. Use a
`for` loop and the `range` type to populate a nested list. Then, call the function to create a list
of lists from the `data` list.

1. Implement the function `format_data()`. The function takes a list of strings and creates a list
   of lists by splitting each string using a specified delimiter. The function is provisioned with
   two (`2`) parameters in the following order:

   - `data` (list): A list of strings.
   - `delimiter` (str): A string that separates the elements in each string.

   **Requirements:**

   1. Inside the function block, assign a variable named `formatted_data` to an empty list.

   2. Using a `for` loop with the `range()` type, access each string element in `data`. Use the
      appropriate `str` method to **split** each string element into a list based on the `delimiter`.
      Assign the new list to _any_ variable name of your choice.

   3. **Add** the new list to `formatted_data` using the appropriate `list` method.

   4. Outside of the loop block, return the `formatted_data` list.

2. Within `main()`, call the `format_data()` function on `DATA` and assign the returned value to a
   new variable named `employers`.

   ❗️ Ensure that you are passing the correct delimiter value.

   ❗️ The value assigned to `employers` _must_ match the list `EMPLOYERS_CHECK`
   (see Setup Code). Uncomment the associated `assert` and `print()` statements, run your code, and
   confirm that the variables match the expected values.

3. Extract the first element from the `employers` list using list indexing and assign it to a
   variable named `headers`.

   ❗️ The value assigned to `headers` _must_ match the list `headers_check`(see Setup Code).
   Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
   the variables match the expected values.

## 2.0 Problem 02 (20 points)

**Task:** Implement a function that filters out employers into two groups based on their name. Then,
call the function to separate `employers` into one list for entries that match **both** keywords
and another list for all other entries.

1. Implement the function `group_employers()`. The function filters a list based on two specified
   filtering criteria. The function is provisioned with three (`3`) parameters in the following
   order:

   - `employers` (list): A list of lists.
   - `keyword1` (str): A string that is used to filter the list.
   - `keyword2` (str): A string that is used to filter the list.

   **Requirements:**

   1. Inside the function block, assign a variable named `matching_companies` to an empty list.

   2. Again, inside the function block, assign another variable named `other_companies` to an empty
      list.

   3. Using a standard `for` loop, iterate over each element in the list `employers`, **excluding**
      the headers row.

   4. Within the loop block, extract the first element of each nested list in the `employers` list
      and utilize `str` method chaining to:
      1) perform a **case-insensitive** transformation
      2) remove _any_ **leading** and **trailing** spaces

      Assign the resulting string to _any_ variable name of your choice.

      ❗️ Ensure that you extract the employer variable and perform `str` method chaining (one `str`
      method for **case-insensitive** transformation, and one `str` method for removing _any_
      **leading** and **trailing** spaces) in a single line of code.

   5. In the loop block, write an `if` statement that evaluates whether the new variable includes
      **both** `keyword1` _and_ `keyword2`.

      - If the conditional statement evaluates to `True`, **add** the employer list to the
         `matching_companies` list.

      - Otherwise, if the conditional statement evaluates to `False`, **add** the employer list to
         the `other_companies` list.

   6. Outside of the loop block, return a tuple containing the `matching_companies` and
      `other_companies` lists.

2. Within `main()`, call the `group_employers()` function on `employers`, with `"university"` and
   `"innovation"` as the keywords. Assign the return value to a variable named `grouped_employers`.
   Next, extract the **first** element of the returned tuple and assign it to a new variable named
   `universities_innovation`. Similarly, extract the **second** element of the returned tuple and
   assign it to a new variable named `other_companies`.

   ❗️ Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
   the variables match the expected values.

## 3.0 Problem 03 (20 points)

**Task:** Implement a function that filters employers based on their industry. Then, call the
function to bin the `employers` into five lists based on their industry.

1. Implement the function `filter_by_industry()`. The function filters a list of employers based on
   their industry. The function is provisioned with three (`3`) parameters in the following order:

   - `list_` (list): A list of lists.
   - `headers` (list): A list of strings that represent the headers of the `employers` list.
   - `industry_filter` (str): A string that is used to filter the list.

   **Requirements:**

   1. Inside the function block, assign a variable named `filtered_companies` to an empty list.

   2. Using a standard `for` loop, iterate over each element in `list_`.

   3. Within the loop block, extract the _industry_ information from each company using `headers`
      to find the appropriate **index**, and assign it to a variable named `industry`, while
      utilizing `str` method chaining to perform a **case-insensitive** transformation and remove
      _any_ **leading** and **trailing** spaces.

      ❗️ Ensure that you extract the industry variable and perform `str` method chaining (one `str`
      method for **case-insensitive** transformation, and one `str` method for removing _any_
      **leading** and **trailing** spaces) in a single line of code.

   4. Next, extract the _name_ of the company from each company list and assign it to a variable
      called `name`.

   5. In the loop block, write an `if` statement that evaluates whether the value stored in
      `industry` matches `industry_filter`.

      - If the conditional statement evaluates to `True`, **add**  _only_ the name of the
         associated company to the `filtered_companies` list.

   6. Outside of the loop block, return the `filtered_companies` list.

2. Within `main()`, call the `filter_by_industry()` function on `other_companies`, with `"consulting"`
   as the industry filter. Assign the returned value to a new variable named `consulting`.

   ❗️ Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
      the variables match the expected values.

3. Within `main()`, call the `filter_by_industry()` function on `other_companies`, with `"education"`
   as the industry filter. Assign the returned value to a new variable named `education`.

   ❗️ Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
      the variables match the expected values.

4. Within `main()`, call the `filter_by_industry()` function on `other_companies`, with `"healthcare"`
   as the industry filter. Assign the returned value to a new variable named `healthcare`.

   ❗️ Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
      the variables match the expected values.

5. Within `main()`, call the `filter_by_industry()` function on `other_companies`, with `"software"`
   as the industry filter. Assign the returned value to a new variable named `software`.

   ❗️ Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
      the variables match the expected values.

## 4.0 Problem 04 (25 points)

**Task:** Implement a function that identifies the largest companies by employee count in a given
state. Then, call the function to find the largest companies in Michigan and California.

1. Implement the function `get_largest_companies()`. The function finds the largest companies in a
   given state by comparing their employee counts. The function is provisioned with two (`2`)
   parameters in the following order:

   - `companies` (list): A list of lists.
   - `state` (str): A string that represents the state to filter the companies.

   **Requirements:**

   1. Inside the function block, assign a variable named `largest_companies` to an empty list.

   2. Again, inside the function block, assign a sensible start value to a variable named
      `max_num_employees`.

      :bulb: Consider what value would ensure any valid number of employees will be larger,
      including zero employees.

   3. Using a standard `for` loop, iterate over each element in `companies`.

   4. Within the loop block, extract the _number of employees_ from each company within the
      `companies` list. Convert the _number of employees_ element into an integer and assign it to
      a variable named `num_employees`.

      ❗️ Ensure that you extract the _number of employees_ element from the `companies` list and
      convert it into an integer in a single line of code.

   5. Next, extract the _location_ element (i.e., the state) from each company within the
      `companies` list and assign it to a variable named `location`. Utilize `str` method chaining
      to perform a **case-insensitive** transformation and remove _any_ **leading** and
      **trailing** spaces.

      ❗️ Ensure that you extract the location variable and perform `str` method chaining (one `str`
      method for **case-insensitive** transformation, and one `str` method for removing _any_
      **leading** and **trailing** spaces) in a single line of code.

   6. In the loop block, write a conditional `if` statement that performs a **case-insensitive**
      equality check to determine whether the extracted `location` matches the `state`.
      If the location matches the state, write a nested conditional `if-elif` statement comparing
      the company’s number of employees `num_employees` with `max_num_employees`.

      - If the company's employee count is greater than `max_num_employees`, update
         `max_num_employees`, clear the `largest_companies` list, and add **only the company name**
         to the `largest_companies` list.

      - If the company's employee count is equal to `max_num_employees`, add **only the company name**
         to the `largest_companies` list without clearing it.

   7. Outside of the loop block, return the `largest_companies` list.

2. Within `main()`, call the `get_largest_companies()` function on `other_companies`, with
   `"michigan"` as the state. Assign the returned value to a new variable named
   `largest_michigan_companies`.

   ❗️ Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
      the variables match the expected values.

3. Within `main()`, call the `get_largest_companies()` function on `other_companies`, with
   `"california"` as the state. Assign the returned value to a new variable named
   `largest_california_companies`.

   ❗️ Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
      the variables match the expected values.

## 5.0 Problem 05 (20 points)

**Task:** Implement a function that converts a _multiline_ string into a formatted list of lists.
Then, call the function to convert a list of salaries.

1. Implement the function `convert_multiline_string()`. The function takes a _multiline_ string,
   splits it by line breaks, and formats it by passing the resulting list into the `format_data()`
   function. The function is provisioned with one (`1`) parameter:

   - `multiline_string` (str): A _multiline_ string where each line represents an entry.

   **Requirements:**

   1. Use the `.splitlines()` method to split the `multiline_string` into a list of strings. Assign
      the resulting list to a variable named `splitlines`.

      ❗️ The `.splitlines()` method automatically splits the string by line breaks and
      returns a list of strings.

   2. Pass the `splitlines` list into the `format_data()` function along with the delimiter `"; "`
      (a semicolon followed by a space). The `format_data()` function will return a list of lists
      with the formatted data.

      ❗️ The `format_data()` function _must_ be called within the
      `convert_multiline_string()` function.

   3. Return the formatted string from the `format_data()` function call.

      ❗️ You _must_ directly return the formatted string from the `format_data()` function
      call in a single line of code without storing the formatted string in a variable.

2. Within `main()`, call the `convert_multiline_string()` function on a _multiline_ string variable
   called `SALARIES`. Assign the returned value to a new variable named `salary_list`.

   ❗️ The value assigned to `salary_list` _must_ match the list `SALARY_LIST_CHECK` (see Setup Code).
   Uncomment the associated `assert` and `print()` statements, run your code, and confirm that the
   variables match the expected values.

## 6.0 Problem 06 (25 points)

**Task:** Implement a function that gets a list of salaries for consultants and managers. Use a
`while` loop (a.k.a. an **indefinite** loop) to iterate over the list of salaries and extract the
salaries for consultants and managers. Then, call the function and calculate the average salary for
consultants and managers.

❗️ Mistakes can happen. Beware of getting stuck in an infinite loop. If you need to exit
the infinite loop, type `CTRL + C` or `command + C` in the terminal.

1. Implement the function `get_consult_manager_salaries()`. The function takes a list of salaries
   and finds the salaries for consultants and managers. The function is provisioned with one (`1`)
   parameter:

   - `salaries` (list): A list of salaries.

   **Requirements:**

   1. Inside the function block, assign a variable named `consult_manager_salary` to an empty list.

   2. Again, inside the function block, assign a sensible start value to a variable named
      `i`.

      :bulb: Consider where iteration typically starts in a list.

   3. Utilize a `while` loop to iterate over `salaries`, using the variable `i` to track your
      position in the list.

   4. Within the `while` loop block, extract the _job title_ for each job, and assign this value to
      a variable named `job_title`. Utilize `str` method chaining to perform a **case-insensitive**
      transformation and remove _any_ **leading** and **trailing** spaces.

      ❗️ Ensure that you extract the _job title_ element from each list in `salaries` and perform
      str method chaining (one `str` method for **case-insensitive** transformation, and one `str`
      method for removing _any_ **leading** and **trailing** spaces) in a single line of code.

   5. Next, extract the _salary_ for each job within `salaries`. Convert the _salary_ element into an
      integer and assign it to a variable named `job_salary`.

      ❗️ Ensure that you extract the _salary_ element from each list in `salaries` and convert it
      into an integer in a single line of code.

   6. In the loop block, write an `if` statement that employs the appropriate membership operator to
      select **jobs that are titled** for **either** a `Consultant` **or** `Manager`. Inside the
      conditional statement, populate the `consult_manager_salary` list with the salaries for
      that job from `job_salary`.

      💡 Remember to increment the value of `i` by one (`1`) in each iteration.

      ❗️ Ensure that you are using the appropriate logical operator to select jobs that are titled
      for **either** a `Consultant` **or** `Manager`.

   5. Outside of the loop block, return the `consult_manager_salary` list.

2. Within `main()`, call the `get_consult_manager_salary()` function on `salary_list` and assign the
   returned value to a new variable named `consult_manager_salary`.

   ❗️ Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
      the variables match the expected values.

3. Write an expression that computes the _average_ salary for the salaries contained in
   `consult_manager_salary`. Utilize two built-in functions to calculate the _average_ salary in the
   `consult_manager_salary` list, then use another built-in function to _round_ the _average_ salary
   to two (`2`) decimal places. Assign this value to the variable `avg_consult_manager_salary`.

   ❗️ The built-in `sum()` function _must_ be used to calculate the sum of all items in the
      `consult_manager_salary` list. The built-in `len()` function _must_ be used to calculate
      the number of items in the `consult_manager_salary` list. Another built-in function _must_ be
      used to _round_ the average salary value.

   ❗️ Ensure that you are calculating the _average_ salary and _rounding_ the value to two decimal
      places in a single line of code.


## 7.0 Problem 07 (20 points)

**Task:** Implement a function that groups companies based on their salary. Use a `while` loop with
`if` and `elif` statements to assign companies to different salary ranges. Then, call the function
to group companies accordingly.

1. Implement the function `group_salaries()`. This function categorizes companies based on their
   salary into two groups: those within a given salary range and those above it. The function takes
   in three(`3`) parameters:

   - `salaries` (list): A list of salaries.
   - `salary1` (int): The minimum value for the first salary range.
   - `salary2` (int): The maximum value for the first salary range.

   **Requirements:**

   1. Inside the function block, assign a variable named `company_salary_one` to an empty list.

   2. Again, inside the function block, assign a variable named `company_salary_two` to an empty
      list.

   3. Next, assign a sensible start value to a variable named `i`.

      :bulb: Consider where iteration typically starts in a list.

   4. Utilize a `while` loop to iterate over `salaries`, using the variable `i` to track your
      position in the list.

   5. Within the `while` loop block, extract the _salary_ for each job within `salaries`. Convert
      the _salary_ element into an integer and assign it to a variable named `job_salary`.

      ❗️ Ensure that you extract the _salary_ element from each list in `salaries` and convert it into an integer
      in a single line of code.

   6. Next, extract the _company name_ for each job within `salaries` and assign it to a variable
      named `company`.

   7. In the loop block, write an `if` statement that evaluates whether the value of `job_salary` is
      between `salary1` and `salary2`, with both being inclusive.

      - If the conditional statement evaluates to `True`, **add** the `company` to the
         `company_salary_one` list.

      - Otherwise, write an `elif` statement that evaluates whether the `job_salary` is greater than
         `salary2`.

         - If the conditional statement evaluates to `True`, **add** the `company` to the
            `company_salary_two` list.

      💡 Remember to increment the value of `i` by one (`1`) in each iteration.

   8. Outside of the loop block, return a tuple containing the `company_salary_one` and
      `company_salary_two` lists.

2. Within `main()`, call the `group_salaries()` function on `salary_list`, with `100000` and `200000`
   as the salary ranges. Assign the returned value to a new variable named `company_salaries`.

3. Extract the first element from `company_salaries` and assign it to a variable named
   `company_salary_one`.

   ❗️ Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
      the variables match the expected values.

4. Extract the second element from `company_salaries` and assign it to a variable named
   `company_salary_two`.

   ❗️ Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
      the variables match the expected values.