# START PROBLEM SET 1
print("Problem Set 1 \n")

# PROBLEM 01
print("\nPROBLEM 01")

# 1frita_batidos = "Frita Batidos"
# zingerman's Delicatessen = "Zingerman's Delicatessen"
# nypd = New York Pizza Depot
hopcat = "HoPcAT"
fleetwood_diner = "Fleetwood Diner"
# tomukun_noodle_bar = "Tomukun Noodle Bar
jerk_pit = "JaMAIcaN JERk PIt"
# mama satto = "Mama Satto"
hola_seoul = "Hola Seoul"
# @shalimar = "Shalimar"

cottage_inn = "Cottage Inn Pizza"
print(cottage_inn)

madras_masala = "Madras Masala"
print(madras_masala)

# PROBLEM 02
print("\nPROBLEM 02")

hopcat_all_lower = hopcat.lower()
print(f"all_lower: {hopcat_all_lower}")

jerk_pit_all_upper = jerk_pit.upper()
print(f"all_upper: {jerk_pit_all_upper}")

madras_masala_count_m = madras_masala.count("m")
print(f"number of letter m: {madras_masala_count_m}")
# 寫到這裡
has_diner = fleetwood_diner.endswith("Diner")
print(has_diner)

starts_seoul = hola_seoul.startswith("Seoul")
print(starts_seoul)

comment = "Great Jamaican food&drinks"
updated_comment = comment.replace("&", " and ")
print(f"updated comment: {updated_comment}")  # Output: Great Jamaican food and drinks


# PROBLEM 03
print("\nPROBLEM 03")

num_chars = len(updated_comment)
print(f"number of characters: {num_chars}")

restaurants = [
    "Frita Batidos",
    "Zingerman's Delicatessen",
    "New York Pizza Depot",
    "Hopcat",
    "Fleetwood Diner",
    "Tomukun Noodle Bar",
    "Jamaican Jerk Pit",
    "Mama Satto",
    "Hola Seoul",
    "Shalimar",
    "Cottage Inn Pizza",
    "Madras Masala",
]

print(type(restaurants))

num_restaurants = len(restaurants)
print(f"number of restaurants: {num_restaurants}")

# PROBLEM 04
print("\nPROBLEM 04")

total_price = 4 * 18.99 + 5 * 6.99 + 2 * 7.00 + 5 * 10.49 + 1 * 22.25 + 2 * 17.99
print(f"total price: {total_price}")


total_bill = total_price + (total_price * 0.06) + (total_price * 0.15)
print(f"total bill: {total_bill}")

each_pay = total_bill / 7
print(f"each person pays: {each_pay}")


# PROBLEM 05
print("\nPROBLEM 05")

# TODO: Create f-string
# updated_comment = "Truly authentic Jamaican food and drinks"
# formatted_comment = updated_comment.replace("Great Jamaican", "Truly authentic Jamaican")
jerk_pit_all_upper = jerk_pit.upper()

print(f"Someone said '{updated_comment}' on Yelp for the restaurant {jerk_pit_all_upper}.")

# PROBLEM 06
print("\nPROBLEM 06")

total_orders = 120 + 95 + 80 + 45 + 60 + 30  # 430 total orders


def calc_pct(orders_of_spec_dish, total_orders):
    percentage = (orders_of_spec_dish / total_orders) * 100  # Calculate the percentage
    return round(percentage, 2)  # Round the result to two decimal places and return it


jerk_pork_pct = calc_pct(120, total_orders)
coconut_shrimp_pct = calc_pct(95, total_orders)
jerk_wings_pct = calc_pct(80, total_orders)
caesar_salad_pct = calc_pct(45, total_orders)
jerk_tofu_pct = calc_pct(60, total_orders)
oxtail_pct = calc_pct(30, total_orders)

print(
    jerk_pork_pct, coconut_shrimp_pct, jerk_wings_pct, caesar_salad_pct, jerk_tofu_pct, oxtail_pct
)


# PROBLEM 07
print("\nPROBLEM 07")

review = """First time trying Jamaican Jerk Pit, and it was a lovely experience. There is seating on
the ground floor when you walk in with additional seating downstairs. The waitress welcomed us and
provided thorough and very helpful recommendations to make our first visit well worth it. Ordered
the curry goat and Jamaican chicken and both were packed with flavor with the meat easily
falling off the bones. Mixing in the sauce with the rice was a great idea too. Festivals were
strangely addicting. Very simple in appearance and taste but I couldn't stop eating them. Crispy
on the outside, soft in the inside. I have had fried plantains with sugar before and it was as
expected. I would recommend!
"""

total_chars = len(review)
print(f"\n7.1 total characters: {total_chars}")

sentence_count = review.count(".") + review.count("!")
print(f"\n7.2 total sentences: {sentence_count}")


# END PROBLEM SET
