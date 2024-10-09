# SI 506: Problem Set 02

## This week's Problem Set

This week's problem set includes six (6) problems that focus on strings, lists, string/list
operations, and using the `main()` function.

:bulb: As you work through the problem set make use of the commented out `print()` function calls
and `assert` statements to check your work.

## Reference

- ["Python Built-in Functions"](https://www.w3schools.com/python/python_ref_functions.asp)
- ["Python Operators"](https://www.w3schools.com/python/python_operators.asp)
- ["Python List Methods"](https://www.w3schools.com/python/python_lists_methods.asp)
- ["Python String Methods"](https://www.w3schools.com/python/python_ref_string.asp)

## Background

The University of Michigan offers numerous well-being resources. UMSI-suggested options are
described in the SI 506 [Syllabus](https://si506.org/syllabus/). For a more comprehensive collection
of resources visit U-M's [Well-Being Collective](https://wellbeing.umich.edu/).

## 1.0 Problem 01 (15 Points)

**Task:** Create a list of well-being resources, then create sublists for different categories of
resources.

1. You have been provided with a string constant named `WELLBEING_RESOURCES`. The string is
   expressed across multiple lines (note the surrounding parentheses `(...)`). Review each
   well-being resource and observe which character(s) delineate (i.e., separate) each resource.
   Within `main()`, call the appropriate string method to return a list of resource
   elements. Assign the return value of the method call to a variable named `resources`.

2. Employ **slicing** to access the **first three elements** of `resources`. Assign the new list to
   a variable named `academic`.

   :exclamation: You are limited to writing a single statement that includes the required slicing
   expression.

3. Employ **slicing** to access the **fourth and fifth elements** of `resources`. Assign the new
   list to a variable named `health`.

   :exclamation: You are limited to writing a single statement that includes the required slicing
   expression.

4. Employ **negative slicing** to access the **sixth, seventh, and eighth elements** of `resources`.
   Assign the new list to the variable named `marginalized_comm`.

   :exclamation: You are limited to writing a single statement that includes the required slicing
   expression.

5. Employ **negative slicing** to access the **last two elements** of `resources`. Assign the new
   list to a variable named `community`.

   :exclamation: You are limited to writing a single statement that includes the required slicing
   expression.

## 2.0 Problem 02 (22 Points)

**Task:** Update some of your well-being resource lists with additional resources using various list
methods.

1. Within `main()`, call the appropriate `list` method to extend the list `health` with the list
   `addl_health_resources`.

   :exclamation: Uncomment the associated `assert` statement, run your code, and confirm that the
   lists are equal.

2. Call the appropriate `list` method to add `embedded_caps` as the **last element** of the `health`
   list.

3. Call the appropriate `list` method to insert `mesa` as the **third element** of the
   `marginalized_comm` list.

4. Mutate each element in `addl_academic_resources` by concatenating the associated telephone number
   found in `addl_academic_resource_numbers` (combine the elements by position: `0` with `0`;
   `1` with `1`).

   :bulb: Access each element, concatenate, and assign the new string element to the appropriate
   element in `addl_academic_resources`.

   :exclamation: Make sure that you **modify** each  element of the existing `addl_academic_resources`, rather than creating a new list or reassigning the entire list variable.

   :exclamation: Uncomment the associated `assert` statement, run your code, and confirm that the
   lists are equal.

5. Call the appropriate `list` method to extend the list `academic` with `addl_academic_resources`.

   :exclamation: Uncomment the associated `assert` statement, run your code, and confirm that the
   lists are equal.

## 3.0 Problem 03 (16 Points)

**Task:** Sort some of your resource sublists using various list methods. Create an additional list
of well-being resources based on the `health` list.

1. Within `main()`, call the appropriate list method to **remove** the element `Spectrum Center|734-763-4186`
   from `marginalized_comm`.

2. Call the appropriate list method to sort the `health` elements in _ascending_ order.

3. Call the appropriate list method to sort the order of `academic` elements in _descending_ order.

   :bulb: Be sure to pass the required argument to the appropriate list method to sort the list in descending order.

4. Calling the appropriate `health` list method, return the index value of
   `UMSI Embedded CAPS Psychologist|Ashley Evearitt`. Assign the index value to the variable
   `umsi_caps`.

5. Employ **slicing** to access the `health` elements `UMSI Embedded CAPS Psychologist|Ashley Evearitt`
   and `University Health Service (UHS)|734-764-8320` using **positive indices**. Note that you
   _must_ use the `umsi_caps` index value in your slicing expression. Assign the new list to a
   variable named `student_focused_health_resources`.

   :exclamation: You are limited to writing a single statement that utilizes `umsi_caps` in the
   slicing expression.

## 4.0 Problem 04 (13 Points)

**Task:** Create lists and access values using slicing.

1. Within `main()`, employ **slicing** to access every element in `health` that is assigned an
   **odd number** index (i.e., `1`, `3`, ...). Assign the new list to a variable called
   `odd_index_health`.

   :bulb: Recall that Python's slice notation contains an optional `step` value.

2. Employ **negative slicing** to access the `academic` list's
   **2nd, 3rd and 4th elements in _reverse_ order**. Assign the new list to a variable named
   `academic_sub_list`.

   :exclamation: Uncomment the associated `assert` statement, run your code, and confirm that the
   lists are equal.

3. Employ **negative slicing** to reverse the list `marginalized_comm`. Assign the new list to a
   variable called `marginalized_comm_reversed`.

   :exclamation: You _must_ employ slicing **not** the `list.reverse()` method.

## 5.0 Problem 05 (17 Points)

**Task:** Implement a function that can move a list element from one position to another.

1. Implement the function `move_element()`. The function is provisioned with three parameters:

   - `list_` (`list`): The list containing the element to move.
   - `current_position` (`int`): The target element's current position.
   - `new_position` (`int`): The target element's new position (default index = `0`).

   **Requirements**

   1. Employ two list methods and pass one method to another to accomplish the task. Use the
      `current_position` and `new_position` indices to specify the element to move and the position
      to which it _must_ be moved. The expression you write to mutate the list is limited to
      a **single line of code**.

   2. After mutating the passed in `list_` add a second line of code to return the list to the
      caller.

2. After implementing the function, navigate to `main()`. Call the function `move_element()` and
   pass it the arguments required to move the **last element** in `health` to the **first position**
   in the list. Pass _minimum arguments required_ to accomplish the task.

   :exclamation: Uncomment the associated `assert` statement, run your code, and confirm that the
   lists are equal.

3. Call the function again. This time, move the **third element** in `health` to the
   **second to last position** in the list. When calling the function you _must_ adhere to the
   following requirements:

   1. You _must_ pass **three keyword arguments** to the function.
   2. The keyword arguments _must_ be passed in **reverse** order (i.e., the reverse of the
      function's defined parameter order).
   3. One of the indices that you pass as an argument _must_ be a **negative** number.

   :bulb: Decompose problem `5.3` into subproblems. First, figure out the arguments you need to pass
   to the function `move_element()` to change the order of the list elements. Second, convert the
   arguments to keyword arguments. Third, reorder the keyword arguments as specified above.

   :exclamation: Uncomment the associated `assert` statement, run your code, and confirm that the
   lists are equal.

## 6.0 Problem 06 (17 points)

**Task:** Implement a function that modifies a list element of type `str` by splitting the string
into a list of substring elements in order to construct a new string that replaces an organization's
telephone number with an email address.

1. In `main()` **uncomment** the `print()` function call that outputs the `academic` list.
   **Run your code** and review the list elements.

   Note the two pieces of information stored in each string element and, in particular, determine
   the character that is used to **separate** each piece of information. You will need to pass the
   character (known as a delimiter or separator) as an argument when calling the function that you
   implement below.

2. Next, implement the function `modify_element()`. The function is provisioned with four parameters:

   - `list_` (`list`): The list containing the element to modify.
   - `element` (`str`): The element in the list targeted for modification.
   - `email` (`str`): Organization's primary email address.
   - `delimiter` (`str`): The delimiter or separator used to split the element into a list of
     substrings (default delimiter = `","`).

   **Requirements**

   Break the problem of implementing the function block into a series of subproblems to solve.

   1. Inside the function block, use the `list.index()` method to locate the position of the
      `element` within `list_`. Assign the index returned to a local variable named `source_idx`.

   2. Next, work with the passed in `element`, and `delimiter` arguments. Create an expression that
      splits `element` into a list of substrings by passing `delimiter` to the appropriate
      string method to effect the split. Assign the new list returned by the method call to a
      local variable named `substrings`.

   3. Create an expression that **concatenates** the following three strings into a new string:

      1. The organization name. Access the name in `substrings` using indexing.
      2. The passed in `delimiter` value.
      3. The passed in `email` address.

      Adopt the following format and assign the new string to a local variable named `string`:

      ```python
      string = "< organization name >< delimiter >< email address >"
      ```

   4. Replace the "parent" string element in `list_` that was used to create `substrings` by
      assigning `string` to it.

      :bulb: When assigning `string` to the "parent" element in `list_` employ the subscript
      operator `[]` in tandem with `source_idx` to identify the element.

   5. After modifying the list element, return the mutated `list_` to the caller.

3. After implementing the function, return to `main()`. Call the function `modify_element()`. The
   goal is to replace the element

   `"Services for Students with Disabilities (SSD)|734-763-3000"`

   with

   `"Services for Students with Disabilities (SSD)|ssdoffice@umich.edu"`

   Pass all arguments **by position** including the email address "ssdoffice@umich.edu" and the
   appropriate delimiter value.

   Assign the return value of the the function call to the variable named `academic_ssd`.

   :exclamation: Uncomment the associated `assert` statement, run your code, and confirm that the
   lists are equal.

4. Call the function a second time. This time, modify the element
   `"Office of the Ombuds|734-763-3545"` in the `academic` list. The goal is to mutate the element
   by replacing the Ombuds' telephone number with the email address "umstudentombuds@umich.edu".

   :exclamation: When calling the function, you _must_ pass **keyword arguments** in **reverse**
   order (i.e., the reverse of the function's defined parameter order).

   Assign the return value of the the function call to the variable named `academic_ombuds`.

   :exclamation: Uncomment the associated `assert` statement, run your code, and confirm that the
   lists are equal.
