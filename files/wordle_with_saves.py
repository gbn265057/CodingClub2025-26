import json
import pickle
import wordle

class Stats:
    def __init__(self, plays=0, wins=0, by_guess=None):
        self.plays = plays
        self.wins = wins
        if by_guess is None:
            self.by_guess = {n: 0 for n in range(1, 7)}
        else:
            self.by_guess = by_guess
    
    def __str__(self):
        return f"""Stats:
Games played: {self.plays}
Games won: {self.wins}
    in 1: {self.by_guess[1]}
    in 2: {self.by_guess[2]}
    in 3: {self.by_guess[3]}
    in 4: {self.by_guess[4]}
    in 5: {self.by_guess[5]}
    in 6: {self.by_guess[6]}"""

#----------------------------------------------------------

def play(stats):
    result = wordle.play_game()
    stats.plays += 1
    if result.won:
        stats.wins += 1
        stats.by_guess[result.guesses_used] += 1

#----------------------------------------------------------

def write_stats_as_text(stats, file):
    file.write(f"{stats.plays} {stats.wins}")
    for n in stats.by_guess.values():
        file.write(" " + str(n))

def load_stats_from_text(file):
    stats = file.read().split(" ")
    plays = int(stats[0])
    wins = int(stats[1])
    by_guess = {}
    for i in range(1, 7):
        by_guess[i] = int(stats[i+1])
    return Stats(plays, wins, by_guess)

#----------------------------------------------------------

def write_stats_as_pickle(stats, file):
    pickle.dump(stats, file)

def load_stats_from_pickle(file):
    return pickle.load(file)

#----------------------------------------------------------

def write_stats_as_json(stats, file):
    stats_dict = {
        "plays": stats.plays,
        "wins": stats.wins,
        "by_guess": stats.by_guess
    }

    json.dump(stats_dict, file)

def load_stats_from_json(file):
    stats_dict = json.load(file)
    
    by_guess = {}
    for k, v in stats_dict["by_guess"].items():
        by_guess[int(k)] = v
    
    stats_dict["by_guess"] = by_guess
    
    return Stats(**stats_dict)

#----------------------------------------------------------

if __name__ == "__main__":
    stats_method = input("What stats method? ")

    if stats_method == "none":
        stats = Stats()
    elif stats_method == "text":
        with open("stats.txt", "r") as stats_file:
            stats = load_stats_from_text(stats_file)
    elif stats_method == "pickle":
        with open("stats.pickle", "rb") as stats_file:
            stats = load_stats_from_pickle(stats_file)
    elif stats_method == "json":
        with open("stats.json", "r") as stats_file:
            stats = load_stats_from_json(stats_file)

    print(stats)

    while True:
        play(stats)
        print(stats)

        if input("Play again? y/n ") == "n":
            break
    
    if stats_method == "text":
        with open("stats.txt", "w") as stats_file:
            write_stats_as_text(stats, stats_file)
    elif stats_method == "pickle":
        with open("stats.pickle", "wb") as stats_file:
            write_stats_as_pickle(stats, stats_file)
    elif stats_method == "json":
        with open("stats.json", "w") as stats_file:
            write_stats_as_json(stats, stats_file)
