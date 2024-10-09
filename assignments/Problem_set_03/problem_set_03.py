# START PROBLEM SET 03

# Setup Code (DO NOT MODIFY)

TV_SHOWS = [
    "Only Murders in the Building | Comedy | 2021 | 8.1 | 99 | Hulu",
    "Reservation Dogs | Crime | 2021 | 8.1 | 99 | Hulu",
    "Suits | Drama | 2011 | 8.5 | 90 | Netflix",
    "Better Things | Comedy | 2016 | 7.8 | 98 | Hulu",
    "Grey's Anatomy | Drama | 2005 | 7.6 | 84 | hulu",
    "Atlanta | comedy | 2016 | 8.6 | 99 | Hulu",
    "The Bold Type | drama | 2017 | 7.8 | 89 | Hulu",
    "Virgin River | Drama | 2019 | 7.4 | 84 | Netflix",
    "What We Do in the Shadows | Horror | 2019 | 8.9 | 92 | Hulu",
    "American Horror Story | Horror | 2011 | 8.0 | 77 | Hulu",
    "Yellowjackets | horror | 2021 | 7.9 | 100 | Hulu",
    "Bridgerton | Drama | 2020 | 7.3 | 82 | Netflix",
    "Stranger Things | Scifi | 2016 | 8.7 | 96 | Netflix",
    "Dark | Thriller | 2017 | 8.8 | 93 | Netflix",
    "The Queen's Gambit | Drama | 2020 | 8.6 | 92 | Netflix",
    "Mindhunter | thriller | 2017 | 8.6 | 90 | Netflix",
    "Money Heist | Crime | 2017 | 8.5 | 90 | Netflix",
    "The Umbrella Academy | Comedy | 2019 | 7.9 | 86 | Netflix",
    "The Witcher | fantasy | 2019 | 8.2 | 89 | Netflix",
    "Ozark | Crime | 2017 | 8.4 | 89 | Netflix",
    "The Crown | Drama | 2016 | 8.6 | 89 | Netflix",
    "Cobra Kai | Comedy | 2018 | 8.6 | 89 | Netflix",
    "The Good Place | Comedy | 2016 | 8.2 | 97 | Netflix",
    "The Family Man | Thriller | 2019 | 8.7 | 100 | prime",
    "On My Block | Drama | 2018 | 7.9 | 93 | Netflix",
    "Band of Brothers | Drama | 2001 | 9.4 | 97 | Prime",
    "Breaking Bad | Crime | 2008 | 9.5 | 96 | Netflix",
    "Peaky Blinders | Crime | 2013 | 8.8 | 93 | Netflix",
    "Lost in Space | Scifi | 2018 | 7.3 | 84 | Netflix",
    "The Marvelous Mrs. Maisel | Comedy | 2017 | 8.7 | 89 | Prime",
    "As We See It | Comedy | 2022 | 9.1 | 90 | Prime",
    "The Cleaning Lady | crime | 2022 | 7.0 | 60 | Prime",
    "The Lord of the Rings: The Rings of Power | Fantasy | 2022 | 6.9 | 84 | Prime",
    "The Wheel of Time | Fantasy | 2021 | 7.1 | 82 | Prime",
    "Fleabag | Drama | 2016 | 8.7 | 100 | Prime",
    "Star Trek: The Next Generation | Scifi | 1987 | 8.7 | 92 | Prime",
    "Panchayat | Comedy | 2020 | 8.9 | 80 | Prime",
    "Severence | Thriller | 2022 | 8.7 | 97 | AppleTV",
    "Trying | Comedy | 2021 | 7.9 | 93 | AppleTV",
    "The Morning Show | Drama | 2019 | 8.2 | 64 | AppleTV",
    "For All Mankind | Scifi | 2019 | 8.0 | 90 | AppleTV",
    "Dickinson | comedy | 2019 | 7.6 | 92 | AppleTV",
    "See | Scifi | 2019 | 7.6 | 63 | AppleTV",
    "How I Caught My Killer | Docu-series | 2023 | 5.5 | 40 | hulu",
    "The Dropout | Drama | 2022 | 7.5 | 90 | hulu",
    "Inventing Anna | Drama | 2022 | 6.8 | 64 | Netflix",
    "One Piece | Action | 2023 | 8.5 | 85 | netflix",
    "The Ultimatum: Marry or Move On | Reality | 2022 | 5.5 | 42 | Netflix",
    "The Real Housewives of Dubai | reality | 2022 | 3.8 | 74 | Appletv",
    "The Afterparty | Comedy | 2022 | 7.3 | 92 | AppleTV",
    "The Summer I Turned Pretty | Drama | 2022 | 7.4 | 74 | Prime",
    "Pinecone & Pony | Adventure | 2022 | 8.1 | 68 | AppleTV",
    "Extraordinary Attorney Woo | drama | 2022 | 8.7 | 100 | netflix",
    "Beef | comedy | 2023 | 8 | 98 | netflix",
    "Percy Jackson And The Olympians | Fantasy | 2023 | 7.4 | 96 | hulu",
]

