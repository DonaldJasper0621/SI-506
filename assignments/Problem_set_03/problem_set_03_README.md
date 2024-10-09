# SI 506: Problem Set 03

## This Week's Problem Set

This week's problem set includes eight (8) problems that focus on `for` loops, conditional
statements (`if-elif-else`), and the `range()` function. Some topics from
previous sections (e.g. methods, indexing, slicing, functions, and the `main()`) are also included.

## Background

This week's problem set deals with data about TV shows from various streaming platforms. You are
provisioned with two lists to operate on and extract meaningful information.

1. `TV_SHOWS`: Each list element is a string (`str`) containing the following information, in the
   order specified:

   - Show Name
   - Genre
   - Year of Release
   - IMDB Rating (0-10)
   - Rotten Tomatoes Rating (0-100)
   - Streaming Platform

2. `NEW_TV_SHOWS`: Represents TV shows from **2024**. Each list element is also a list (`list`)
   i.e. `NEW_TV_SHOWS` is a list of lists. Each nested list contains the same 6 pieces of TV show
   information but as individual list elements. These shows are NOT included in the `TV_SHOWS` list.

## Problem 01 (20 points)

This problem is divided into 2 tasks, A and B.

### Task A - Combining Data

The purpose of this task is to combine the `TV_SHOWS` and `NEW_TV_SHOWS` lists while ensuring that
they have a consistent data format.

1. First, implement the function named `convert_to_list()`. The function's task is to split a string
   into a list of substring elements using a specified delimiter and returns the resulting list. The function is provisioned with two parameters:

   - `show` (`str`): A string containing information about a particular TV show.
   - `delimiter` (`str`): The delimiter or separator used to split the string element into a list of
      substrings.

   **Requirements**

   1. Inside the function block, call the appropriate `str` method to split the passed in `show`
      string into a list of substring elements using the passed in `delimiter` value and return the
      result to the caller.

      :exclamation: Your function block must consist of a **single line of code**.

2. Within `main()`, create an empty list named `combined_tv_shows`.

3. Call the appropriate `list` method to **extend** `combined_tv_shows` with the `NEW_TV_SHOWS`
   list.

4. Uncomment the associated `print()` function call to print the first 5 elements of your
   `combined_tv_shows` list.

   :bulb: Note that `combined_tv_shows` is now a **list of lists**.

5. Next, combine the `TV_SHOWS` list with the `combined_tv_shows` list. As previously noted,
   `combined_tv_shows` is a list of lists whereas `TV_SHOWS` is a list of strings. Before combining
   the two, let's first convert each element of `TV_SHOWS` into a list to ensure consistency in our
   data format.

   1. To do this, loop over `TV_SHOWS` using a standard `for` loop. Inside the loop block, write code
      that implements the following operations:

   2. Call the `convert_to_list()` function on each show in `TV_SHOWS` and assign the return value
      to a new variable named `show_list`.

      :exclamation: Make sure to pass the correct delimiter value.

      :bulb: Carefully inspect the `TV_SHOWS` list (given in the Setup Code) to determine the
      character(s) used to **separate** each piece of TV show information for a particular show.

   3. **Append** `show_list` to the `combined_tv_shows` list using the appropriate list method.

6. Outside the loop block, uncomment the associated `assert` statement, run your code, and
      confirm that the lists are equal.

### Task B - Cleaning Data

Implement the function `clean_list()` that takes a list of lists and converts the data types of
certain elements within each of its nested lists. Then, call this function to compute a "cleaned"
version of `combined_tv_shows`.

7. First, implement the function named `clean_list()`. The function's task is to convert the data
   types of certain elements of a nested list. The function is provisioned with a single parameter:

   - `list_` (`list`): A list of lists.

   **Requirements**

   - Inside the function block, do the following operations:

      1. Implement a `for` loop that iterates over an instance of the `range()` function (i.e., a
         sequence of numbers). Instantiate the `range()` object with a stop value equal to the length
         of `list_`. Inside the loop block, write code that implements the following operations:

         1. Convert the IMDB Rating and the Rotten Tomatoes Rating of each nested list from type `str`
            to type `float`.

            :bulb: Make sure to use the proper indexing method for nested lists.

      2. Outside the loop block, return the updated `list_`.

8. Next, within `main()`, call the `clean_list()` function and pass it the `combined_tv_shows` list
   as an argument. Assign the return value to a variable called `cleaned_tv_shows`.

9. Uncomment the associated `assert` statement, run your code, and confirm that the lists are equal.

## Problem 02 (20 points)

**Task:** Implement a function that filters out TV shows based on a specified criterion/filter.
Then call that function to filter out various sublists from `cleaned_tv_shows`.

