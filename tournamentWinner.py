
def tournamentWinner(competitions, results):

    currentWinningTeam = ""

    scores = { currentWinningTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]

        homeTeam, awayTeam = competition
        winningTeam = homeTeam if result == 1 else awayTeam

        updateScores(winningTeam, 3 , scores)

        if scores[winningTeam] > scores[currentWinningTeam]:
            currentWinningTeam = winningTeam


    return currentWinningTeam

def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += 3



print(tournamentWinner([
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ], [0, 0, 1]))