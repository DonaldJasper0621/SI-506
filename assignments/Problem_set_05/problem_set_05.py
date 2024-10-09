import csv
from pathlib import Path
import pprint


def clean_squad(squad):
    """Converts a player's "Squad" value (e.g. "es Spain") to a two-item tuple
    comprising the following items:

    1  Upper case two-letter country abbreviation (e.g., "ES")
    2. squad name (e.g., "Spain")

    Parameters:
        squad (str): comprises a two-letter country abbreviation and squad name

    Returns:
        tuple: "Squad" element converted to a two-item tuple
    """

    # TODO 2.2
    return (squad[0:2].upper(), squad[3:])


def format_player_position(position):
    """Reformats player's position string by converting the comma (",") delimiter that
    separates multiple positions to a pipe (|), e.g., "MF,DF" -> "MF|DF". This change
    eliminates the need to surround the position string with double quotes when writing the
    value to a CSV file.

    Parameters:
        position (str): player's position string

    Returns:
        str: reformatted position string
    """

    # TODO 2.1
    return position.replace(",", "|")


def get_multi_position_players(players, pos_idx):
    """Returns players who play multiple positions. Evaluates the "Pos" element
    for the presence of multiple positions (e.g., "DF", "FW", "GK", "MF").

    Parameters:
        players (list): nested list of player data
        pos_idx (int): index value of the "Pos" element

    Returns:
        list: nested list of players who play multiple positions
    """

    # TODO 4.1
    multi_position_players = []
    for player in players:
        positions = player[pos_idx].split("|")
        if len(positions) > 1:
            multi_position_players.append(player)
    return multi_position_players


def get_player_shooting_numbers(player, slice_):
    """Returns a player's shots, shots on target, and goals scored. All values
    are converted from strings to integers before being returned to the caller.

    Parameters:
        player (list): a list containing player data
        slice_ (slice): slice() instance required to access the shooting-related
                        elements in the player list.

    Returns:
        list: player's shooting statistics (shots, shots on target, and goals)
    """

    # TODO 8.1
    shooting_numbers = player[slice_]

    for i in range(len(shooting_numbers)):
        shooting_numbers[i] = int(shooting_numbers[i])
    return shooting_numbers


def get_team(players, squad_idx, squad):
    """Returns members of a country's team.

    Parameters:
        players (list): nested list of player data
        squad_idx (int): index value of the "Squad" element
        squad (str): country/squad name

    Returns:
        list: team members who represent the < squad >
    """

    # TODO 5.1
    country_team_members = []
    for player in players:
        if player[squad_idx].lower() == squad.lower():
            country_team_members.append(player)
    return country_team_members


def get_team_names(players, squad_idx):
    """Returns a list of team/squad names that correspond to the countries participating
    in the World Cup. Duplicate names are filtered out of the list returned to the caller.

    Parameters:
        players (list): nested list of player data
        squad_idx (int): index value of the "Squad" element

    Returns:
        list: countries represented by the players in the < players > list
    """

    # TODO 7.1
    team_names = []
    for player in players:
        if player[squad_idx] not in team_names:
            team_names.append(player[squad_idx])
    return team_names


def get_top_scorer(players, gls_idx):
    """Returns the top scorer from the < players > list. Filters out players
    that did not score a goal and excludes them from consideration. Ties between
    top scorers are accommodated.

    Parameters:
        players (list): nested list of player data
        gls_idx (int): index value of a nested list's "Gls" element

    Returns:
        list: nested list of one or more top scorers
    """

    # TODO 6.1
    top_scorer_list = []
    max_goals = 0
    for player in players:
        goals = int(player[gls_idx])
        if goals > 0 and goals > max_goals:
            max_goals = goals
            top_scorer_list.clear()
            top_scorer_list.append(player)
        elif goals > 0 and goals == max_goals:
            top_scorer_list.append(player)
    return top_scorer_list


def read_csv(filepath, encoding="utf-8", newline="", delimiter=","):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
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