1. First, implement the function named `filter_list()`. The function filters a list based on a
   specified filtering criteria. The function is provisioned with three (`3`) parameters in the
   following order:

   - `list_` (`list`): A list of lists.
   - `filter` (`str`): A string value that the function will use to filter the list. It will be
      compared against an element within each nested list.
   - `filter_idx` (`int`): This represents the index of the nested list element you want to filter
      by. The function will check the value at this index in each nested list.

   **Requirements**

   1. Inside the function block, assign an empty list to a variable named `filtered_shows`. This list will
      store the nested lists that meet the `filter` condition.

   2. Next, utilize a `for` loop that iterates over an instance of the `range()` function. Instantiate
      the `range()` object with a stop value equal to the length of `list_`. Inside the loop block,
      write code to perform the following operations:

      1. Write a conditional `if` statement that performs a **_case-insensitive_ equality check** to
         determine whether or not the the `filter` matches the nested list element at position `filter_idx`.
      2. If the value at `filter_idx` in the nested list matches the `filter`, append the entire nested
         list to `filtered_shows`.

         :exclamation: You _must_ perform a _case-insensitive_ equality check **within** the `if`
         condition.

   3. Outside the loop block, return the updated `filtered_shows` list.

2. Now let's put our function to the test. First, we will filter out TV shows which have `"scifi"` as
   their genre. Within `main()`, assign an empty list to a variable named `scifi_tv_shows`.

3. Next, call the `filter_list()` function and pass to it the `cleaned_tv_shows` list, the filter
   string `"scifi"`, and the index position within each nested list of `cleaned_tv_shows` that
   corresponds with the genre. Assign the return value of the function call to `scifi_tv_shows`.

4. Uncomment the associated `assert` and `print()` statements, run your code, and confirm that the
   lists are equal.

5. Now we will try to filter out TV shows from `"2024"` that have `"netflix"` as the streaming platform.
   We will accomplish this in two filtering steps.

   1. First, call the `filter_list()` function and pass to it the `cleaned_tv_shows` list, the filter
      string `"netflix"`, and the index position within each nested list of `cleaned_tv_shows` that
      corresponds with the the Streaming Platform. Assign the return value of the function call to
      `netflix_tv_shows`.

   2. Then, call the `filter_list()` function again. This time pass to it the `netflix_tv_shows` list,
      the filter string `"2024"`, and the index position within each nested list of `cleaned_tv_shows`
      that corresponds with the Year of Release. Assign the return value of the function call to
      `netflix_new_tv_shows`.

6. Uncomment the associated `assert` and `print()` statements, run your code, and confirm that the
   lists are equal.

## Problem 03 (10 points)

**Task:** Leverage the `filter_list()` function to compute a sublist of `cleaned_tv_shows` that has
`crime` as the genre. Then utilize list indexing to capture only the Show Name, Year of Release, and
the Rotten Tomatoes Rating of each crime show.

1. Within `main()` assign an empty list to a variable named `crime_tv_shows`.

2. Next, call the `filter_list()` function and pass to it the `cleaned_tv_shows` list, the filter
   string `"crime"`, and the index position within each nested list of `cleaned_tv_shows` that
   corresponds with the genre. Assign the return value of the function call to `crime_tv_shows`.

3. Finally, we will focus on capturing only the Show Name, Year of Release, and the Rotten Tomatoes
   Rating of each show in `crime_tv_shows`. Initialize a new empty list called `crime_tv_shows_focused`.

4. Implement a standard `for` loop that iterates over `crime_tv_shows`. Inside the loop block,
   utilize a single list slicing expression to capture only the Show Name, Year of Release, and the Rotten Tomatoes
   Rating of each crime show and append it to `crime_tv_shows_focused`.

   :exclamation: You must achieve this in a single line of code.

5. Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
   the lists are equal.

## Problem 04 (10 points)

**Task:** Group TV shows into two different categories by iterating over `cleaned_tv_shows` to find
those streamed by Hulu versus those streamed by other platforms.

1. Create an empty list named `select_content` and another empty list named `non_select_content`.

2. Use a `for` loop that iterates over an instance of the `range()` function. Instantiate
   the `range()` object with a stop value equal to the length of `cleaned_tv_shows`. Inside the loop
   block write code that implements the following operations:

   1. Employ `if-else` conditional statements and a **_case-insensitive_** equality check to determine
      if the TV show being evaluated is streaming on Hulu.

      :exclamation: You _must_ perform a _case-insensitive_ equality check **within** the `if`
      condition.

   2. If the conditional statement evaluates to `True`, append the list representation of the show
      to `select_content`.

   3. Otherwise, append the list representation of the show to `non_select_content`.

## Problem 05 (15 points)

**Task:** Sum up the Rotten Tomatoes Ratings across all shows in `cleaned_tv_shows`. Then compute the
average Rotten Tomatoes Rating across all TV shows.

1. Assign a sensible starting value to the variable `total_rotten_tomato_ratings`.

