# START BONUS 02

from pprint import pprint  # import statement

print("BONUS CHALLENGE 02 \n")

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


def main():
    new_item = "belgian waffles, whipped cream, fruit, and spam"

    new_menu = MENU.lower()
    print(f"\n1.1 {new_menu}")

    new_menu = new_menu.replace("sausage", "toast,")
    print(f"\n1.2 {new_menu}")

    new_menu = new_menu.splitlines()  # or newmenu.split('\n)
    print(f"\n1.3 {new_menu}")

    new_menu.pop(-1)
    print(f"\n1.4 {new_menu}")

    new_menu = [item.replace("spam, spam, spam", "spam, spam, oatmeal") for item in new_menu]
    print(f"\n1.5 {new_menu}")

    new_menu.append("belgian waffles, whipped cream, fruit, and spam")
    print(f"\n1.6 {new_menu}")

    # TODO: Continue to mutate < new_menu > per instructions

    # TODO Uncomment
    print("\n1.7 new_menu\n")
    pprint(new_menu, width=125)

    # TODO Uncomment (when new_menu is complete)
    # Assert equality
    assert new_menu == [
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
    return new_menu  # WARN: DO NOT REMOVE


if __name__ == "__main__":
    main()

# END BONUS 02
