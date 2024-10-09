# START PROBLEM SET 04

# Setup Code (DO NOT MODIFY)

# fmt: off

DATA = [
    "Company Name, Location, Number of Employees, Website, Industry",
    "Amcor, switzerland, 44000, https://www.amcor.com, consumer packaged goods ",
    "Auto-Owners Insurance, michigan, 5394, https://www.auto-owners.com , insurance ",
    "Blue cross Blue Shield of Michigan, michigan, 850, https://m.bcbsm.com/index.html, Insurance",
    "Cisco, California, 77500, https://www.cisco.com, software",
    "Deloitte, England, 41500, https://www2.deloitte.com/us/en.html, financial",
    "Epic, Wisconsin, 10000, https://www.epic.com, healthcare",
    "Health Management Associates, Michigan, 5394, https://www.healthmanagement.com , healthcare",
    "Johnson Controls, wisconsin, 97000, https://www.johnsoncontrols.com, software",
    "menlo innovations, michigan, 34, https://menloinnovations.com, Software ",
    "MRM, New York, 2300, https://www.mrm.com/en/, software",
    "OneMagnify, Michigan, 520, https://onemagnify.com, Marketing",
    "Plymouth District Library, Michigan, 37, https://www.plymouthlibrary.org, education",
    "PricewaterhouseCoopers (PwC), england, 295000, https://www.pwc.com/us/en, consulting ",
    "Procter & Gamble (P&G), Ohio, 97000, https://us.pg.com, Consumer Packaged Goods",
    "TechSmith Corporation, Michigan, 293, https://www.techsmith.com, Software",
    "United States Federal Bureau of Investigation (FBI), Washington DC, 35000, https://www.fbi.gov, government",
    "University of Michigan Bentley Historical Library, Michigan, 29, https://bentley.umich.edu, education",
    "University of Michigan Center for Academic Innovation, Michigan, 150, https://ai.umich.edu, Education",
    "University of Michigan Desai Accelerator, Michigan, 30, https://desaiaccelerator.umich.edu, Consulting",
    "University of Michigan Innovation Partnerships, michigan, 15, https://innovationpartnerships.umich.edu, consulting",
    "University of Michigan ITS, Michigan, 500, https://its.umich.edu, education",
    "University of Michigan Library, michigan, 400, https://www.lib.umich.edu, Education",
    "VA Center for Clinical Management Research, Michigan, 150, https://www.annarbor.hsrd.research.va.gov, healthcare",
]

EMPLOYERS_CHECK = [
    ["Company Name", "Location", "Number of Employees", "Website", "Industry"],
    ["Amcor", "switzerland", "44000", "https://www.amcor.com", "consumer packaged goods "],
    ["Auto-Owners Insurance", "michigan", "5394", "https://www.auto-owners.com ", "insurance "],
    ["Blue cross Blue Shield of Michigan", "michigan", "850", "https://m.bcbsm.com/index.html", "Insurance"],
    ["Cisco", "California", "77500", "https://www.cisco.com", "software"],
    ["Deloitte", "England", "41500", "https://www2.deloitte.com/us/en.html", "financial"],
    ["Epic", "Wisconsin", "10000", "https://www.epic.com", "healthcare"],
    ["Health Management Associates", "Michigan", "5394", "https://www.healthmanagement.com ", "healthcare"],
    ["Johnson Controls", "wisconsin", "97000", "https://www.johnsoncontrols.com", "software"],
    ["menlo innovations", "michigan", "34", "https://menloinnovations.com", "Software "],
    ["MRM", "New York", "2300", "https://www.mrm.com/en/", "software"],
    ["OneMagnify", "Michigan", "520", "https://onemagnify.com", "Marketing"],
    ["Plymouth District Library", "Michigan", "37", "https://www.plymouthlibrary.org", "education"],
    ["PricewaterhouseCoopers (PwC)", "england", "295000", "https://www.pwc.com/us/en", "consulting "],
    ["Procter & Gamble (P&G)", "Ohio", "97000", "https://us.pg.com", "Consumer Packaged Goods"],
    ["TechSmith Corporation", "Michigan", "293", "https://www.techsmith.com", "Software"],
    ["United States Federal Bureau of Investigation (FBI)", "Washington DC", "35000", "https://www.fbi.gov", "government"],
    ["University of Michigan Bentley Historical Library", "Michigan", "29", "https://bentley.umich.edu", "education"],
    ["University of Michigan Center for Academic Innovation", "Michigan", "150", "https://ai.umich.edu", "Education"],
    ["University of Michigan Desai Accelerator", "Michigan", "30", "https://desaiaccelerator.umich.edu", "Consulting"],
    ["University of Michigan Innovation Partnerships", "michigan", "15", "https://innovationpartnerships.umich.edu", "consulting"],
    ["University of Michigan ITS", "Michigan", "500", "https://its.umich.edu", "education"],
    ["University of Michigan Library", "michigan", "400", "https://www.lib.umich.edu", "Education"],
    ["VA Center for Clinical Management Research", "Michigan", "150", "https://www.annarbor.hsrd.research.va.gov", "healthcare"]
]

