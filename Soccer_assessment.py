
#Mariska Olwagen

reading=open("sample_input.txt", "r")

all_scores = reading.readlines()
team_names = []
score_sheet = dict()

for x in all_scores:

    match = x
       
    match_split = match.split(",")
       

    team_score_a = match_split[0]
    team_score_b = match_split[1]

    i = 0
    temp = []
    team_name_a = ''
    team_name_b = ''
    
    for i in team_score_a:
        if (not i.isdigit()):
            team_name_a = team_name_a+i
    for i in team_score_b:
        if (not i.isdigit()):
            team_name_b = team_name_b+i
    team_name_a = team_name_a.strip()
    team_name_b = team_name_b.strip()
    
    score_a = [int(s) for s in team_score_a.split() if s.isdigit()]
    score_b = [int(s) for s in team_score_b.split() if s.isdigit()]
    
    if (not team_name_a in team_names):
        team_names.append(team_name_a)
        score_sheet[team_name_a] = 0
    if (not team_name_b in team_names):
        team_names.append(team_name_b)
        score_sheet[team_name_b] = 0

    if (score_a > score_b):
        score_sheet[team_name_a] = score_sheet.setdefault(team_name_a, score_a) + 3
    if (score_b > score_a):
        score_sheet[team_name_b] = score_sheet.setdefault(team_name_b, score_b) + 3
    if (score_a == score_b):
        score_sheet[team_name_a] = score_sheet.setdefault(team_name_a, score_a) + 1
        score_sheet[team_name_b] = score_sheet.setdefault(team_name_b, score_b) + 1
i = 0
prev_score = -1

for key, value in sorted(score_sheet.iteritems(), key=lambda (k,v): (-v,k)):   
    if (not value == prev_score):
        i += 1
    if (value != 1):
        print "%d. %s, %s pts" % (i, key, value)
    if (value == 1):
        print "%d. %s, %s pt" % (i, key, value)
    prev_score = value

reading.close()