# SI 506: Working with files, variable scope, error handling, and iterable unpacking

import csv
import pprint

from pathlib import Path

RESNICK = "Resnick, Paul"  # global constant, global scope


def clean_data(publication):
    """Mutates the passed in < publication > list by converting numbers masquerading as
    strings to an integer (int).

    Checks each string element in the < publication > list. Delegates to the function
    < convert_to_int > the task of attempting to convert the target string to an integer.
    Strings that cannot be converted are returned unchanged.

    Parameters:
      publication (list): represents a publication

    Returns:
        list: mutated publication list
    """

    for i in range(len(publication)):
        publication[i] = convert_to_int(publication[i])
    return publication


def convert_to_int(value):
    """Attempts to convert a string, number or boolean value to an int. If
    a runtime ValueError exception is encountered, the function returns the
    value unchanged.

    Parameters:
        value (str|bool): string or boolean value to be converted

    Returns:
        int: if value successfully converted else returns value unchanged
    """

    try:
        return int(value)
    except ValueError:
        return value


def get_element(publication, headers, column_name):
    """Returns a < publication > list element by looking up its index value in
    the accompanying < headers > list using the < column_name > as the target
    header value.

    Parameters:
        publication (list): represents a publication
        headers (list): column names sourced from the first row of the CSV file
        column_name (str): provides header value used to look up the index value
                           of the target element

    Returns:
        str: element sourced from passed in publication list
    """

    return publication[headers.index(column_name)]


def get_citation_count_by_year(publications, headers, year):
    """Returns the annual citation count across all < publications > per
    the provided < year >. Delegates the task of accessing each publication's
    yearly citation count to the function < get_attribute >.

    Parameters:
        publications (list): nested list of publications
        headers (list): column names sourced from the CSV
        year (str): column name (e.g., '1995')

    Returns:
        int: citation count across all publications for a given year
    """

    count = 0
    # TODO Implement loop
    return count


def get_min_details(publication, headers, column_names):
    """Returns a slimmed down version of the < publication > list. Loops over < column_names >
    and delegates the task of extracting each target element to the function < get_element() >.
    Each extracted element is appended to the < details > list and returned to the caller.

    Parameters:
        publication (list): represents a publication
        headers (list): column names sourced from the CSV
        column_names (tuple): target column names

    Returns:
        list: slimmed down version of the < publication >
    """

    details = []
    for column_name in column_names:
        details.append(get_element(publication, headers, column_name))
    return details


def has_faculty_coauthor(author, coauthors, faculty):
    """Returns True if a coauthor in the < coauthors > list is a member of the < faculty > list.
    Otherwise, returns False. Note that the < author > is excluded from the search and each
    < coauthor > is stripped, lowercased, and then titled before the string and membership
    comparisons are performed.

    Parameters:
        author (str): author name
        coauthors (list): list of coauthors
        faculty (list): list of faculty members

    Returns:
        bool: True if author has a faculty coauthor, else False
    """

    for coauthor in coauthors:
        name = None  # TODO Implement
        # TODO Implement conditional statement
    return False


def read_csv(filepath, encoding="utf-8", newline="", delimiter=","):
    """Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
    may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested "row" lists
    """

    with open(filepath, "r", encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)
        return data


def read_file(filepath, encoding="utf-8", strip=True):
    """Read text file line by line. Remove whitespace and trailing newline
    escape character.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file.
        strip (bool): remove white space, newline escape characters

    Returns
        list: list of lines in file
    """

    with open(filepath, "r", encoding=encoding) as file_obj:
        if strip:
            data = []
            for line in file_obj:
                # data.append(line) # includes trailing newline '\n'
                data.append(line.strip())  # strip leading/trailing whitespace including '\n'
            return data
        else:
            return file_obj.readlines()  # list


def write_csv(filepath, data, headers=None, encoding="utf-8", newline=""):
    """Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    `\r\n` an extra `\r` will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence to be written to the target file
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)


def write_file(filepath, data, encoding="utf-8", newline=True):
    """Write content to a target file encoded as UTF-8. If optional newline is specified
    append each line with a newline escape sequence (`\n`).

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence of strings comprising the content to be written to the
                             target file
        encoding (str): name of encoding used to encode the file.
        newline (bool): add newline escape sequence to line

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding) as file_obj:
        if newline:
            for line in data:
                file_obj.write(f"{line}\n")  # add newline
        else:
            file_obj.writelines(data)  # write sequence to file


