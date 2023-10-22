from collections import defaultdict


def team_lineup(*players_info):
    players_per_country = defaultdict(list)
    for player, country in players_info:
        players_per_country[country].append(player)

    result = ''
    for country, players in sorted(players_per_country.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result += f"{country}:"
        for player in players:
            result += f"\n  -{player}"
        result += f"\n"

    return result


def main():
    print(team_lineup(
        ("Harry Kane", "England"),
        ("Manuel Neuer", "Germany"),
        ("Raheem Sterling", "England"),
        ("Toni Kroos", "Germany"),
        ("Cristiano Ronaldo", "Portugal"),
        ("Thomas Muller", "Germany")))

    print(team_lineup(
        ("Lionel Messi", "Argentina"),
        ("Neymar", "Brazil"),
        ("Cristiano Ronaldo", "Portugal"),
        ("Harry Kane", "England"),
        ("Kylian Mbappe", "France"),
        ("Raheem Sterling", "England")))

    print(team_lineup(
        ("Harry Kane", "England"),
        ("Manuel Neuer", "Germany"),
        ("Raheem Sterling", "England"),
        ("Toni Kroos", "Germany"),
        ("Cristiano Ronaldo", "Portugal"),
        ("Thomas Muller", "Germany"),
        ("Bruno Fernandes", "Portugal"),
        ("Bernardo Silva", "Portugal"),
        ("Harry Maguire", "England")))


if __name__ == '__main__':
    main()