def write_csv(filepath, data, headers=None, encoding="utf-8", newline=""):
    """
    Writes data to a target CSV file. Column headers are written as the first
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


def main():
    """Program entry point. Orchestrates workflow.

    Parameters:
        None

    Returns:
        None
    """
    print("Problem Set 5 \n")

    # PROBLEM 01
    print("\nPROBLEM 1")

    # TODO 1.1
    filepath = Path("data-2023-fifa_wwc-players.csv").resolve()
    # TODO 1.2
    data = read_csv(filepath)
    pp = pprint.PrettyPrinter(indent=1, compact=True, width=100)
    pp.pprint(data)
    # TODO 1.3
    for i in range(len(data)):
        data[i] = data[i][:10]  # [包含:不包含]
    # TODO 1.4
    headers = data[0]
    players = data[1:]
    # TODO 1.5
    print(f"\n1.4 data[0] = {headers}")  # headers
    print(f"\n1.4 data[-1] = {players[-1]}")  # last player
    assert headers == ["Rk", "Player", "Pos", "Squad", "Age", "Born", "90s", "Gls", "Sh", "SoT"]
    assert players[-1] == [
        "619",
        "Claudia Zornoza",
        "MF",
        "es Spain",
        "32",
        "1990",
        "0.4",
        "0",
        "0",
        "0",
    ]

    # PROBLEM 02
    print("\nPROBLEM 2")

    # TODO 2.1
    assert "MF|DF" == format_player_position("MF,DF")
    assert "GK" == format_player_position("GK")

    # TODO 2.2
    assert ("NG", "Nigeria") == clean_squad("ng Nigeria")
    assert ("ZA", "South Africa") == clean_squad("za South Africa")

    # PROBLEM 03
    print("\nPROBLEM 3")

    # TODO 3.1

    pos_idx = headers.index("Pos")
    squad_idx = headers.index("Squad")
    # print(squad_idx)
    # TODO 3.2

    for player in players:
        player[pos_idx] = format_player_position(player[pos_idx])
        code, squad = clean_squad(player[squad_idx])
        player.insert(squad_idx, code)
        player[squad_idx + 1] = squad

    # TODO 3.3
    headers.insert(squad_idx, "Country_Code")  # headers.insert(3, "Country_Code")
    # TODO 3.4
    squad_idx += 1
    # TODO 3.5
    write_csv("stu-players.csv", players, headers)
    # PROBLEM 04
    print("\nPROBLEM 4")

    # TODO 4.2
    multi_position_players = get_multi_position_players(players, pos_idx)
    # TODO 4.3
    write_csv("stu-players-multi_position.csv", multi_position_players, headers)
    # PROBLEM 05
    print("\nPROBLEM 5")

    # TODO 5.2
    team_china = get_team(players, squad_idx, "China PR")
    # TODO 5.3
    write_csv("stu-team-china.csv", team_china, headers)

    # PROBLEM 06
    print("\nPROBLEM 6")

    # TODO 6.2
    gls_idx = headers.index("Gls")
    # TODO 6.3
    top_scorers = get_top_scorer(players, gls_idx)
    # TODO 6.4
    print(f"\n6.4 top scorer(s) (n={len(top_scorers)}) = {top_scorers}")

    # PROBLEM 07
    print("\nPROBLEM 7")

    # TODO 7.2
    countries = get_team_names(players, squad_idx)
    # TODO 7.3
    countries.sort()
    # TODO 7.4
    print(f"\n7.4 countries = {countries}")
    assert len(countries) == 32

    # TODO 7.5-9
    team_top_scorers = []
    for country in countries:
        team = get_team(players, squad_idx, country)
        top_scorers = get_top_scorer(team, gls_idx)
        team_top_scorers.extend(top_scorers)  # 因為已經是list, list加list用extend
    # TODO 7.10
    write_csv("stu-team-top_scorers.csv", team_top_scorers, headers)
    # PROBLEM 08
    print("\nPROBLEM 8")

    # TODO 8.2 UNCOMMENT: built-in slice(< start >, < start >, < step >=None) object in action!
    slice_ = slice(gls_idx, len(headers))  #  equivalent to slice(8, 11) #slice_(包含,不包含)

    # TODO 8.3
    goals, shots, shots_on_target = get_player_shooting_numbers(players[0], slice_)
    # TODO 8.4
    print(
        f"\n8.4 goals = {goals}",
        f"shots = {shots}",
        f"shots_on_target = {shots_on_target}",
        sep="\n",
    )
    assert goals == 1
    assert shots == 10
    assert shots_on_target == 4


if __name__ == "__main__":
    main()