def main():
    """Program entry point. Orchestrates execution flow.

    Parameters:
        None

    Returns:
        None
    """
    # Instantiate a custom PrettyPrinter object
    pp = pprint.PrettyPrinter(indent=1, compact=True, width=100)

    # 4.0 FILE SYSTEM PATHS

    # 4.4.1 CURRENT WORKING DIRECTORY (CWD)
    cwd = Path.cwd()  # TODO method call
    print(f"\n4.4.1.1 pathlib.path cwd = {cwd}")

    # 4.4.2 PARENT DIR PATH
    parent_path = None  # TODO create Path object
    # print(f"\n4.4.2.1 Path(__file__).resolve().parent = {parent_path}")
    # OR
    parent_path = Path().absolute()
    # print(f"\n4.4.2.2 Path.absolute() = {parent_path}")
    # OR
    parent_path = Path().resolve()
    # print(f"\n4.4.2.3 Path.resolve() = {parent_path}")

    # 4.4.3 THIS FILE ABSOLUTE (ABS) PATH
    abs_path = Path(__file__).absolute()
    # print(f"\n4.4.3.1 Path(__file__).absolute() = {abs_path}")
    # OR
    abs_path = Path(__file__).resolve()
    # print(f"\n4.4.3.2 Path(__file__).resolve() = {abs_path}")
    # OR
    abs_path = Path("si506_06.py").resolve()
    # print(f"\n4.4.3.3 Path('si506_week_07.py').resolve() = {abs_path}")

    # 2.4.4 JOIN PATHS
    parent_path = Path(__file__).resolve().parent  # parent directory

    faculty_path = None  # TODO create Path object
    # print(f"\n4.4.4.1 Path.joinpath() data-umsi-faculty.txt path = {faculty_path}")

    resnick_path = parent_path.joinpath("data-resnick_citations.csv")
    # print(f"\n4.4.4.2 Path.joinpath() data-resnick_citations.csv path = {resnick_path}")
    # print(f"\n4.4.4.3 resnick_path type = {type(resnick_path)}")

    # 4.4.5 PATH SEGMENTS
    # print(
    #     "\n4.4.5.1 Path parts",
    #     f"\nname = {resnick_path.name}",
    #     f"\nstem = {resnick_path.stem}",
    #     f"\nsuffix = {resnick_path.suffix}",
    #     f"\nparent dir = {resnick_path.parent}",
    #     f"\nparent.parent dir = {resnick_path.parent.parent}",
    # )

    # 5.0 FILES

    # Relative path
    # filepath = "./data-umsi-faculty.txt"  # relative path
    # filepath = "data-umsi-faculty.txt" # alternative
    # filepath = Path("data-umsi-faculty.txt")  # relative
    # print(f"\n5.0.1 Relative filepath (type={type(filepath)}) = {filepath}")

    # Absolute path (safe)
    filepath = Path("data-umsi-faculty.txt").resolve()
    # filepath = Path("data-umsi-faculty.txt").resolve()
    # filepath = Path().cwd().joinpath("data-umsi-faculty.txt") # alternative
    # print(f"\n5.0.2 ABS Path() filepath (type={type(filepath)}) = {filepath}")

    # 5.1.1 WITH STATEMENT AND OPEN()

    with open(filepath) as file_obj:  # open
        data = file_obj.read()  # returns a single string

    # print(f"\n5.1.1 with open() file_obj.read()\n{data}")

    # 5.2 FILE OPENING MODES

    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.read()

    # print(f"\n5.2 file_obj.read() data (type = {type(data)})")

    # Write out files with names converted to upper case
    # TODO Uncomment
    # with open("./stu-umsi-faculty-v1.txt", "w") as file_obj:  # open in write mode
    #     file_obj.write(data.upper())  # writes string to file

    # 5.3 READ METHODS (READLINE(), READLINES())

    # 5.3.1 READLINE()

    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.readline()
        # data += file_obj.readline() # UNCOMMENT: call n times but not efficient
        # data += file_obj.readline() # UNCOMMENT: call n times but not efficient
        # data += file_obj.readline() # UNCOMMENT: call n times but not efficient

    # print(f"\n5.3.1 file_obj.readline()\n{data}")

    # 5.3.2 READLINES()

    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.readlines()  # returns list; elements include trailing '\n'

    # print(f"\n5.3.2.1 file_obj.readlines() (type={type(data)}\n{data[-8:]}")
    # print(f"\n5.3.2.2 file_obj.readlines(), .join()\n{"".join(data)}")  # print string (pretty)

    # 5.3.3 GOTCHA: READ(), READLINES() LIMITED TO ONE CALL ONLY

    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.read()
        data_lines = file_obj.readlines()  # WARN: does not execute

    # print(f"\n5.3.3 data_lines list is empty = {data_lines}\n")

    # 5.5 WRITE METHODS (WRITE(), WRITELINES())

    # 5.5.1 WRITE STR TO FILE WITH WRITE()

    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.read()  # returns a single multiline string

    # Write out files with names converted to upper case
    # TODO Uncomment
    # with open("./stu-umsi-faculty-v2.txt", "w") as file_obj:  # open in write mode
    #     file_obj.write(data.lower())

    # 5.5.2 WRITE SEQUENCE TO FILE WITH WRITELINES()

    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.readlines()  # returns a list

    # Reverse names: last, first -> first, last
    for i in range(len(data)):
        name = data[i].strip().split(", ")  # strip \n
        data[i] = f"{name[1]} {name[0]}\n"  # restore \n

    # WARN: does not update string
    # for faculty_member in data:
    #     name = faculty_member.strip().split(", ") # strip \n
    #     faculty_member = f"{name[1]} {name[0]}\n" # does not update string element

    # TODO Uncomment
    # with open("./stu-umsi-faculty-v3.txt", "w") as file_obj:  # open in write mode
    #     file_obj.writelines(data)

    # ALTERNATIVE (reverse name order without mutating original data)
    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.readlines()  # returns a single multiline string

    # TODO Uncomment
    # with open("./stu-umsi-faculty-v4.txt", "w") as file_obj:  # open in write mode
    #     for row in data:
    #         name = row.strip().split(", ")
    #         # file_obj.write(f"{name[1]} {name[0]}") # WARN: lose trailing `n`
    #         file_obj.write(f"{name[1]} {name[0]}\n")  # restore `\n`

    # 5.7 CHALLENGE 01

    # Get data
    data = None  # TODO Call function

    # Access surnames first before calling write_file()
    surnames = []
    # TODO Uncomment
    # for row in data:
    #     pass # TODO call function  # trailing \n not required

    # TODO Uncomment
    # Write surnames to file in reverse order
    # write_file("./stu-umsi-faculty-v5.txt", surnames[::-1])

    # TODO Uncomment
    # data_v5 = read_file("./stu-umsi-faculty-v5.txt")
    # assert data_v5[::-1] == surnames  # Reverse to match
    # assert data_v5 == surnames  # Triggers AssertionError

    # 6.0 CSV FILES

    # 6.4 CHALLENGE 02

    # Read CSV file and retrieve data
    filepath = Path("./data-resnick_citations.csv").resolve()  # absolute
    publications_data = None  # TODO Call function
    # print(f"\n6.4.1: Total publications (rows) = {len(publications_data)}")

    # Get headers and publications
    # TODO Uncomment
    # headers = publications_data[0]  # header row
    # print(f"\n6.4.2: headers length: {len(headers)}")
    # publications = publications_data[1:]  # exclude header row
    # print(f"\n6.4.3: publications length: {len(publications)}")

    # Filter title on "recommender"; accumulate results
    recommender_publications = []
    # for publication in publications:
    #   pass  # TODO Implement

    # Write CSV file
    filepath = "./stu-resnick-recommender_pubs.csv"
    # TODO Uncomment
    # write_csv(filepath, recommender_publications, headers)

    # 7.0 VARIABLE SCOPE

    # 7.1 GLOBAL SCOPE AND BUILD-IN SCOPE

    faculty_path = Path("data-umsi-faculty.txt").resolve()  # absolute
    faculty_data = read_file(faculty_path)  # includes header row

    faculty_headers = faculty_data[0]  # header row
    faculty = faculty_data[1:]  # exclude header row

    has_resnick = False
    for member in faculty:
        if member == RESNICK:  # global constant (global scope)
            has_resnick = True
            break

    # print(f"\n7.1: Paul Resnick in faculty = {has_resnick}")

    # 7.2 ENCLOSING SCOPE

    # Inner function (a.k.a nested function)
    def has_person(person):
        return person in faculty  # enclosing scope

    has_resnick = has_person(RESNICK)
    # print(f"\n7.2: Paul Resnick in faculty = {has_resnick}")

    # TODO Uncomment
    # name = person # Triggers NameError

    # 7.3 LOCAL SCOPE

    # Inner function (a.k.a nested function)
    def get_surnames(people):
        last_names = []  # local scope
        for person in people:
            last_names.append(person.split(", ")[0])
        return last_names

    surnames = get_surnames(faculty)
    # print(f"\n7.3: surnames (n={len(surnames)}) = {surnames}")

    # TODO Uncomment
    # surnames = last_names # Triggers NameError

    # 8.0 TRY/EXCEPT

    num = convert_to_int("24")
    # print(f"\n8.0.2: num = {num}")

    num = convert_to_int("twenty_four")
    # print(f"\n8.0.3: num = {num}")

    # 9.0 FUNCTIONS CALLING OTHER FUNCTIONS

    # print(f"\n6.1.0 All strings = {publications[-7]}")  # Recommender systems article

    # TODO Uncomment
    # for publication in publications:
    #     publication = clean_data(publication)

    # print(f"\n6.1.1 Integers converted = {publications[-7]}")  # Recommender systems article

    # 10.0 TUPLE UNPACKING

    # Packing a tuple
    article = (
        "Enquiring Minds: Early Detection of Rumors in Social Media from Enquiry Posts",
        "Zhao, Zhe; Resnick, Paul; Mei, Qiaozhu",
        2015,
        103,
    )
    # print(f"\n10.0.1: article = {article}")

    # Unpacking a tuple
    title, authors, pub_year, citations = article
    # print(f"\n10.0.2: {title} | {authors} | {pub_year} | {citations}")

    # 10.1 UNPACKING ERRORS

    # Uncomment: triggers ValueError (expected 4)
    # title, authors, source_title, pub_year, citations = article

    # Uncomment: triggers ValueError (expected 3)
    # title, authors, pub_year = article

    # Variable order wrong (backwards)
    citations, pub_year, authors, title = article
    # print(f"\n10.0.3: {title} | {authors} | {pub_year} | {citations}")

    # 10.2 UNPACKING IN A LOOP

    column_names = ("Title", "Authors", "Publication Year", "Total Citations")
    recent_publications = []
    # TODO Uncomment
    # for publication in publications[-5:-1]:
    #     title, authors, pub_year, citations = get_min_details(publication, headers, column_names)
    #     recent_publications.append([authors, title, pub_year, citations])

    # print("\n10.2.1: recent publications")
    # pp.pprint(recent_publications)

    # print("\n10.2.2: recent publications")
    # TODO Uncomment
    # for title, authors, pub_year, citations in recent_publications:
    # print(f"{title} | {authors} | {pub_year} | {citations}")

    # 10.3 CHALLENGE 03

    # Test function
    # TODO Uncomment
    # has_umsi_coauther = has_faculty_coauthor(RESNICK, ["Mei, Qiaozhu", "Resnick, Paul"], faculty)
    # print(f"\n10.3.1: Paul Resnick has UMSI coauthor = {has_umsi_coauther}")  # True

    # UMSI coauthored publications
    umsi_coauthored_publications = []
    # for publication in publications:
    # authors = None # TODO Call function
    # authors = None # TODO Call method
    # TODO Implement conditional statement

    # Write to file
    filepath = "./stu-resnick-citations-umsi_coauthored.csv"
    # filepath = Path(__file__).resolve().parent.joinpath("resnick-citations-umsi_coauthors.csv")
    # TODO Uncomment
    # write_csv(filepath, umsi_coauthored_publications, headers)

    # 10.4 CHALLENGE 04

    column_names = ("Title", "Authors", "Publication Year", "Total Citations")

    # Challenge code
    recent_publications = []
    # TODO Uncomment
    # for publication in publications:
    #     ???? = get_min_details(publication, headers, column_names)
    #     if ???:
    #         recent_publications.append(f"{authors}, {title} ({pub_year}), citations={citations}")

    # print("\n10.3.1 recent publications (UMSI coauthors)")
    # pp.pprint(recent_publications)

    # 11.0 ADDITIONAL CHALLENGES

    # 11.1 CHALLENGE 05

    max_citations = None  # TODO replace
    max_count = None  # TODO replace
    # Uncomme
    # for publication in publications:
    #     citation_count = None  # TODO Call function
    #     # TODO Implement conditional statement block

    # Write to file
    filepath = "./stu-resnick-citations-max_citations.csv"
    # filepath = Path(__file__).resolve().parent.joinpath("resnick-citations-max_citations.csv")
    # TODO Call function

    # 11.2 CHALLENGE 06

    # Slice out the years
    # TODO Uncomment
    # year_1995_idx = headers.index("1995")  # first column with annual citation counts
    years = None  # TODO slice

    annual_counts = []
    # TODO Uncomment
    # for year in years:
    #     pass

    # Write to file
    filepath = "./stu-resnick-citations-annual_counts.csv"
    # filepath = Path(__file__).resolve().parent.joinpath("resnick-citations-annual_counts.csv")
    # TODO Call function


if __name__ == "__main__":
    main()
