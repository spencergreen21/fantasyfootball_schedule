def generate_schedule(num_teams):
    if num_teams % 2 != 0:
        num_teams += 1

    teams = list(range(1, num_teams + 1))
    schedule = {}
    rounds = []
    mid_point = len(teams) // 2

    for i in range(num_teams - 1):
        round = []
        for j in range(mid_point):
            match = (teams[j], teams[num_teams - 1 - j])
            round.append(match)
        rounds.append(round)

        teams = [teams[0]] + [teams[-1]] + teams[1:-1]

    for week, round_matches in enumerate(rounds, start=1):
        schedule[week] = round_matches

    return schedule

def print_schedule(schedule):
    for week, week_matches in schedule.items():
        print(f"Week {week}: {', '.join([f'Team {match[0]} vs Team {match[1]}' for match in week_matches])}")


num_teams = 12
schedule = generate_schedule(num_teams)
print_schedule(schedule)