OTHER_COMPANIES_CHECK = [
    ["Amcor", "switzerland", "44000", "https://www.amcor.com", "consumer packaged goods "],
    ["Auto-Owners Insurance", "michigan", "5394", "https://www.auto-owners.com ", "insurance "],
    ["Blue cross Blue Shield of Michigan", "michigan", "850", "https://m.bcbsm.com/index.html", "Insurance"],
    ["Cisco", "California", "77500", "https://www.cisco.com", "software"],
    ["Deloitte", "England", "41500", "https://www2.deloitte.com/us/en.html", "financial"],
    ["Epic", "Wisconsin", "10000", "https://www.epic.com", "healthcare"],
    ["Health Management Associates", "Michigan", "5394", "https://www.healthmanagement.com ", "healthcare"],
    ["Johnson Controls", "wisconsin", "97000", "https://www.johnsoncontrols.com", "software"],
    ["menlo innovations", "michigan", "34", "https://menloinnovations.com", "Software "],
    ["MRM", "New York", "2300", "https://www.mrm.com/en/", "software"],
    ["OneMagnify", "Michigan", "520", "https://onemagnify.com", "Marketing"],
    ["Plymouth District Library", "Michigan", "37", "https://www.plymouthlibrary.org", "education"],
    ["PricewaterhouseCoopers (PwC)", "england", "295000", "https://www.pwc.com/us/en", "consulting "],
    ["Procter & Gamble (P&G)", "Ohio", "97000", "https://us.pg.com", "Consumer Packaged Goods"],
    ["TechSmith Corporation", "Michigan", "293", "https://www.techsmith.com", "Software"],
    ["United States Federal Bureau of Investigation (FBI)", "Washington DC", "35000", "https://www.fbi.gov", "government"],
    ["University of Michigan Bentley Historical Library", "Michigan", "29", "https://bentley.umich.edu", "education"],
    ["University of Michigan Desai Accelerator", "Michigan", "30", "https://desaiaccelerator.umich.edu", "Consulting"],
    ["University of Michigan ITS", "Michigan", "500", "https://its.umich.edu", "education"],
    ["University of Michigan Library", "michigan", "400", "https://www.lib.umich.edu", "Education"],
    ["VA Center for Clinical Management Research", "Michigan", "150", "https://www.annarbor.hsrd.research.va.gov", "healthcare"]
]

SALARIES = """Amcor; Project Engineer; 156857
Auto-Owners Insurance; Systems Analyst; 107997
Blue Cross Blue Shield of Michigan; Senior Analyst; 99793
Cisco; Business analyst; 150000
Deloitte; Senior Consultant; 111176
Epic; Software developer; 152441
Health Management Associates; Senior Consultant; 121856
Johnson Controls; Associate Project Manager; 90541
Menlo Innovations; Software Consultant; 234724
MRM; Associate Project Manager; 70338
OneMagnify; Technical Solutions Manager; 173165
Plymouth District Library; Librarian; 63927
PricewaterhouseCoopers (PwC); Technology Consultant; 123246
Procter & Gamble (P&G); Business Analyst; 116342
TechSmith Corporation; Technical Support Specialist; 62559
United States Federal Bureau of Investigation (FBI); Special agent; 115500
"""

