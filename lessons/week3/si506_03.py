# SI 506 Week 03: Spam, main(), optional params, keyword args, indexing, slicing, and Spam

from pprint import pprint  # import statement

# Constant
INQUISITION = """Nobody expects the Spanish Inquisition.
Our chief weapon is surprise.
Surprise and fear.
Fear and surprise.
Our TWO weapons are fear and surprise ... and ruthless efficiency.
Our THREE weapons are fear and surprise and ruthless efficiency ... and an almost fanatical devotion to the pope.
Uh! FOUR. No.
Amongst our weapons ....
Amongst our weaponry are such elements as fear, su -- I'll come in again.
"""

MENU = """Egg and bacon
Egg, sausage and bacon
Egg and Spam
Egg, bacon and Spam
Egg, bacon, sausage and Spam
Spam, bacon, sausage and Spam
Spam, egg, Spam, Spam, bacon and Spam
Spam, Spam, Spam, egg and Spam
Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam
Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top and Spam
"""

NEW_MENU = [
    "egg and bacon",
    "egg, toast, and bacon",
    "egg and spam",
    "egg, bacon and spam",
    "egg, bacon, toast, and spam",
    "spam, bacon, toast, and spam",
    "spam, egg, spam, spam, bacon and spam",
    "spam, spam, oatmeal, egg and spam",
    "spam, spam, oatmeal, spam, spam, oatmeal, baked beans, spam, spam, oatmeal and spam",
    "belgian waffles, whipped cream, fruit, and spam",
]

MINI_MENU = [
    "egg and bacon",
    "egg, bacon, toast, and spam",
    "egg, bacon, sausage, tomatoes, mushrooms, baked beans, toast, and spam",
    "veggie omelette, home fries, toast, and spam",
    "baked beans, spam, spam, oatmeal and spam",
]


def calculate_sale_price(price, quantity, discount):
    return quantity * price * (1 - discount)  # pass in .15 for 15% discount


def calculate_sale_price_v1p1(price, quantity=1, discount=0.0):
    return quantity * price * (1 - discount)  # pass in .15 for 15% discount


def calculate_sale_price_v1p2(price, quantity=1, discount=0.0, sales_tax=0.0):
    purchase_price = quantity * price * (1 - discount)  # pass in .15 for 15% discount
    return purchase_price + (purchase_price * sales_tax)