NEW_TV_SHOWS = [
    ["Fool Me Once", "crime", "2024", "6.9", "67", "netflix"],
    ["Criminal Record", "drama", "2024", "7.2", "90", "appleTV"],
    ["Hazbin Hotel", "Comedy", "2024", "7.7", "88", "prime"],
    ["Dark Matter", "Scifi", "2024", "7.7", "83", "appleTV"],
    ["Manhunt", "fiction", "2024", "7.2", "88", "appleTV"],
    ["Women in Blue", "crime", "2024", "6.9", "100", "appleTV"],
]

COMBINED_TV_SHOWS_CHECK = [
    ["Fool Me Once", "crime", "2024", "6.9", "67", "netflix"],
    ["Criminal Record", "drama", "2024", "7.2", "90", "appleTV"],
    ["Hazbin Hotel", "Comedy", "2024", "7.7", "88", "prime"],
    ["Dark Matter", "Scifi", "2024", "7.7", "83", "appleTV"],
    ["Manhunt", "fiction", "2024", "7.2", "88", "appleTV"],
    ["Women in Blue", "crime", "2024", "6.9", "100", "appleTV"],
    ["Only Murders in the Building", "Comedy", "2021", "8.1", "99", "Hulu"],
    ["Reservation Dogs", "Crime", "2021", "8.1", "99", "Hulu"],
    ["Suits", "Drama", "2011", "8.5", "90", "Netflix"],
    ["Better Things", "Comedy", "2016", "7.8", "98", "Hulu"],
    ["Grey's Anatomy", "Drama", "2005", "7.6", "84", "hulu"],
    ["Atlanta", "comedy", "2016", "8.6", "99", "Hulu"],
    ["The Bold Type", "drama", "2017", "7.8", "89", "Hulu"],
    ["Virgin River", "Drama", "2019", "7.4", "84", "Netflix"],
    ["What We Do in the Shadows", "Horror", "2019", "8.9", "92", "Hulu"],
    ["American Horror Story", "Horror", "2011", "8.0", "77", "Hulu"],
    ["Yellowjackets", "horror", "2021", "7.9", "100", "Hulu"],
    ["Bridgerton", "Drama", "2020", "7.3", "82", "Netflix"],
    ["Stranger Things", "Scifi", "2016", "8.7", "96", "Netflix"],
    ["Dark", "Thriller", "2017", "8.8", "93", "Netflix"],
    ["The Queen's Gambit", "Drama", "2020", "8.6", "92", "Netflix"],
    ["Mindhunter", "thriller", "2017", "8.6", "90", "Netflix"],
    ["Money Heist", "Crime", "2017", "8.5", "90", "Netflix"],
    ["The Umbrella Academy", "Comedy", "2019", "7.9", "86", "Netflix"],
    ["The Witcher", "fantasy", "2019", "8.2", "89", "Netflix"],
    ["Ozark", "Crime", "2017", "8.4", "89", "Netflix"],
    ["The Crown", "Drama", "2016", "8.6", "89", "Netflix"],
    ["Cobra Kai", "Comedy", "2018", "8.6", "89", "Netflix"],
    ["The Good Place", "Comedy", "2016", "8.2", "97", "Netflix"],
    ["The Family Man", "Thriller", "2019", "8.7", "100", "prime"],
    ["On My Block", "Drama", "2018", "7.9", "93", "Netflix"],
    ["Band of Brothers", "Drama", "2001", "9.4", "97", "Prime"],
    ["Breaking Bad", "Crime", "2008", "9.5", "96", "Netflix"],
    ["Peaky Blinders", "Crime", "2013", "8.8", "93", "Netflix"],
    ["Lost in Space", "Scifi", "2018", "7.3", "84", "Netflix"],
    ["The Marvelous Mrs. Maisel", "Comedy", "2017", "8.7", "89", "Prime"],
    ["As We See It", "Comedy", "2022", "9.1", "90", "Prime"],
    ["The Cleaning Lady", "crime", "2022", "7.0", "60", "Prime"],
    ["The Lord of the Rings: The Rings of Power", "Fantasy", "2022", "6.9", "84", "Prime"],
    ["The Wheel of Time", "Fantasy", "2021", "7.1", "82", "Prime"],
    ["Fleabag", "Drama", "2016", "8.7", "100", "Prime"],
    ["Star Trek: The Next Generation", "Scifi", "1987", "8.7", "92", "Prime"],
    ["Panchayat", "Comedy", "2020", "8.9", "80", "Prime"],
    ["Severence", "Thriller", "2022", "8.7", "97", "AppleTV"],
    ["Trying", "Comedy", "2021", "7.9", "93", "AppleTV"],
    ["The Morning Show", "Drama", "2019", "8.2", "64", "AppleTV"],
    ["For All Mankind", "Scifi", "2019", "8.0", "90", "AppleTV"],
    ["Dickinson", "comedy", "2019", "7.6", "92", "AppleTV"],
    ["See", "Scifi", "2019", "7.6", "63", "AppleTV"],
    ["How I Caught My Killer", "Docu-series", "2023", "5.5", "40", "hulu"],
    ["The Dropout", "Drama", "2022", "7.5", "90", "hulu"],
    ["Inventing Anna", "Drama", "2022", "6.8", "64", "Netflix"],
    ["One Piece", "Action", "2023", "8.5", "85", "netflix"],
    ["The Ultimatum: Marry or Move On", "Reality", "2022", "5.5", "42", "Netflix"],
    ["The Real Housewives of Dubai", "reality", "2022", "3.8", "74", "Appletv"],
    ["The Afterparty", "Comedy", "2022", "7.3", "92", "AppleTV"],
    ["The Summer I Turned Pretty", "Drama", "2022", "7.4", "74", "Prime"],
    ["Pinecone & Pony", "Adventure", "2022", "8.1", "68", "AppleTV"],
    ["Extraordinary Attorney Woo", "drama", "2022", "8.7", "100", "netflix"],
    ["Beef", "comedy", "2023", "8", "98", "netflix"],
    ["Percy Jackson And The Olympians", "Fantasy", "2023", "7.4", "96", "hulu"],
]