SALARY_LIST_CHECK = [
    ["Amcor", "Project Engineer", "156857"],
    ["Auto-Owners Insurance", "Systems Analyst", "107997"],
    ["Blue Cross Blue Shield of Michigan", "Senior Analyst", "99793"],
    ["Cisco", "Business analyst", "150000"],
    ["Deloitte", "Senior Consultant", "111176"],
    ["Epic", "Software developer", "152441"],
    ["Health Management Associates", "Senior Consultant", "121856"],
    ["Johnson Controls", "Associate Project Manager", "90541"],
    ["Menlo Innovations", "Software Consultant", "234724"],
    ["MRM", "Associate Project Manager", "70338"],
    ["OneMagnify", "Technical Solutions Manager", "173165"],
    ["Plymouth District Library", "Librarian", "63927"],
    ["PricewaterhouseCoopers (PwC)", "Technology Consultant", "123246"],
    ["Procter & Gamble (P&G)", "Business Analyst", "116342"],
    ["TechSmith Corporation", "Technical Support Specialist", "62559"],
    ["United States Federal Bureau of Investigation (FBI)", "Special agent", "115500"]
]

# fmt: on

# End Setup Code


def convert_multiline_string(multiline_string):
    # TODO 5.1
    splitlines = multiline_string.splitlines()
    return format_data(splitlines, "; ")


def filter_by_industry(list_, headers, industry_filter):
    # TODO 3.1
    filtered_companies = []
    for item in list_:
        industry = item[headers.index("Industry")].lower().strip()
        name = item[0]
        if industry == industry_filter:
            filtered_companies.append(name)
    return filtered_companies


def format_data(data, delimiter):
    # TODO 1.1
    formatted_data = []
    for i in range(len(data)):
        rel_data = data[i].split(delimiter)
        formatted_data.append(rel_data)
    return formatted_data


def get_consult_manager_salaries(salaries):
    # TODO 6.1
    consult_manager_salary = []
    i = 0
    while i < len(salaries):
        job_title = salaries[i][1].lower().strip()
        job_salary = int(salaries[i][2])
        if "consultant" in job_title or "manager" in job_title:
            consult_manager_salary.append(job_salary)
        i += 1
    return consult_manager_salary


def get_largest_companies(companies, state):
    # TODO 4.1
    largest_companies = []
    max_num_employees = -1
    for item in companies:
        num_employees = int(item[2])
        location = item[1].lower().strip()
        if location == state.lower():
            if num_employees > max_num_employees:
                max_num_employees = num_employees
                largest_companies.clear()
                largest_companies.append(item[0])
            elif num_employees == max_num_employees:
                largest_companies.append(item[0])
    return largest_companies


def group_employers(employers, keyword1, keyword2):
    # TODO 2.1
    matching_companies = []
    other_companies = []
    for item in employers[1:]:
        every_employer = str(item[0]).lower().strip()
        if keyword1 in every_employer and keyword2 in every_employer:
            matching_companies.append(item)
        else:
            other_companies.append(item)
    return (matching_companies, other_companies)


def group_salaries(salaries, salary1, salary2):
    # TODO 7.1
    company_salary_one = []
    company_salary_two = []
    i = 0
    while i < len(salaries):
        job_salary = int(salaries[i][2])
        company = salaries[i][0]
        if job_salary >= salary1 and job_salary <= salary2:
            company_salary_one.append(company)
        elif job_salary > salary2:
            company_salary_two.append(company)
        i += 1
    return (company_salary_one, company_salary_two)