def main():
    # 4.0 FUNCTIONS: OPTIONAL PARAMETERS AND KEYWORD ARGUMENTS

    # 4.1 Optional parameters

    # Supermarket list price
    eggs = 2.59  # Kroger Grade A Large Eggs 12 ct
    bacon = 6.49  # Jimmy Dean Applewood Smoked Bacon 12 oz
    sausage = 3.79  # Kroger Original Breakfast Sausage 12 oz
    baked_beans = 2.79  # Busch's Baked Beans 28 oz
    spam = 4.19  # Spam Classic 12 oz

    # NOTE: Non-function examples
    item_01 = 12*eggs  # TODO price 12ct eggs
    print(f"\n4.1.1 Eggs price = ${item_01:.1f}")

    item_02 = None  # TODO price 2 packages of bacon
    # print(f"\n4.1.2 Bacon price = ${item_02:.2f}")

    # Apply discount
    item_03 = None  # TODO one package of sausage discounted 0.34 (34%)
    # print(f"\n4.1.3 Sausage price (discount) = ${item_03:.2f}")

    # Call function (all three arguments required)
    item_04 = None  # TODO One can of baked beans (no discount)
    # print(f"\n4.1.4 Baked Beans price = ${item_04:.2f}")

    item_05 = None  # TODO Two cans of spam (discount)
    # print(f"\n4.1.5 Spam price (discount) = ${item_05:.2f}")

    # Add optional parameters
    item_06 = None  # TODO One can of baked beans (no discount)
    # print(f"\n4.1.6 Baked Beans price = ${item_06:.2f}")

    item_07 = None  # TODO Two cans of spam (discount)
    # print(f"\n4.1.7 Spam price (no discount) = ${item_07:.2f}")

    # 4.2 Keyword arguments

    # Keyword arguments passed in reverse order
    # TODO Uncomment
    # item_08 = calculate_sale_price_v1p1(None, None, None) # One can of spam (no discount)
    # print(f"\n4.2 Spam price (discounted) = ${item_08:.2f}")

    # 4.3 Skipping optional parameters

    # Quantity not specified, keyword arg used to specify discount
    # TODO Uncomment
    # item_09 = calculate_sale_price_v1p1(None, None)  # One can of spam (discount)
    # print(f"\n4.3.1 Spam price (discount) = ${item_09:.2f}")

    # ERROR: If quantity not specified, discount treated as quantity
    # TODO Uncomment
    # item_09 = calculate_sale_price_v1p1(spam, 0.0475)
    # print(f"\n4.3.2 Spam price (discount) = ${item_09:.2f}")

    # 4.1 CHALLENGE 01

    total_cost = None  # TODO call function
    print(f"\n4.5.1 Spam x 3 (taxed) = ${total_cost:.2f}")

    ## 5.0 WORKING WITH SEQUENCES

    # String
    comedy_series = "Monty Python"
    comedy_series_len = len(comedy_series)  # Returns length (i.e., character count)
    print(f"\n5.0.1 comedy series (n={comedy_series_len}) = {comedy_series}")

    # TODO: Uncomment immutability check
    # comedy_series[0] = 'm'  # TypeError: 'str' object does not support item assignment

    # List
    pythons = ["Graham Chapman", "John Cleese", "Terry Jones", "Eric Idle", "Michael Palin"]
    pythons_len = len(pythons)  # Return the length
    # print(f"\n5.0.2 pythons (n={pythons_len}) = {pythons}")

    # Mutate the list (in-place)
    # TODO Uncomment
    # pythons.append(None)  # TODO Add "Terry Gilliam"

    pythons.insert(-1, "Terry Gilliam")  # Alternative
    # pythons.extend(["Terry Gilliam"])  # Alternative
    print(f"\n5.0.3 pythons (n={len(pythons)}) = {pythons}")

    # TODO Uncomment
    # pythons.insert(None, None)  # TODO Have fun (move Terry)
    # print(f"\n5.0.4 pythons (n={len(pythons)}) = {pythons}")

    pythons_all = None  # TODO Add Neil Innes via list concatenation (new list)
    # print(f"\n5.0.5 pythons_all (n={len(pythons_all)}) = {pythons_all}")

    # Tuple
    silly_walks = ("Monty Python", "Sketch", "The Ministry of Silly Walks", "15 September 1970")
    silly_walks_len = len(silly_walks)  # Return the length
    # print(f"\n5.0.6 silly walks (n={silly_walks_len}) = {silly_walks}")

    python_theme_song = None  # Add single item tuple (note trailing comma)
    # print(f"\n5.0.7 Python theme song = {python_theme_song}")

    # TODO Uncomment
    # sousa_tune = (
    #     ("John Philip Sousa", "Composer") + python_theme_song + (1893,)
    # )  # tuple concatenation
    # print(f"\n5.0.8 Sousa tune (n={len(sousa_tune)}) = {sousa_tune}")

    holy_grail = (
        "Monty Python and the Holy Grail",
        1975,
        [
            "Arthur, King of the Britons",
            "Sir Lancelot the Brave",
            "Sir Bedevere the Wise",
            "Sir Galahad the Pure",
        ],
    )

    # TODO Uncomment
    # holy_grail[1] = '3 April 1975' # Triggers exception
    # holy_grail[2] = ["Arthur", "Lancelot", "Bedevere", "Galahad", "Patsy"]  # Triggers exception
    # holy_grail[2].append("Patsy")  # Mutates list item with a new element
    # print(f"\n5.0.9 Holy Grail (n={len(holy_grail)}) = {holy_grail}")

    # 5.1 Creaitng a list from a string

    # 5.1.1 str.split()

    sketch_comedy = "Monty Python's Flying Circus"
    words = None  # TODO Split string
    # print(f"\n5.1.1.1 Split title (n={len(words)}) = {words}")

    sketch_titles = "Dead Parrot Sketch, The Spanish Inquisition, The Argument Clinic"
    sketches = None  # TODO Split string with separator
    # print(f"\n5.1.1.2 sketches (n={len(sketches)}) = {sketches}")

    sketches = sketch_titles.split(", ", maxsplit=1)
    # print(f"\n5.1.1.3 Split sketches (n={len(sketches)}, maxsplit=1) = {sketches}")

    # 5.1.2 str.splitlines()

    dialogue = None  # TODO Split INQUISITION
    # print(f"\n5.1.2.1 Cardinal Ximinez (n={len(dialogue)}) = {dialogue}")

    dialogue = None  # TODO Split INQUISITION with keepends=True
    # print(f"\n5.1.2.2 Cardinal Ximinez (n={len(dialogue)}, keepends=True) = {dialogue}")

    # 5.2.1 CHALLENGE 02

    arthur = (
        "The Lady of the Lake, "
        "her arm clad in the purest shimmering samite, "
        "held aloft Excalibur from the bosom of the water "
        "signifying by Divine Providence that "
        "I, Arthur, was to carry Excalibur. "
        "That is why I am your king."
    )

    dennis = (
        "Listen, strange women lying in ponds distributing swords "
        "is no basis for a system of government. "
        "Supreme executive power derives from a mandate from the masses, "
        "not from some farcical aquatic ceremony."
    )

    excalibur = None

    # print(f"\n5.2.1 Arthur and Dennis (n={len(excalibur)}) = {excalibur}")

    ## 6.0 INDEXING

    # 6.1 Accessing a character by position

    name = "Monty Python"
    letter = None  # TODO first letter (zero-based index)
    # print(f"\n6.1.1 Letter = {letter}")

    letter = None  # TODO 5th letter (zero-based index)
    # print(f"\n6.1.2 Letter = {letter}")

    letter = None  # TODO last letter (negative index)
    # print(f"\n6.1.3 Letter = {letter}")

    # 6.2 Index operator (list)

    # Create a new menu list
    menu = MENU.splitlines()
    # print(f"\n6.2.0 Menu (n={len(menu)}) = {menu}")

    menu_item = None  # TODO 2nd menu item
    # print(f"\n6.2.1 2nd menu item = {menu_item}")

    menu_item = None  # TODO 2nd to last menu item
    # print(f"\n6.2.2 2nd to last menu item = {menu_item}")

    # 6.3 Mutating a list element using indexing

    menu[3] = "Scrambled eggs, bacon and Spam"
    # print(f"\n6.3 Scrambled eggs added to menu = {menu}")

    # Trigger an IndexError exception
    # menu_item = menu[10] # IndexError: list index out of range#

    # 6.4.1 CHALLENGE 04

    # NOTE: Review output
    # print(f"\n6.4.1 menu (n={len(menu)}) = {menu}")

    menu_item = None  # TODO first element with 2 helpings of spam
    # print(f"\n6.4.2 menu_item = {menu_item}")

    # TODO Uncomment
    # assert menu_item == "Spam, bacon, sausage and Spam"  # Assert equality

    ## 7.0 SLICING

    cast = [
        "Terry Jones, Waitress",
        "Eric Idle, Mr Bun",
        "Graham Chapman, Mrs Bun",
        "John Cleese, The Hungarian",
        "Michael Palin, Historian",
        "Extra, Viking 01",
        "Extra, Viking 02",
        "Extra, Viking 03",
        "Extra, Viking 04",
        "Extra, Viking 05",
        "Extra, Viking 06",
        "Extra, Police Constable",
    ]

    # 7.1 Slicing start/end range (index 0 to index n, stride = 1)

    # Return Mr and Mrs Bun
    cast_members = None  # TODO slice
    # print(f"\n7.1.1 The Buns = {cast_members}")

    # Return Mr and Mrs Bun (negative slice)
    named_cast_members = None  # TODO negative slice
    # print(f"\n7.1.2 The Buns (negative slice) = {named_cast_members}")

    # Slice from index 0 to index n (stride = 1)
    named_cast_members = None  # TODO slice
    # print(f"\n7.1.3 Named cast members = {named_cast_members}")

    # Slice from index -n to end of list inclusive (stride = 1)
    unnamed_cast_members = None  # TODO slice
    # print(f"\n7.1.4 Extras = {unnamed_cast_members}")

    # 7.2 Working with stride values

    cast = [
        "Terry Jones, Waitress",
        "Eric Idle, Mr Bun",
        "Graham Chapman, Mrs Bun",
        "John Cleese, The Hungarian",
        "Michael Palin, Historian",
        "Extra, Viking 01",
        "Extra, Viking 02",
        "Extra, Viking 03",
        "Extra, Viking 04",
        "Extra, Viking 05",
        "Extra, Viking 06",
        "Extra, Police Constable",
    ]

    # Retrieve the late Terry Jones and Graham Chapman
    cast_members = None  # TODO slice
    # print("\n7.2.1 Deceased cast members\n")
    # pprint(cast_members)

    # Return cast members in reverse order
    cast_members = None  # TODO slice
    # print("\n7.2.2 Cast members reverse order\n")
    # pprint(cast_members)

    # Return every other cast member starting from the first element
    cast_members = None  # TODO slice
    # print("\n7.2.3 Every other cast member\n")
    # pprint(cast_members)

    # 7.3.1 CHALLENGE 05

    vikings = None  # TODO slice
    # print(f"\n7.3.1 Vikings = {vikings}")

    # TODO Uncomment
    # assert vikings == [
    #     "Extra, Viking 01",
    #     "Extra, Viking 02",
    #     "Extra, Viking 03",
    #     "Extra, Viking 04",
    #     "Extra, Viking 05",
    #     "Extra, Viking 06",
    # ]

    # 7.3.2 CHALLENGE 06

    # Return every other Viking starting with Viking 01.
    cast_members = None  # TODO slice
    # print("\n7.3.2.1 Every other Viking\n")
    # pprint(cast_members)

    # BONUS. Return every other Viking starting with Viking 01 in reverse order.
    cast_members = None  # TODO slice
    # print("\n7.3.2.2 Every other Viking reverse order \n")
    # pprint(cast_members)

    # Workaround
    cast_members = None  # TODO slice
    # print("\n7.3.2.3 Every other Viking reverse order workaround\n")
    # pprint(cast_members)

    # TODO Uncomment
    # assert cast_members == ["Extra, Viking 06", "Extra, Viking 04", "Extra, Viking 02"]

    ## 8.0 ADDITIONAL STRING AND LIST METHODS

    # 8.1 Select string methods

    # 8.1.1 str.find()

    menu_item = menu[6]  # "Spam, egg, Spam, Spam, bacon and Spam"

    idx = menu_item.find("Spam")
    # print(f"\n8.1.1.1 'Spam' index (first instance) = {idx}")

    idx = menu_item.rfind("Spam")
    # print(f"\n8.1.1.2 'Spam' index (last instance) = {idx}")

    idx = menu_item.find("ham")
    # print(f"\n8.1.1.3 'ham' index (first instance) = {idx}")

    # 8.1.2 str.index()

    idx = menu_item.index("bacon and Spam")
    # print(f"\n8.1.2.1 Index position = {idx}")

    idx = menu_item.rindex("Spam", 11, 21)  # Search within a range
    # print(f"\n8.1.2.2 Index position = {idx}")

    # WARN: Uncomment (triggers exception)
    # idx = menu_item.index("ham")  # ValueError: substring not found

    # 8.2 LIST METHODS

    menu_v2 = MENU.splitlines()  # Create a new list

    # 8.2.1 list.append() (in-place)

    # modify in-place (no variable assignment)
    # TODO Uncomment
    # menu_v2  # TODO Append
    # print("\n8.2.1 New menu item\n")
    # pprint(menu_v2, width=125)

    # 8.2.2 list.index()

    # TODO Uncomment
    # idx = menu_v2  # TODO Index
    # print(f"\n8.2.2 Index = {idx}")

    # 8.2.3 list.insert() (in-place)

    new_item = "blueberry pancakes, strawberry yogurt, and spam"
    # TODO Uncomment
    menu_v2  # TODO Insert 1st position
    # print("\n8.2.3 pancakes and yogurt added to the menu\n")
    # pprint(menu_v2, width=125)

    # 8.2.4 list.pop() (in-place)

    # TODO Uncomment
    # last_item = menu_v2  # TODO Pop last item
    # print("\n8.2.4.1 Last item removed\n")
    # pprint(last_item, width=125)

    # TODO Uncomment
    # first_item = menu_v2  # TODO Pop first item
    # print("\n8.2.4.2 First item removed\n")
    # pprint(first_item, width=125)

    # 8.2.5 list.remove() (in-place)

    item = menu_v2[-2]  # Lobster Thermidor
    # TODO Uncomment
    # menu_v2  # TODO Remove
    # print("\n8.2.5 Lobster Thermidor removed\n")
    # pprint(menu_v2, width=125)

    # Do not do this: items variable no longer points to a list object
    # TODO Uncomment
    # items = items.remove("bacon and Spam") # None is returned

    # 8.2.6 list.sort() (in-place)

    # TODO Uncomment
    # menu_v2  # TODO Sort
    # print("\n8.2.6.1 Menu sorted\n")
    # pprint(menu_v2, width=125)

    # TODO Uncomment
    # menu_v2  # TODO Sort (reverse)
    # print("\n8.2.6.2 Menu sorted (reverse)\n")
    # pprint(menu_v2, width=125)

    # 8.3.1 CHALLENGE 06

    new_item = "belgian waffles, whipped cream, fruit, and spam"

    new_menu = None
    # print(f"\n8.3.1.1 {new_menu}")
    new_menu = None
    # print(f"\n8.3.1.2 {new_menu}")

    # TODO: Continue to mutate < new_menu > per instructions

    # TODO Uncomment
    # print("\n8.3.1.7 new_menu\n")
    # pprint(new_menu, width=125)

    # TODO Uncomment (when new_menu is complete)
    # Assert equality
    # assert new_menu == NEW_MENU

    # 8.3.2 CHALLENGE 07

    # Select every other menu item
    mini_menu = None  # TODO slice
    # print(f"\n8.3.2.1 mini_menu (n={len(mini_menu)}) = {mini_menu}")

    # Return the index of "egg and spam"
    idx = None  # TODO call method
    # print(f"\n8.3.2.2 'egg and spam' index = {idx}")

    # Remove menu item using its index
    # TODO Uncomment
    # mini_menu  # TODO call method (ignore return value)
    # print(f"\n8.3.2.3 mini_menu (n={len(mini_menu)}) = {mini_menu}")

    # Replace the second to last menu item
    new_item = "egg, bacon, sausage, tomatoes, mushrooms, baked beans, toast, and spam"
    # TODO Uncomment
    # mini_menu[?] = None  # TODO Fix index; assign < new_item >
    # print(f"\n8.3.2.4 mini_menu (n={len(mini_menu)}) = {mini_menu}")

    # Insert new menu item in the 4th position
    new_item = "veggie omelette, home fries, toast, and spam"
    # TODO Uncomment
    # mini_menu  # TODO call method
    # print(f"\n8.3.2.5 mini_menu (n={len(mini_menu)}) = {mini_menu}")

    # Remove 2x "spam, spam, oatmeal, " from the last menu item
    # NOTE: last "spam, spam, oatmeal" retained (no trailing comma)
    menu_item = None  # TODO assign element
    idx = None  # TODO find "bake beans", return index
    # TODO Uncomment
    # mini_menu[?] = None  # TODO Fix index; assign < menu_item > SLICE

    # TODO Uncomment
    # print(f"\n8.3.2.6 mini_menu (id={id(mini_menu)}, len={len(mini_menu)})\n")
    # pprint(mini_menu, width=125)

    # TODO Uncomment (when mini_menu is complete)
    # assert mini_menu == MINI_MENU


if __name__ == "__main__":
    main()
