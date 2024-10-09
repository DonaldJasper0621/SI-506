# SI 506 Week 02: Everything is an object (and other preliminaries)

# 3.0 STATEMENTS AND EXPRESSIONS

# 3.1 Statement

office = "ALA Office for Intellectual Freedom"  # variable assignment

# 3.2 Expression

# Statements (variable assignments)
x = 2571
y = 4240

# Statement containing the arithmetic expression y - x
diff = y -x 

# Also an expression (function call)
print(f"\n3.2 diff ={diff}")

# TODO Uncomment
# print(f"\n3.2 diff = {diff}") # formatted string literal

# 4.0 COMMENTS

# TODO Uncomment
title = "Top 10 Most Challenged Books of 2023"  # TODO Uncomment
# print(f"\n4.0 title = {title}") f-string
print(f"this is title: {title}")

# 5.0 VARIABLES

# 5.2.1 Good

# Choose lowercase
title = "Beloved"

# Separate words with underscore (_)
banned_author = "Toni Morrison"

# Use plural form to indicate a set or sequence
banned_titles = ["The Bluest Eye", "Beloved", "Song of Solomon"]

# Ok to use recognizable abbreviations like num[ber], val[ue] or var[iable].
num = 1247

# "is_", "has_" prefix: Boolean True/False
is_banned = False
has_mask = True

# All caps designates a module level constant (special case)
BASE_URL = "https://www.ala.org/"


# Function definition specifying two parameters x and y
def add(x, y):
    return x + y  # arithmetic expression

print(add(3,2))

# For loop incorporating a counter < i > value
i = 1  # counter
for title in banned_titles:
    print(f"{i}. {title}") # TODO Uncomment
    i += 1  # addition assignment (increment)

# 5.2.2 Bad (But Legal)

# Opaque
b = "Beloved"
sos = "Song of Solomon"

# Reserve CamelCase for class names, e.g. GraphicMemoir().
GraphicMemoir = "Gender Queer"  # restyle variable as graphic_memoir

# Not a fan of trailing data type suffixes (_list)
banned_authors_list = ["Maia Kobabe", "George M. Johnson", "Mike Curato"]

# Avoid use of built-in function names
# TODO Uncomment
id_1 = "12345"
print(id(id_1)) # TypeError: 'str' object is not callable; built-in function id() not recognized

# 5.2.3 Ugly (Illegal)

# Illegal: keyword used as a variable name (language-specific identifiers reserved by Python)
# TODO Uncomment
# class = "SI 506"

# Illegal: variable name commences with a numeric value.
# TODO Uncomment
# 506_lecture = "SI 506 lecture"

# Illegal: variable name includes a special character
# TODO Uncomment
# $number = 506
# domain@ = "umich.edu"

# Illegal: variable name includes a dash (`-`).
# TODO Uncomment
# course-list = ["SI 506", "SI 507", "SI 618"]

# Illegal: variable name includes a space.
# TODO Uncomment
# course name = "SI 506"

# 6.0 OPERATORS: BASIC ARITHMETIC

x = 5 / 2  # Floating point division
print(f"\n6.0.1 x = {x}")

x = 5 // 2  # Integer division
print(f"\n6.0.2 y = {x}")

y = 2 * (3 - 1)
# print(f"\n6.0.3 y = {y}")

z = (4 + 3) * (5 - 2)
# z = (4 + 3) * 5 - 2  # TODO Uncomment
# print(f"\n6.0.4 z = {z}")

# String concatenation
uniqname = "arwhyte"
domain = "umich"
email = uniqname + domain # TODO Replace with concatenated string
print(f"\n6.0.5 email = {email}")

# 6.1.1 CHALLENGE 01

# 3, 5, 7, 9
w = 3, 5, 7, 9
print(f"\n6.1.1.1 w = {w}")

# 2, 4, 8
x = 2,4,8
print(f"\n6.1.1.2 x = {x}")

