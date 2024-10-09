# START PROBLEM SET 2
print("PROBLEM SET 02 \n")

WELLBEING_RESOURCES = (
    "Dean of Students Office|734-764-7420, "
    "Sweetland Center for Writing|734-764-0429, "
    "Office of the Ombuds|734-763-3545, "
    "Counseling and Psychological Services (CAPS)|734-764-8312, "
    "Wolverine Wellness|, "
    "Sexual Assault Prevention and Awareness Center (SAPAC)|734-764-7771, "
    "Trotter Multicultural Center|734-763-3670, "
    "Spectrum Center|734-763-4186, "
    "Maize and Blue Cupboard (MBC)|734-936-2794, "
    "Ginsberg Center for Community Service Learning|734-763-3548"
)


def modify_element(list_, element, email, delimiter=","):
    source_idx = list_.index(element)
    substrings = element.split(delimiter)
    string = substrings[0] + delimiter + email
    list_[source_idx] = string
    return list_


def move_element(list_, current_position, new_position=0):
    list_.insert(new_position, list_.pop(current_position))
    return list_


def main():
    # PROBLEM 01
    print("\nPROBLEM 01")

    # TODO 1.1

    resources = WELLBEING_RESOURCES.split(", ")
    print(f"\n1.1 resource = {resources}")
    print(len(resources))

    # TODO 1.2
    academic = resources[0:3]
    print(f"\n1.2 academic = {academic}")

    # TODO 1.3
    health = resources[3:5]
    print(f"\n1.3 health = {health}")

    # TODO 1.4
    print(len(resources))  # 加起來是總個數
    marginalized_comm = resources[-5:-2]
    print(f"\n1.4 marginalized_comm = {marginalized_comm}")

    # TODO 1.5
    community = resources[-2:]
    print(f"\n1.5 community = {community}")

    # PROBLEM 02
    print("\nPROBLEM 02")

    # TODO 2.1
    addl_health_resources = [
        "University Health Service (UHS)|734-764-8320",
        "SilverCloud|734-936-8660",
    ]
    health.extend(addl_health_resources)
    print(f"\n2.1 health = {health}")
    assert health == [
        "Counseling and Psychological Services (CAPS)|734-764-8312",
        "Wolverine Wellness|",
        "University Health Service (UHS)|734-764-8320",
        "SilverCloud|734-936-8660",
    ]

    # TODO 2.2
    embedded_caps = "UMSI Embedded CAPS Psychologist|Ashley Evearitt"
    health.append(embedded_caps)
    print(f"\n2.2 health = {health}")

    # TODO 2.3
    mesa = "Multi-ethnic Student Affairs (MESA)|734-763-9044"
    marginalized_comm.insert(2, mesa)
    print(f"\n2.3 marginalized_com = {marginalized_comm}")

    # TODO 2.4
    addl_academic_resources = [
        "Office of Student Conflict Resolution",
        "Services for Students with Disabilities (SSD)",
    ]
    addl_academic_resource_numbers = ["|734-936-6308", "|734-763-3000"]

    addl_academic_resources[0] = addl_academic_resources[0] + addl_academic_resource_numbers[0]
    addl_academic_resources[1] = addl_academic_resources[1] + addl_academic_resource_numbers[1]

    # addl_academic_resources = [
    #     resources + numbers
    #     for resources, numbers in zip(addl_academic_resources, addl_academic_resource_numbers)
    # ]

    print(f"\n2.4 addl_academic_resources = {addl_academic_resources}")
    assert addl_academic_resources == [
        "Office of Student Conflict Resolution|734-936-6308",
        "Services for Students with Disabilities (SSD)|734-763-3000",
    ]

    # TODO 2.5
    academic.extend(addl_academic_resources)
    print(f"\n2.5 academic = {academic}")
    assert academic == [
        "Dean of Students Office|734-764-7420",
        "Sweetland Center for Writing|734-764-0429",
        "Office of the Ombuds|734-763-3545",
        "Office of Student Conflict Resolution|734-936-6308",
        "Services for Students with Disabilities (SSD)|734-763-3000",
    ]

    # PROBLEM 03
    print("\nPROBLEM 03")

    # TODO 3.1
    marginalized_comm.remove("Spectrum Center|734-763-4186")
    print(f"\n3.1 marginalized_comm = {marginalized_comm}")

    # TODO 3.2
    health.sort()
    print(f"\n3.2 health = {health}")

    # TODO 3.3
    academic.sort(reverse=True)
    print(f"\n3.3 academic = {academic}")

    # TODO 3.4
    umsi_caps = health.index("UMSI Embedded CAPS Psychologist|Ashley Evearitt")
    print(f"\n3.4 umsi_caps = {umsi_caps}")

    # TODO 3.5
    print(health)
    student_focused_health_resources = health[umsi_caps : umsi_caps + 2]
    print(f"\n3.5 student_focused_health_resources = {student_focused_health_resources}")

    # PROBLEM 04
    print("\nPROBLEM 04")

    # TODO 4.1
    # print("\n", health)
    odd_index_health = health[1::2]
    print(f"\n4.1 odd_index_health = {odd_index_health}")

    # TODO 4.2
    print("\n", academic)
    academic_sub_list = academic[-2:-5:-1]
    print(f"\n4.2 academic_sub_list = {academic_sub_list}")
    assert academic_sub_list == [
        "Office of Student Conflict Resolution|734-936-6308",
        "Office of the Ombuds|734-763-3545",
        "Services for Students with Disabilities (SSD)|734-763-3000",
    ]

    # TODO 4.3
    print("\n", marginalized_comm)
    marginalized_comm_reversed = marginalized_comm[::-1]
    print(f"\n4.3 marginalized_comm_reversed = {marginalized_comm_reversed}")

    # PROBLEM 05
    print("\nPROBLEM 05")

    # TODO 5.2
    print("\n", health)
    rotated_health = move_element(health, -1)
    print(f"\n5.2 rotated_health = {rotated_health}")
    assert rotated_health == [
        "Wolverine Wellness|",
        "Counseling and Psychological Services (CAPS)|734-764-8312",
        "SilverCloud|734-936-8660",
        "UMSI Embedded CAPS Psychologist|Ashley Evearitt",
        "University Health Service (UHS)|734-764-8320",
    ]

    # TODO 5.3
    print("\n", health)
    rotated_health = move_element(new_position=-1, current_position=2, list_=health)
    print(f"\n5.3 rotated_health = {rotated_health}")
    assert rotated_health == [
        "Wolverine Wellness|",
        "Counseling and Psychological Services (CAPS)|734-764-8312",
        "UMSI Embedded CAPS Psychologist|Ashley Evearitt",
        "SilverCloud|734-936-8660",
        "University Health Service (UHS)|734-764-8320",
    ]

    # PROBLEM 06
    print("\nPROBLEM 06")

    # TODO 6.1
    print(f"\n6.1 academic = {academic}")

    # TODO 6.2
    academic_ssd = modify_element(
        academic,
        element="Services for Students with Disabilities (SSD)|734-763-3000",
        email="ssdoffice@umich.edu",
        delimiter="|",
    )
    print(f"\n6.2 academic_ssd = {academic_ssd}")
    assert academic_ssd == [
        "Sweetland Center for Writing|734-764-0429",
        "Services for Students with Disabilities (SSD)|ssdoffice@umich.edu",
        "Office of the Ombuds|734-763-3545",
        "Office of Student Conflict Resolution|734-936-6308",
        "Dean of Students Office|734-764-7420",
    ]

    # TODO 6.3
    academic_ombuds = modify_element(
        delimiter="|",
        email="umstudentombuds@umich.edu",
        element="Office of the Ombuds|734-763-3545",
        list_=academic,
    )
    print(f"\n6.3 academic_ombuds = {academic_ombuds}")
    assert academic_ombuds == [
        "Sweetland Center for Writing|734-764-0429",
        "Services for Students with Disabilities (SSD)|ssdoffice@umich.edu",
        "Office of the Ombuds|umstudentombuds@umich.edu",
        "Office of Student Conflict Resolution|734-936-6308",
        "Dean of Students Office|734-764-7420",
    ]

    # END PROBLEM SET


# WARN: do not modify or remove the following if statement.

if __name__ == "__main__":
    main()
