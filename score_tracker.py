scores = {
    "Ryan": 5,
    "Mia": 8,
    "Jay": 3
}

print("Current Scores:")
for player in scores:
    print(player, "has", scores[player], "points")

winner = input("\nWho won a point? ")

if winner in scores:
    scores[winner] = scores[winner] + 1
    print(winner, "now has", scores[winner], "points!")

print("\nFinal Scores:")
for player in scores:
    print(player + ":", scores[player])
