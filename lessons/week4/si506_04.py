# SI 506: Iteration and Control Flow, Part I

import pprint  # import statement

# fmt: off
E_VEHICLES = [
    ["make", "model", "type", "drivetrain", "fuel_ec_mpge", "range_mi", "battery_kwh", "seats", "base_msrp"],
    ["Tesla", "Model 3 RWD", "Sedan/Wagon", "RWD", "132", "272", "60", "5", "$46,990"],
    ["Porsche", "Taycan GTS Sport Turismo", "Sedan/Wagon", "AWD", "80", "233", "109", "4", "$86,700"],
    ["Kia", "Niro Electric", "Sedan/Wagon", "FWD", "113", "253", "64", "5", "$39,900"],
    ["Lucid", "Air G Touring XR AWD", "Sedan/Wagon", "AWD", "131", "516", "120", "5", "$87,400"],
    ["Toyota", "bZ4X AWD", "SUV", "AWD", "104", "228", "72", "5", "$44,080"],
    ["BMW", "i4 M50 Gran Coupe", "Sedan/Wagon", "AWD", "96", "271", "83", "5", "$67,300"],
    ["Tesla", "Model X", "SUV", "AWD", "102", "348", "104", "7", "$120,990"],
    ["Volkswagen", "ID.4 AWD Pro/Pro S", "SUV", "AWD", "99", "255", "81", "5", "$41,230"],
    ["Genesis", "Electrified G80", "Sedan/Wagon", "AWD", "97", "282", "87", "", "$79,825"],
    ["Porsche", "Taycan AWD", "Sedan/Wagon", "AWD", "83", "246", "109", "4", "$86,700"],
    ["Mini Cooper", "SE Hardtop 2 door", "Sedan/Wagon", "FWD", "110", "114", "32", "4", "$29,900"],
    ["Genesis", "GV60 Performance", "Sedan/Wagon", "AWD", "90", "235", "77", "", "$67,890"],
    ["Rivian", "R1S", "SUV", "AWD", "71", "321", "144", "7", "$78,000"],
    ["Tesla", "Model Y AWD", "SUV", "AWD", "123", "330", "84", "7", "$65,990"],
    ["Audi", "e-tron Sportback/S Sportback", "SUV", "AWD", "78", "225", "95", "5", "$69,100"],
    ["Rivian", "R1T", "Pickup", "AWD", "73", "328", "144", "5", "$73,000"],
    ["Tesla", "Model S", "Sedan/Wagon", "AWD", "120", "405", "104", "5", "$104,990"],
    ["Toyota", "bZ4X", "SUV", "FWD", "119", "252", "71", "5", "$42,000"],
    ["Polestar", "Automotive USA Polestar 2", "Sedan/Wagon", "FWD", "107", "270", "77", "5", "$48,400"],
    ["Audi", "e-tron quattro/S", "SUV", "AWD", "79", "226", "95", "5", "$65,900"],
    ["BMW", "i7 xDrive60 Sedan", "Sedan/Wagon", "AWD", "89", "318", "105", "5", "$119,300"],
    ["BMW", "iX xDrive50", "SUV", "AWD", "86", "324", "76", "5", "$83,200"],
    ["Chevrolet", "Bolt EV", "Sedan/Wagon", "FWD", "120", "259", "75", "5", "$25,600"],
    ["BMW", "iX M60", "SUV", "AWD", "78", "288", "111", "5", "$108,900"],
    ["Tesla", "Model 3 AWD", "Sedan/Wagon", "AWD", "131", "358", "84", "5", "$46,990"],
]
# fmt: on


def count_vehicles_by_range(vehicles, headers, range_mi=250):
    vehicle_count = 0
    for vehicle in vehicles:
        if vehicle[headers.index("range_mi")] >= range_mi:
         vehicle_count += 1
    return vehicle_count


def get_ev_types(vehicles):
    ev_types = []
    # TODO: implement loop using range()
    return ev_types


def get_make_model(vehicle):
    return f"{vehicle[0]} {vehicle[1]}"  # TODO: implement f-string