CLEANED_TV_SHOWS_CHECK = [
    ["Fool Me Once", "crime", "2024", 6.9, 67.0, "netflix"],
    ["Criminal Record", "drama", "2024", 7.2, 90.0, "appleTV"],
    ["Hazbin Hotel", "Comedy", "2024", 7.7, 88.0, "prime"],
    ["Dark Matter", "Scifi", "2024", 7.7, 83.0, "appleTV"],
    ["Manhunt", "fiction", "2024", 7.2, 88.0, "appleTV"],
    ["Women in Blue", "crime", "2024", 6.9, 100.0, "appleTV"],
    ["Only Murders in the Building", "Comedy", "2021", 8.1, 99.0, "Hulu"],
    ["Reservation Dogs", "Crime", "2021", 8.1, 99.0, "Hulu"],
    ["Suits", "Drama", "2011", 8.5, 90.0, "Netflix"],
    ["Better Things", "Comedy", "2016", 7.8, 98.0, "Hulu"],
    ["Grey's Anatomy", "Drama", "2005", 7.6, 84.0, "hulu"],
    ["Atlanta", "comedy", "2016", 8.6, 99.0, "Hulu"],
    ["The Bold Type", "drama", "2017", 7.8, 89.0, "Hulu"],
    ["Virgin River", "Drama", "2019", 7.4, 84.0, "Netflix"],
    ["What We Do in the Shadows", "Horror", "2019", 8.9, 92.0, "Hulu"],
    ["American Horror Story", "Horror", "2011", 8.0, 77.0, "Hulu"],
    ["Yellowjackets", "horror", "2021", 7.9, 100.0, "Hulu"],
    ["Bridgerton", "Drama", "2020", 7.3, 82.0, "Netflix"],
    ["Stranger Things", "Scifi", "2016", 8.7, 96.0, "Netflix"],
    ["Dark", "Thriller", "2017", 8.8, 93.0, "Netflix"],
    ["The Queen's Gambit", "Drama", "2020", 8.6, 92.0, "Netflix"],
    ["Mindhunter", "thriller", "2017", 8.6, 90.0, "Netflix"],
    ["Money Heist", "Crime", "2017", 8.5, 90.0, "Netflix"],
    ["The Umbrella Academy", "Comedy", "2019", 7.9, 86.0, "Netflix"],
    ["The Witcher", "fantasy", "2019", 8.2, 89.0, "Netflix"],
    ["Ozark", "Crime", "2017", 8.4, 89.0, "Netflix"],
    ["The Crown", "Drama", "2016", 8.6, 89.0, "Netflix"],
    ["Cobra Kai", "Comedy", "2018", 8.6, 89.0, "Netflix"],
    ["The Good Place", "Comedy", "2016", 8.2, 97.0, "Netflix"],
    ["The Family Man", "Thriller", "2019", 8.7, 100.0, "prime"],
    ["On My Block", "Drama", "2018", 7.9, 93.0, "Netflix"],
    ["Band of Brothers", "Drama", "2001", 9.4, 97.0, "Prime"],
    ["Breaking Bad", "Crime", "2008", 9.5, 96.0, "Netflix"],
    ["Peaky Blinders", "Crime", "2013", 8.8, 93.0, "Netflix"],
    ["Lost in Space", "Scifi", "2018", 7.3, 84.0, "Netflix"],
    ["The Marvelous Mrs. Maisel", "Comedy", "2017", 8.7, 89.0, "Prime"],
    ["As We See It", "Comedy", "2022", 9.1, 90.0, "Prime"],
    ["The Cleaning Lady", "crime", "2022", 7.0, 60.0, "Prime"],
    ["The Lord of the Rings: The Rings of Power", "Fantasy", "2022", 6.9, 84.0, "Prime"],
    ["The Wheel of Time", "Fantasy", "2021", 7.1, 82.0, "Prime"],
    ["Fleabag", "Drama", "2016", 8.7, 100.0, "Prime"],
    ["Star Trek: The Next Generation", "Scifi", "1987", 8.7, 92.0, "Prime"],
    ["Panchayat", "Comedy", "2020", 8.9, 80.0, "Prime"],
    ["Severence", "Thriller", "2022", 8.7, 97.0, "AppleTV"],
    ["Trying", "Comedy", "2021", 7.9, 93.0, "AppleTV"],
    ["The Morning Show", "Drama", "2019", 8.2, 64.0, "AppleTV"],
    ["For All Mankind", "Scifi", "2019", 8.0, 90.0, "AppleTV"],
    ["Dickinson", "comedy", "2019", 7.6, 92.0, "AppleTV"],
    ["See", "Scifi", "2019", 7.6, 63.0, "AppleTV"],
    ["How I Caught My Killer", "Docu-series", "2023", 5.5, 40.0, "hulu"],
    ["The Dropout", "Drama", "2022", 7.5, 90.0, "hulu"],
    ["Inventing Anna", "Drama", "2022", 6.8, 64.0, "Netflix"],
    ["One Piece", "Action", "2023", 8.5, 85.0, "netflix"],
    ["The Ultimatum: Marry or Move On", "Reality", "2022", 5.5, 42.0, "Netflix"],
    ["The Real Housewives of Dubai", "reality", "2022", 3.8, 74.0, "Appletv"],
    ["The Afterparty", "Comedy", "2022", 7.3, 92.0, "AppleTV"],
    ["The Summer I Turned Pretty", "Drama", "2022", 7.4, 74.0, "Prime"],
    ["Pinecone & Pony", "Adventure", "2022", 8.1, 68.0, "AppleTV"],
    ["Extraordinary Attorney Woo", "drama", "2022", 8.7, 100.0, "netflix"],
    ["Beef", "comedy", "2023", 8.0, 98.0, "netflix"],
    ["Percy Jackson And The Olympians", "Fantasy", "2023", 7.4, 96.0, "hulu"],
]