y = 506//3
print(f"\n6.1.1.3 y = {y}")

z = 506%3
print(f"\n6.1.1.4 z = {z}")

# 6.1.2 CHALLENGE 02

author = "Maia Kobabe"
title = "Gender Queer: A Memoir"	
publisher = "Lion Forge Comics"
pub_date = "2019"

challenged_book = None
# print(f"\n6.1.2.1 challenged_book = {challenged_book}")

# TODO Copy challenged_book assignment above and modify

# print(f"\n6.1.2.1 challenged_book = {challenged_book}")

# 7.0 OBJECTS

# 7.1 NoneType

value = None

# 7.2.1 Numeric (int)

x = 4240
y = 0.65
z = -506

# 7.2.2 Numeric (float)

pi = 3.14159
corr_coeff = -0.85

# 7.3 bool

is_challenged = True
is_banned = False

# 7.4.1 String (str)

author = "Ellen Hopkins"
# print(f"\n7.4.1.1 author = {author}")

intro = """There can't be anyone, I am sure, who doesn't know what it
feels liked to be disliked, even rejected, momentarily or for sus-
tained periods of time. Perhaps the feeling is merely indiffer-
ence, mild annoyance, but it may also be hurt. It may even be
that some of us know what it is like to be actually hated--
hated for things we have no control over and cannot change. . . .
"""
print(f"\n7.4.1.2 intro = {intro}")

intro = (
    "There can't be anyone, I am sure, who doesn't know what it\n"
    "feels liked to be disliked, even rejected, momentarily or for sus-\n"
    "tained periods of time. Perhaps the feeling is merely indiffer-\n"
    "ence, mild annoyance, but it may also be hurt. It may even be\n"
    "that some of us know what it is like to be actually hated--\n"
    "hated for things we have no control over and cannot change. . . ."
)
print(f"\n7.4.1.3 intro = {intro}")

# 7.4.2 List (list)

challenged_books = ["Flamer", "Tricks", "Sold"]  # TODO Replace with list of book titles
# 7.4.3 Tuple (tuple)

municipality = ("45",8,"99")# TODO Replace with tuple
print(municipality)
city = None  # TODO single item
#dic
# imune = {"item":1,3 , "arer": 6}
# imune[0,]
# 7.5 Callable (function)

# 7.5.1 Defining and calling a user-defined function

# TODO define function

# Multiply 4 and 6
product = None  # TODO call function
# print(f"\n7.5.1.1 product = {product}")

# TODO define function

# Divide 10 by 2
quotient = None  # TODO call function
quotient = None  # TODO call function
# print(f"\n7.5.1.2 quotient = {quotient}")

# 7.5.2 Built-in functions

# 7.5.2.1 print()
namu = .65
print(type(namu))
print(namu)
# Passing a hard-coded string.
# print("\nLibraries rock!")  # includes optional newline \n escape character

# Formatted string literal (combination of characters and variables)
library = "University of Michigan Library"
url = "https://www.lib.umich.edu/"

# TODO Call print() pass f-string

# 7.5.2.2 type()

challenge_count = 4240  # unique titles
count_type = None  # TODO call function
# print(f"\n7.5.2.2.1 challenge_count type = {count_type}")

url = "https://www.ala.org/bbooks/frequentlychallengedbooks/top10"
url_type = None  # TODO call function
# print(f"\n7.5.2.2.2 url type = {url_type}")

# 7.5.2.3 len()

char_count = None  # TODO call function; count characters in URL
# print(f"\n7.5.2.3.1 char_count = {char_count}")

# States that lead in book banning (2022-2023)
state_count = len(["Florida", "Missouri", "North Carolina", "Texas", "Utah"])
# print(f"\n7.5.2.3.2 states_count = {state_count}")

# 7.5.2.4 round()

tau = 6.28318530717958647692  # approximation
tau = None  # TODO Call function
# print(f"\n7.5.2.4.1 tau = {tau}")