2. Using a standard `for` loop, iterate over `cleaned_tv_shows`. Inside the loop block write code
   that implements the following operations:

   1. Add the Rotten Tomatoes Rating for each show to `total_rotten_tomato_ratings`.

3. Outside the loop block, compute the average Rotten Tomatoes Rating across all TV shows using
   `total_rotten_tomato_ratings`. Use the built-in function `round()` to round the average to one
   (`1`) decimal place and assign the rounded average to `avg_rotten_tomato_ratings`.

   :bulb: To find the average, divide the total ratings by the number of TV shows. You can get
   the total number of shows using the `len()` function on `cleaned_tv_shows`.

## Problem 06 (20 points)

**Task:** Accumulate lists of above-average, average, and below-average rated TV shows by iterating
over the `cleaned_tv_shows` list.

1. Create an empty list named `above_avg_rotten_tomato_rating_shows`, another empty list named
   `avg_rotten_tomato_rating_shows`, and a final empty list named `below_avg_rotten_tomato_rating_shows`.

2. Using a standard `for` loop, iterate over `cleaned_tv_shows`. Inside the loop block write code
   that implements the following operations:

   1. Employ conditional `if-elif-else` statements to determine whether or not the TV show being
      evaluated possesses a **Rotten Tomatoes rating** that is _greater than_, _equal to_, or
      _less than_ the `avg_rotten_tomato_ratings` variable.

   2. For the first conditional statement, if the Rotten Tomatoes rating is _greater than_ the
      `avg_rotten_tomato_ratings`, append the **show name** to `above_avg_rotten_tomato_rating_shows`.

   3. For the second conditional statement, if the Rotten Tomatoes rating is _equal to_ the
      `avg_rotten_tomato_ratings`, append the **show name** to `avg_rotten_tomato_rating_shows`.

   4. For the final conditional statement, append the **show name** to
      `below_avg_rotten_tomato_rating_shows`.

   :exclamation: Note that for each condition, you must only append the **show name** to the relevant
   list.

## Problem 07 (15 points)

**Task:** Find the oldest show by implementing a function that uses a `for` loop and an
`if` statement.

1. Implement the function named `get_oldest_show()`. The function is provisioned with a single
   parameter:

   - `list_` (`list`): A list of lists.

   **Requirements**

   1. Inside the function block, create two variables named `min_year` and `oldest_show`. Assign
      them reasonable starting values.

      :bulb: Start `min_year` with a value that is larger than any possible year in your list to
      ensure any year found will be smaller.

   2. Using a standard `for` loop, iterate over the TV shows in `list_`. Inside the loop block,
      write code that implements the following operations:

      1. Create a variable named `year` and assign it the **Year of Release** of the current show
         by accessing the year value using list indexing. Convert it from type `str` to type `int`.

         :exclamation: You must assign the `year` value **and** convert its type in a single line of
         code.

      2. Then, employ an `if` statement that evaluates whether or not `year` is less than `min_year`.

      3. If the conditional statement evaluates to `True`, assign `year` to `min_year` and assign
         **only the name of the show** to `oldest_show`.

      4. Outside of the loop block, return the `oldest_show` variable.

2. Within `main()`, call the `get_oldest_show()` function and pass to it the `cleaned_tv_shows` list.
   Assign the return value in a variable named `oldest_show`.

## Problem 08 (15 points)

**Task:** Accumulate a list of all genres that appear in `cleaned_tv_shows` with no duplicates.

1. Implement the function named `get_unique_elements()`. The function is provisioned with two (`2`)
   parameters:

   - `list_` (`list`): A list of lists.
   - `idx` (`int`): The index position within each nested list of `list_` that corresponds with any
      interested element.

   **Requirements**

   1. Inside the function block, create an empty list named `unique_elements`.

   2. Then, utilize a `for` loop that iterates over an instance of the `range()` function.
      Instantiate the `range()` object with a stop value equal to the length of `list_`. Inside the
      loop block, write code that implements the following operations:

      1. Write an `if` statement that evaluates whether or not a show's element at index position
         `idx` is a member of the `unique_elements` list.
         To do this, you must perform a **_case insensitive_** comparison with the list elements.

         :exclamation: You _must_ perform a _case-insensitive_ comparison **within** the `if`
         condition

      2. If the show's element at index `idx` is **not a member** of the `unique_elements` list,
         append it to the `unique_elements` list.

         :bulb: Note that certain show elements may be case sensitive (e.g. "Crime" and "crime"). Make sure to **also** utilize the appropriate `str` method when appending the show element to the `unique_elements` list to
         ensure that the string appended to the `unique_elements` list is lowercase.

2. Within `main()`, call the `get_unique_elements()` function and pass to it the `cleaned_tv_shows`
list and the index position within each nested list of `cleaned_tv_shows` that corresponds with the
**genre**. Assign the return value to a variable named `genres`.

3. Uncomment the associated `assert` and `print()` statements, run your code, and confirm that
   the lists are equal.
