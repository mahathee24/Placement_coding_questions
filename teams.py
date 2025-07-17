#enter the number of teams and all teams and one of meeting and the ans should be match1:ind vs australia , india vs pakistan and india vs srilanka 
#same later the loop goes on 
teams = int(input("Enter the number of teams: "))
matches = []
meetings = []
for i in range(teams):
    a = input(f"Enter the name of team: ")
    matches.append(a)
for i in range(teams - 1):
    meet = input(f"Enter the name of meeting {i + 1}: ")
    meetings.append(meet)

match = []
for i in range(teams):
    for j in range(i + 1, teams):
        for k in range(len(meetings)):
            match.append(f"{matches[i]} vs {matches[j]} in {meetings[k]}")
print("Matches:")
for idx, m in enumerate(match, 1):
    print(f"Match{idx}: {m}")