tau = 6.28318530717958647692 # approximation
tau = None  # TODO Call function
# print(f"\n7.5.2.4.2 tau = {tau}")
# 7.6.1 CHALLENGE 03

titles = None  # TODO Replace with list of tuples

print(f"\n7.6.1 list[tuple] = {titles}")

# 7.6.2 CHALLENGE 04

# TODO define function

alaska = None  # TODO call function
sold = None  # TODO call function
bluest_eye = None  # TODO call function

total_mins = None  # Concatenate

# print(f"\n7.6.2 total_mins = {total_mins}")


# 8.0 OBJECT BEHAVIORS

# 8.1.1 str.capitalize()

event = "banned books week (22-28 September 2024)"
event = None  # TODO call method
# print(f"\n8.1.1 event = {event}")

# 8.1.2 str.lower(), str.upper()

title = "Beyond Magenta"
lower_case = None  # TODO call method
# print(f"\n8.1.2.1 lower_case = {lower_case}")

upper_case = title.upper()
# print(f"\n8.1.2.2 lower_case = {lower_case}")

# 8.1.3 str.startswith(), str.endswith()

title = "Out of Darkness"
starts_with_O = None  # TODO call method
# print(f"\n8.1.3.1 starts_with_O = {starts_with_O}")

ends_with_S = None  # TODO call method
# print(f"\n8.1.3.2 ends_with_S = {ends_with_S}")

# 8.1.4 str.count()

guid = "179e7cb5-cc25-4be8-8094-31c9095987e2"

char_count = None  # TODO call method
# print(f"\n8.1.4.1 char_count = {char_count}")

char_count = None  # TODO call method
# print(f"\n8.1.4.2 char_count = {char_count}")

char_count = None  # TODO call method
# print(f"\n8.1.4.3 char_count = {char_count}")

# 8.1.5 str.replace()

statement = (
    "The American Library Association condemns censorship "
    "and works to ensure free access to information."
)
statement = None  # TODO call method
# print(f"\n8.1.5 ALA statement = {statement}")

# 8.2.1 CHALLENGE 05

stamped = """BEFORE WE BEGIN, LET'S GET SOMETHING STRAIGHT. This is not a history book. I repeat,
this is not a history book. At least not like the ones you're used to reading in school. The ones
that feel more like a list of dates (there will be some), with an occasional war here and there, a
declaration (definitely gotta mention that), a constitution (that too), a court case or two, and, of
course, the paragraph that's read during Black History Month (Harriet! Rosa! Martin!). This isn't
that. This isn't a history book. Or, at least, it's not that kind of history book. Instead, what
this is, is a book that contains history. A history directly connected to our lives as we live
them right this minute. This is a present book. A book about the here and now. A book that hopefully
will help us better understand why we are where we are as Americans, specifically as our identity
pertains to race.
"""

book_count = None  # TODO call method
# print(f"\n8.2.1.1 book_count = {book_count}")

space_count = None  # TODO call method
# print(f"\n8.2.1.2 space_count = {space_count}")
space_part = None  # TODO divide
# print(f"\n8.2.1.3 space_part = {space_part}")

space_part = None  # TODO Call function
# print(f"\n8.2.1.4 space_part = {space_part}")

# 8.2.2 CHALLENGE 06

title = "Angie Thomas, The Hate You Give (Balzer + Bray, 2017)"  # contains a typo
# print(f"\n7.5 title (id={id(title)}) = {title}")  # includes object id

title = None  # TODO call method
# print(f"\n7.5 title (id={id(title)}) = {title}")  # includes object id

# 8.2.3 CHALLENGE 07

# TODO define function


surge_pct = None  # TODO call function
# print(f"\n8.2.3.1 surge_pct = {surge_pct}")

# Bonus: Copilot demo

# TODO prompt Copilot to format value

# print(f"\n8.2.3.2 surge_pct_01 = {surge_pct_01}")