def get_vehicles(vehicles, automaker):
    autos = []
    # TODO: implement loop
    for vehicle in vehicles:
        if vehicle[0].lower() == automaker.lower():
            autos.append(vehicle)
    return autos


def is_domestic(vehicle, automakers):
    return vehicle[0] in automakers  # returns True or False


def main():
    # Create a PrettyPrinter object
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=120)

    # 3.1 NESTED LISTS

    # EV attributes: make, model, vehicle type, drivetrain, fuel economy mpge,
    # range mi, battery capacity kwh, seats, base msrp

    vehicles = [
        "Tesla, Model 3 RWD, Sedan/Wagon, RWD, 132, 272, 60, 5, $46,990",
        "Porsche, Taycan GTS Sport Turismo, Sedan/Wagon, AWD, 80, 233, 109, 4, $86,700",
        "Kia, Niro Electric, Sedan/Wagon, FWD, 113, 253, 64, 5, $39,900",
        "Lucid, Air G Touring XR AWD, Sedan/Wagon, AWD, 131, 516, 120, 5, $87,400",
        "Toyota, bZ4X AWD, SUV, AWD, 104, 228, 72, 5, $44,080",
    ]

    model = vehicles[0].split(", ")[1] # TODO access Model 3 RWD
    # print(f"\n3.1.1 Model = {model}")

    # fmt: off
    vehicles = [
        ["Tesla", "Model 3 RWD", "Sedan/Wagon", "RWD", "132", "272", "60", "5", "$46,990"],
        ["Porsche", "Taycan GTS Sport Turismo", "Sedan/Wagon", "AWD", "80", "233", "109", "4", "$86,700"],
        ["Kia", "Niro Electric", "Sedan/Wagon", "FWD", "113", "253", "64", "5", "$39,900"],
        ["Lucid", "Air G Touring XR AWD", "Sedan/Wagon", "AWD", "131", "516", "120", "5", "$87,400"],
        ["Toyota", "bZ4X AWD", "SUV", "AWD", "104", "228", "72", "5", "$44,080"]
    ]
    # fmt: on

    model = vehicles[0][1]  # TODO access Model 3 RWD
    # print(f"\n3.1.2 Model = {model}")

    # 3.2 FOR LOOP
    for element in E_VEHICLES:
        print(element)
    # print("\n3.2.1 Print elements")
    # TODO: implement loop to print all vehicles

    # print("\n3.2.2 Print first three vehicle elements")
    # TODO: implement loop to print first three vehicles
    for elements in range(3):
        print(E_VEHICLES[elements])

    # 3.3 IF STATEMENT

    # print("\n3.3.1 Find Kia and print")
    for vehicle in E_VEHICLES[1:]:
        if vehicle[0].startswith("Kia"):
            print(vehicle)

    # print("\n3.3.2 Get all Volkswagen vehicles and print")
    for vehicle in E_VEHICLES[1:]:
        if "volkswagen" in vehicle[0].lower():
            print(vehicle)

    # print("\n3.3.3 Exclude all Volkswagen vehicles and print")
    for vehicle in E_VEHICLES[1:]:
       if "volkswagen" not in vehicle[0].lower():
            print(vehicle)

    # 3.4.1 CHALLENGE 01

    headers = E_VEHICLES[0]  # TODO replace with column headers
    model_idx = headers.index("model")  # TODO lookup index
    print(f"\n3.4.1.1 model index = {model_idx}")

    vehicles = E_VEHICLES[1:]  # TODO replace with nested lists
    print(f"\n3.4.1.2 vehicle count = {len(vehicles)}")

    lucid = vehicles[3]  # TODO access Lucid Air G Touring XR AWD
    print(f"\n3.4.1.3 Lucid Air G Touring XR AWD = {lucid}")

    range_mi_idx = headers.index("range_mi")  # TODO lookup index
    lucid_range_mi = lucid [range_mi_idx] # TODO access range_mi
    print(f"\n3.4.1.4 Lucid Air G Touring XR AWD battery range = {lucid_range_mi} mi")
    # assert lucid_range_mi == "516"

    # 3.4.2 CHALLENGE 02

    make_model = get_make_model(vehicles[-2])  # TODO call function
    print(f"\n3.4.2 Make and model = {make_model}")
    # assert make_model == "BMW iX M60"

    # 4.0 ACCUMULATOR PATTERN
    pp.pprint(f"4.0{vehicles}")
    teslas = []
    # TODO: Uncomment loop
    for vehicle in vehicles:
        if "tesla" in vehicle[0].lower():
            teslas.append(vehicle)

    print(f"\n4.0.0 Teslas (n={len(teslas)})")
    pp.pprint(teslas)

    # 4.0.1 Max range (does not handle ties)
    ev_max_range = None
    max_range = 0
    # TODO: Uncomment loop
    for vehicle in vehicles:
        # vehicle_range = int(vehicle[5])  # cast str to int
        vehicle_range = int(vehicle[headers.index("range_mi")])  # lookup index
        if vehicle_range > max_range:
            ev_max_range = get_make_model(vehicle)  # call function
            max_range = vehicle_range


    print(f"\n4.0.1 EV max range = {ev_max_range} ({max_range} mi)")

    # 4.1.1 CHALLENGE 03

    rivian_models = get_vehicles(E_VEHICLES[1:], "Rivian")  # TODO call function
    
    print(f"\n4.1.1 Rivian EVs (n={len(rivian_models)})")
    pp.pprint(rivian_models)

    # 4.1.3 CHALLENGE 04

    ev_min_range = [None, float("inf")]  # store in list
    # ev_min_range = [None, float("inf")] # infinity
    for vehicle in vehicles:
        range_mi_idx = vehicle[headers.index("range_mi")]
        vehicle_range = int(range_mi_idx)
    
        if vehicle_range < ev_min_range[1]:
            ev_min_range[0] = get_make_model(vehicle)
            ev_min_range[1] = vehicle_range


    print(f"\n4.1.3 Shortest range = {ev_min_range[0]} ({ev_min_range[1]} mi)")
    # assert ev_min_range == ["Mini Cooper SE Hardtop 2 door", 114]

    # 4.2 ACCUMULATING COUNTS

    bmw_count = 0
    for vehicle in vehicles:
        if "bmw" in vehicle[0].lower():
            bmw_count += 1  # assignment addition equivalent to bmw_count = bmw_count + 1

    print(f"\n4.2 BMW count = {bmw_count}")

    # 4.3.1 CHALLENGE 05
    
    vehicle_count = None  # TODO call function
    # print(f"\n4.3 Vehicle range >= {vehicle_count}")
    # assert vehicle_count == 18

    # 5.0 IF-ELSE CONDITIONS

    sedan_wagon = []
    suv_pickup = []
    for vehicle in vehicles:
        make_model = get_make_model(vehicle)
        if vehicle[headers.index("type")] == "Sedan/Wagon":
            sedan_wagon.append(make_model)
        else:
            suv_pickup.append(make_model)

    # print(f"\n5.0.1 Sedan/Wagon (n={len(sedan_wagon)})")
    # pp.pprint(sedan_wagon)
    # print(f"\n5.0.1 SUV/Pickup (n={len(suv_pickup)})")
    # pp.pprint(suv_pickup)

    standard_ranges = []
    outlier_ranges = []
    for vehicle in vehicles:
        make_model = f"{get_make_model(vehicle)} (range = {vehicle[5]} mi)"
        range_mi_idx = headers.index("range_mi")  # lookup index
        if 225 <= int(vehicle[range_mi_idx]) <= 325:
            standard_ranges.append(make_model)
        else:
            outlier_ranges.append(make_model)

    # print(f"\n5.0.2 Standard ranges (n={len(standard_ranges)})")
    # pp.pprint(standard_ranges)
    # print(f"\n5.0.2 Outlier ranges (n={len(outlier_ranges)})")
    # pp.pprint(outlier_ranges)

    # 5.1.1 Challenge 06

    us_automakers = [
        "Cadillac",
        "Chevrolet",
        "Ford",
        "Lucid",
        "Polestar Automotive USA",
        "Rivian",
        "Tesla",
    ]

    domestic_count = 0
    foreign_count = 0
    for vehicle in vehicles:
        pass  # Implement conditional logic

    # print(f"\n5.1.1.1 Domestic-designed EV count = {domestic_count}")
    # print(f"\n5.1.1.2 Foreign-designed EV count = {foreign_count}")

    # 5.1.2 CHALLENGE 07

    affordable = []
    unaffordable = []
    for vehicle in vehicles:
        msrp = vehicle[headers.index("base_msrp")]
        msrp = None  # TODO: eliminate dollar sign ($) sign and comma (,)
        make_model = None  # TODO: call function
        # TODO Implement conditional logic

    # print(f"\n5.1.2.1 Affordable EVs for loop (len={len(affordable)})")
    # pp.pprint(sorted(affordable))
    # print(f"\n5.1.2.2 Unaffordable EVs for loop (len={len(unaffordable)})")
    # pp.pprint(sorted(unaffordable))

    # 6.0 IF-ELIF-ELSE CONDITIONS

    awd_count = 0
    fwd_count = 0
    rwd_count = 0
    unknown_count = 0
    for vehicle in vehicles:
        drivetrain = vehicle[headers.index("drivetrain")]
        if drivetrain == "AWD":
            awd_count += 1
        elif drivetrain == "FWD":
            fwd_count += 1
        elif drivetrain == "RWD":
            rwd_count += 1
        else:
            unknown_count += 1

    # print(f"\n6.0.1 Drivetrain (AWD) count = {awd_count}")
    # print(f"\n6.0.2 Drivetrain (FWD) count = {fwd_count}")
    # print(f"\n6.0.3 Drivetrain (RWD) count = {rwd_count}")
    # print(f"\n6.0.4 Drivetrain (Unknown) count = {unknown_count}")

    watts_mi_low = []
    watts_mi_med = []
    watts_mi_high = []
    watts_mi_vhigh = []
    for vehicle in vehicles:
        watt_hours = int(vehicle[headers.index("battery_kwh")]) * 1000
        range_mi = int(vehicle[headers.index("range_mi")])
        watts_mi = round(watt_hours / range_mi, 2)
        make_model_watts = f"{get_make_model(vehicle)} ({watts_mi} watts/mi)"
        if watts_mi < 250:
            watts_mi_low.append(make_model_watts)
        elif 250 <= watts_mi < 300:
            watts_mi_med.append(make_model_watts)
        elif 300 <= watts_mi < 350:
            watts_mi_high.append(make_model_watts)
        elif watts_mi >= 350:
            watts_mi_vhigh.append(make_model_watts)

    # print(f"\n6.0.5 Low watts/mi (len={len(watts_mi_low)})")
    # pp.pprint(sorted(watts_mi_low))
    # print(f"\n6.0.6 Medium watts/mi (len={len(watts_mi_med)})")
    # pp.pprint(sorted(watts_mi_med))
    # print(f"\n6.0.7 High watts/mi (len={len(watts_mi_high)})")
    # pp.pprint(sorted(watts_mi_high))
    # print(f"\n6.0.8 Very high watts/mi (len={len(watts_mi_vhigh)})")
    # pp.pprint(sorted(watts_mi_vhigh))

    # 6.1.1 CHALLENGE 08

    awd_range = []
    fwd_range = []
    rwd_range = []
    for vehicle in vehicles:
        drivetrain = vehicle[headers.index("drivetrain")]
        range_mi = None  # TODO: access range_mi
        # TODO Implement conditional logic

    awd_avg_range = None  # TODO calculate average range
    fwd_avg_range = None  # TODO calculate average range
    rwd_avg_range = None  # TODO calculate average range

    # print(f"\n6.1.1.1 AWD avg range (n={len(awd_range)}) = {awd_avg_range} mi")
    # print(f"\n6.1.1.2 FWD avg range (n={len(fwd_range)}) = {fwd_avg_range} mi")
    # print(f"\n6.1.1.3 RWD avg range (n={len(rwd_range)}) = {rwd_avg_range} mi")

    # 7.0 LOOPING WITH RANGE()

    # 7.1 range() behaviors

    seq = range(10)
    # print(f"\n7.1.1 seq (type={type(seq)}) = {seq}")  # <class 'range'>

    seq = list(range(10))  # convert range object to a list
    # print(f"\n7.1.2 range seq = {seq}")

    seq = list(range(5, 10))
    # print(f"\n7.1.3 range seq start/stop = {seq}")

    seq = list(range(5, 21, 5))
    # print(f"\n7.1.4 range seq start/stop/step = {seq}")

    seq = list(range(20, 4, -5))
    # print(f"\n7.1.5 range seq start/stop/step reversed = {seq}")

    # 7.2 The `for` loop and `range`

    # print("\n7.2 for loop with range()\n")
    # TODO: Uncomment
    # for i in range(5):
    #     # print("I want an EV!")

    automakers = [
        "Bayerische Motoren Werke AG",
        "Ford Motor Co.",
        "General Motors Co.",
        "Kandi Technologies Group",
        "Nissan Motor Co.",
        "Volkswagen AG",
        "Volvo Group",
        "Tesla, Inc.",
    ]

    # print("\n7.2 access automakers with range()")

    # TODO: Uncomment
    # for i in range(len(automakers)):
    #     # print(f"{i} {automakers[i]}")

    # WARN: Replace immutable string value fails
    for automaker in automakers:
        automaker = automaker.upper()  # assigns new string to loop variable only

    # 7.3 Employing `range` to replace list elements

    # print("\n7.3.1 automaker to uppercase (fail)")
    # pp.pprint(automakers)

    # Replace immutable element value (success)
    for i in range(len(automakers)):
        pass # TODO assign new string to element

    # print("\n7.3.2 automaker to uppercase")
    # pp.pprint(automakers)

    # Modify every third element commencing from index 0
    for i in range(0, len(automakers), 3):
        automakers[i] = automakers[i].lower()  # assigns new string elements at positions 0, 3, 6

    # print(f"\n7.3.3 to lowercase (sequence = {list(range(0, len(automakers), 3))})")
    # pp.pprint(automakers)

    # 7.4 Subscript notation chaining

    # ["make", "model", "type", "drivetrain", "fuel_ec_mpge", "range_mi", "battery_kwh", "seats", "base_msrp"],
    # ["Tesla", "Model 3 RWD", "Sedan/Wagon", "RWD", "132", "272", "60", "5", "$46,990"],

    tesla_3_range = E_VEHICLES[-1][5]  # Tesla Model 3 AWD
    # print(f"\n7.4.1 Tesla Model 3 range (mpg) = {tesla_3_range}")

    # ["Tesla Model S", "Sedan/Wagon", "AWD", "120", "405", "104", "5", "$104,990"]

    tesla_s_range = 0
    for i in range(len(vehicles)):
        pass  # TODO: implement if block

    # print(f"\n7.4.2 Tesla Model S range (mpg) = {tesla_s_range}")

    # 7.5.1 CHALLENGE 09

    sedan_wagon = []
    suv_pickup = []

    # TODO refactor to use range()
    # for vehicle in vehicles:
    #     make_model = get_make_model(vehicle)
    #     if vehicle[headers.index("type")] == "Sedan/Wagon":
    #         sedan_wagon.append(make_model)
    #     else:
    #         suv_pickup.append(make_model)

    # TODO refactor loop to use range()

    # print(f"\n7.5.1 Sedan/Wagon (n={len(sedan_wagon)})")
    # pp.pprint(sedan_wagon)
    # print(f"\n7.5.1 SUV/Pickup (n={len(suv_pickup)})")
    # pp.pprint(suv_pickup)

    # 7.5.2 CHALLENGE 10

    ev_types = None # TODO call function
    # print(f"\n7.5.2 EV types = {ev_types}")
    # assert ev_types == ["Sedan/Wagon", "SUV", "Pickup"]

    # 7.5.1 CHALLENGE 11

    # TODO: Implement loop

    # print("\n7.5.3 vehicles modified (last 5)")
    # pp.pprint(vehicles[-5:])


if __name__ == "__main__":
    main()