def convert_to_list(show, delimiter):
    # TODO 1.1
    return show.split(delimiter)


def clean_list(list_):
    # Loop through each nested list in the input list
    for i in range(len(list_)):
        list_[i][3] = float(list_[i][3])
        list_[i][4] = float(list_[i][4])
    return list_


def filter_list(list_, filter, filter_idx):
    # TODO 2.1
    filtered_shows = []
    for i in range(len(list_)):
        if list_[i][filter_idx].lower() == filter.lower():
            filtered_shows.append(list_[i])
    return filtered_shows


def get_oldest_show(list_):
    # TODO 7.1
    min_year = float("inf")
    oldest_show = ""
    for shows in list_:
        year = int(shows[2])
        if year < min_year:
            min_year = year
            oldest_show = shows[0]
    return oldest_show


def get_unique_elements(list_, idx):
    # TODO 8.1
    unique_elements = []
    for i in range(len(list_)):
        if list_[i][idx].lower() not in unique_elements:
            unique_elements.append(list_[i][idx].lower())
    return unique_elements


def main():
    print("\nPROBLEM SET 03\n")

    # PROBLEM 1
    print("\nPROBLEM 01")

    # TODO 1.1
    # Implement the function convert_to_list()
    # convert_to_list(TV_SHOWS, delimiter = ", ")

    # TODO 1.2
    combined_tv_shows = []

    # TODO 1.3
    combined_tv_shows.extend(NEW_TV_SHOWS)
    print(f"\n1.3: combined_tv_shows (first 5 elements) = {combined_tv_shows[:5]}")

    # TODO 1.5
    for show in TV_SHOWS:
        show_list = convert_to_list(show, " | ")  # Lowercase platform
        combined_tv_shows.append(show_list)

    print(f"\n1.5: combined_tv_shows (first 5 elements) = {combined_tv_shows[:5]}")
    assert combined_tv_shows == COMBINED_TV_SHOWS_CHECK

    # TODO 1.7
    # Implement the function clean_list()

    # TODO 1.8
    cleaned_tv_shows = clean_list(combined_tv_shows)

    print(f"\n1.8: cleaned_tv_shows (first 5 elements) = {cleaned_tv_shows[:5]}")
    assert cleaned_tv_shows == CLEANED_TV_SHOWS_CHECK

    # PROBLEM 2
    print("\nPROBLEM 02")

    # TODO 2.1
    # Implement the function filter_list()

    # TODO 2.2
    scifi_tv_shows = []
    # TODO 2.3
    scifi_tv_shows = filter_list(cleaned_tv_shows, "scifi", 1)

    print(f"\n2.3: scifi_tv_shows = {scifi_tv_shows}")
    assert scifi_tv_shows == [
        ["Dark Matter", "Scifi", "2024", 7.7, 83.0, "appleTV"],
        ["Stranger Things", "Scifi", "2016", 8.7, 96.0, "Netflix"],
        ["Lost in Space", "Scifi", "2018", 7.3, 84.0, "Netflix"],
        ["Star Trek: The Next Generation", "Scifi", "1987", 8.7, 92.0, "Prime"],
        ["For All Mankind", "Scifi", "2019", 8.0, 90.0, "AppleTV"],
        ["See", "Scifi", "2019", 7.6, 63.0, "AppleTV"],
    ]

    # TODO 2.5
    netflix_tv_shows = filter_list(cleaned_tv_shows, "netflix", 5)

    netflix_new_tv_shows = filter_list(netflix_tv_shows, "2024", 2)

    print(f"\n2.5: netflix_new_tv_shows = {netflix_new_tv_shows}")
    assert netflix_new_tv_shows == [["Fool Me Once", "crime", "2024", 6.9, 67.0, "netflix"]]

    # PROBLEM 3
    print("\nPROBLEM 03")

    # TODO 3.1
    crime_tv_shows = []

    # TODO 3.2
    crime_tv_shows = filter_list(cleaned_tv_shows, "crime", 1)
    # print(crime_tv_shows)
    # TODO 3.3
    crime_tv_shows_focused = []

    # TODO 3.4
    for shows in crime_tv_shows:
        # crime_tv_shows_focused.append([shows[0], shows[2], shows[4]])
        crime_tv_shows_focused.append(shows[::2])

    print(f"\n3.4: crime_tv_shows_focused = {crime_tv_shows_focused}")
    assert crime_tv_shows_focused == [
        ["Fool Me Once", "2024", 67.0],
        ["Women in Blue", "2024", 100.0],
        ["Reservation Dogs", "2021", 99.0],
        ["Money Heist", "2017", 90.0],
        ["Ozark", "2017", 89.0],
        ["Breaking Bad", "2008", 96.0],
        ["Peaky Blinders", "2013", 93.0],
        ["The Cleaning Lady", "2022", 60.0],
    ]

    # PROBLEM 4
    print("\nPROBLEM 04")

    # TODO 4.1
    select_content = []
    non_select_content = []

    # TODO 4.2
    for i in range(len(cleaned_tv_shows)):
        if cleaned_tv_shows[i][5].lower() == "hulu":
            select_content.append(cleaned_tv_shows[i])
        else:
            non_select_content.append(cleaned_tv_shows[i])
    print(f"\n4.2: select_content (first 5 elements) = {select_content[:5]}")
    print(f"\n4.2: non_select_content (first 5 elements) = {non_select_content[:5]}")

    # PROBLEM 5
    print("\nPROBLEM 05")

    # TODO 5.1
    total_rotten_tomato_ratings = 0
    # TODO 5.2
    for i in cleaned_tv_shows:
        total_rotten_tomato_ratings += i[4]
    print(f"\n5.2: total_ratings = {total_rotten_tomato_ratings}")

    # TODO 5.3
    avg_rotten_tomato_ratings = round(total_rotten_tomato_ratings / len(cleaned_tv_shows), 1)
    print(f"\n5.3: average rating = {avg_rotten_tomato_ratings}")

    # PROBLEM 6
    print("\nPROBLEM 06")

    # TODO 6.1
    above_avg_rotten_tomato_rating_shows = []
    avg_rotten_tomato_rating_shows = []
    below_avg_rotten_tomato_rating_shows = []

    # TODO 6.2
    for shows in cleaned_tv_shows:
        if shows[4] > avg_rotten_tomato_ratings:
            above_avg_rotten_tomato_rating_shows.append(shows[0])
        elif shows[4] == avg_rotten_tomato_ratings:
            avg_rotten_tomato_rating_shows.append(shows[0])
        else:
            below_avg_rotten_tomato_rating_shows.append(shows[0])

    print(
        f"\n6.2: above average shows (first 5 elements) = {above_avg_rotten_tomato_rating_shows[:5]}"
    )
    print(f"\n6.2: average shows (first 5 elements) = {avg_rotten_tomato_rating_shows[:5]}")
    print(
        f"\n6.2: below average shows (first 5 elements) = {below_avg_rotten_tomato_rating_shows[:5]}"
    )

    # PROBLEM 7
    print("\nPROBLEM 07")

    # TODO 7.1
    # Implement the function get_oldest_show()

    # TODO 7.2
    oldest_show = get_oldest_show(cleaned_tv_shows)
    print(f"\n7.2: The oldest show is {oldest_show}.")

    # PROBLEM 8
    print("\nPROBLEM 08")

    # TODO 8.1
    # Implement the function get_unique_elements()
    genres = get_unique_elements(cleaned_tv_shows, 1)
    # TODO 8.2

    print(f"\n8.2: unique genres list = {genres}")
    assert genres == [
        "crime",
        "drama",
        "comedy",
        "scifi",
        "fiction",
        "horror",
        "thriller",
        "fantasy",
        "docu-series",
        "action",
        "reality",
        "adventure",
    ]

    # END PROBLEM SET 03


# WARN: do not modify or remove the following if statement.

if __name__ == "__main__":
    main()
