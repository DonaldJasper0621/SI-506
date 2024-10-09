STREETS = (
    "Ann Arbor-Saline Rd",
    "Auto Mall Dr",
    "Boardwalk Dr",
    "Broadway St",
    "Catherine St",
    "Depot St",
    "Eisenhower Place",
    "Ellsworth Rd",
    "Greene St",
    "Henry Street",
    "Jackson Rd",
    "James L Hart Pkwy",
    "Forrest St",
    "Maynard St",
    "Murfin Ave",
    "Plymouth Rd",
    "Research Park Dr",
    "Runway Blvd",
    "Thompson St",
    "Varsity Dr",
    "Wall St",
    "Washtenaw Ave",
    "William St",
    "Woodridge Ave",
    "E Ann St",
    "E Eisenhower Pkwy",
    "E Huron St",
    "E Washington St",
    "N Adams St",
    "N Ashley St",
    "S Main St",
    "S Fifth Ave",
    "S 5th AveS Forest Ave",
    "S State Rd",
    "S State St",
    "W Ann St",
    "W Liberty Rd",
    "W Washington",
    "W William St",
)


def main():
    """Entry point of the program. Orchestrates the flow of execution.

    Attempt to obtain an exact match of the street name; otherwise attempt to obtain a case
    insensitive partial match.

    Parameters:
        None

    Returns:
        None
    """

    msgs = (
        "SUCCESS: One or more EV charging stations can be found on the provided street.",
        "FAIL: No EV charging stations found on provided street. Provide a different street name.",
    )

    while True:
        is_found = False
        entry = input("\nProvide street name: ")

        if entry in STREETS:
            is_found = True  # exact match obtained
        else:
            for street in STREETS:
                if entry.lower() in street.lower():
                    is_found = True
                    break  # partial match obtained, exit loop

        if is_found:
            print(f"\n{msgs[0]}")
            break  # exit while loop
        print(f"\n{msgs[1]}")


if __name__ == "__main__":
    main()