def main():
    print("Problem Set 4 \n")

    # PROBLEM 01
    print("\nPROBLEM 1")

    # TODO 1.1
    # Implement the function format_data()

    # TODO 1.2
    employers = format_data(DATA, ", ")

    print(f"\n[1.2] employers = {employers}")
    assert employers == EMPLOYERS_CHECK

    # TODO 1.3
    headers = employers[0]
    print(f"\n[1.3] headers row = {headers}")
    assert headers == ["Company Name", "Location", "Number of Employees", "Website", "Industry"]

    # PROBLEM 02
    print("\nPROBLEM 2")

    # TODO 2.1
    # Implement the function group_employers()

    # TODO 2.2
    grouped_employers = group_employers(employers, "university", "innovation")
    universities_innovation = grouped_employers[0]
    other_companies = grouped_employers[1]

    print(f"\n[2.2] universities_innovation = {universities_innovation}")
    assert universities_innovation == [
        [
            "University of Michigan Center for Academic Innovation",
            "Michigan",
            "150",
            "https://ai.umich.edu",
            "Education",
        ],
        [
            "University of Michigan Innovation Partnerships",
            "michigan",
            "15",
            "https://innovationpartnerships.umich.edu",
            "consulting",
        ],
    ]
    # print(f"{grouped_employers}")
    print(f"\n[2.2] other_companies = {other_companies}")
    assert other_companies == OTHER_COMPANIES_CHECK

    # PROBLEM 03
    print("\nPROBLEM 3")

    # TODO 3.1
    # Implement the function filter_by_industry()

    # TODO 3.2
    consulting = filter_by_industry(other_companies, headers, "consulting")

    print(f"\n[3.2] consulting = {consulting}")
    assert consulting == [
        "PricewaterhouseCoopers (PwC)",
        "University of Michigan Desai Accelerator",
    ]

    # TODO 3.3
    education = filter_by_industry(other_companies, headers, "education")

    print(f"\n[3.3] education = {education}")
    assert education == [
        "Plymouth District Library",
        "University of Michigan Bentley Historical Library",
        "University of Michigan ITS",
        "University of Michigan Library",
    ]

    # TODO 3.4
    healthcare = filter_by_industry(other_companies, headers, "healthcare")

    print(f"\n[3.4] healthcare = {healthcare}")
    assert healthcare == [
        "Epic",
        "Health Management Associates",
        "VA Center for Clinical Management Research",
    ]

    # TODO 3.5
    software = filter_by_industry(other_companies, headers, "software")

    print(f"\n[3.5] software = {software}")
    assert software == [
        "Cisco",
        "Johnson Controls",
        "menlo innovations",
        "MRM",
        "TechSmith Corporation",
    ]

    # PROBLEM 04
    print("\nPROBLEM 4")

    # TODO 4.1
    # Implement the function get_largest_companies()

    # TODO 4.2
    largest_michigan_companies = get_largest_companies(other_companies, "michigan")

    print(f"\n[4.2] largest_michigan_companies = {largest_michigan_companies}")
    assert largest_michigan_companies == ["Auto-Owners Insurance", "Health Management Associates"]

    # TODO 4.3
    largest_california_companies = get_largest_companies(other_companies, "california")

    print(f"\n[4.3] largest_california_companies = {largest_california_companies}")
    assert largest_california_companies == ["Cisco"]

    # PROBLEM 05
    print("\nPROBLEM 5")

    # TODO 5.1
    # Implement the function convert_multiline_string()

    # TODO 5.2
    salary_list = convert_multiline_string(SALARIES)

    print(f"\n[5.2] salary_list = {salary_list}")
    assert salary_list == SALARY_LIST_CHECK

    # PROBLEM 06
    print("\nPROBLEM 6")

    # TODO 6.1
    # Implement the function get_consult_manager_salaries()

    # TODO 6.2
    consult_manager_salary = get_consult_manager_salaries(salary_list)

    print(f"\n[6.2] consult_manager_salary = {consult_manager_salary}")
    assert consult_manager_salary == [111176, 121856, 90541, 234724, 70338, 173165, 123246]

    # TODO 6.3
    avg_consult_manager_salary = round(sum(consult_manager_salary) / len(consult_manager_salary), 2)
    print(f"\n[6.3] avg_consult_manager_salary = {avg_consult_manager_salary}")

    # PROBLEM 07
    print("\nPROBLEM 7")

    # TODO 7.1
    # Implement the function group_salaries()

    # TODO 7.2
    company_salaries = group_salaries(salary_list, 100000, 200000)

    # TODO 7.3
    company_salary_one = company_salaries[0]

    print(f"\n[7.3] company_salary_one = {company_salary_one}")
    assert company_salary_one == [
        "Amcor",
        "Auto-Owners Insurance",
        "Cisco",
        "Deloitte",
        "Epic",
        "Health Management Associates",
        "OneMagnify",
        "PricewaterhouseCoopers (PwC)",
        "Procter & Gamble (P&G)",
        "United States Federal Bureau of Investigation (FBI)",
    ]

    # TODO 7.4
    company_salary_two = company_salaries[1]

    print(f"\n[7.4] company_salary_two = {company_salary_two}")
    assert company_salary_two == ["Menlo Innovations"]


# END PROBLEM SET


# WARN: do not modify or remove the following if statement.

if __name__ == "__main__":
    main()
