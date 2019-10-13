import re


def getEventsOrder(team1, team2, events1, events2):

    games = []
    original_events = []
    priority = ['G', 'Y', 'R', 'S']

    def helper(team, events):
        for event in events:
            original_events.append(team + " " + event)

            # split events string to get details
            pattern = re.compile("([a-zA-Z\s]*)(\d+)[+]?(\d*).([G,Y,R,S])([a-zA-Z\s]*)")
            split_event = pattern.search(event)

            # create a list of format ["team name", "player name", "time", "extra time", "event", "second player name"]
            record = []
            record.append(team)  # team name
            if split_event:
                record.append(split_event.group(1).strip())  # player name
                record.append(int(split_event.group(2).strip()))  # time
                record.append(
                    int(split_event.group(3).strip()) if len(split_event.group(3).strip()) > 0 else 0)  # extra time
                record.append(priority.index(split_event.group(4).strip()))  # event
                record.append(split_event.group(5).strip())  # second player
            games.append(record)

    helper(team1, events1)
    helper(team2, events2)

    # sorting the list to return index position of the sorted list
    new_num_index_sorted = (sorted(range(len(games)),
                                   key=lambda k: (
                                       games[k][2],  # time
                                       games[k][3],  # extra time
                                       games[k][4],  # event
                                       games[k][0],  # team name
                                       games[k][1],  # player name
                                       games[k][5])))

    # based on the index position, fetching result from original event list and appending in answer
    answer = []
    for i in new_num_index_sorted:
        answer.append(original_events[i])
    return answer

print(getEventsOrder('EDC', 'CDE', ['Name1 12 G', 'FirstName LastName 43 Y'], ['Name3 45+1 S SubName', 'Name4 46 G']))