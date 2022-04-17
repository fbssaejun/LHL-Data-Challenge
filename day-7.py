'''
Challenge
To help Dot learn more about FC Barcelona’s statistics, we have the historical La Liga results of the 1988/1989 season.

Dot needs you to figure out the answers to the following questions:

1. What is the maximum amount of games Barcelona playes in 1 season?
2. What is the average attendance across the seasons?
3. What is the difference between median value of wins and losses?
4. What is the minimum number of games Barcelona managed to win in 1 season?
5. What is the difference between max and min amount of points Barcelona was able to get in all seasons?

'''
import pandas as pd
df = pd.read_csv('fc_barcelona.csv')
df.head()

'''

Season	Squad	Country	Comp	LgRank	MP	W	D	L	GF	GA	GD	Pts	Attendance	Top Team Scorer	Goalkeeper	Notes
0	2020-2021	Barcelona	es ESP	1. La Liga	3rd	38	24	7	7	85	38	47	79	NaN	Lionel Messi - 30	Marc-André ter Stegen	→ UEFA Champions League via league finish
1	2019-2020	Barcelona	es ESP	1. La Liga	2nd	38	25	7	6	86	38	48	82	54223.0	Lionel Messi - 25	Marc-André ter Stegen	→ UEFA Champions League via league finish
2	2018-2019	Barcelona	es ESP	1. La Liga	1st	38	26	9	3	90	36	54	87	76104.0	Lionel Messi - 36	Marc-André ter Stegen	→ UEFA Champions League via league finish
3	2017-2018	Barcelona	es ESP	1. La Liga	1st	38	28	9	1	99	29	70	93	67142.0	Lionel Messi - 34	Marc-André ter Stegen	→ UEFA Champions League via league finish
4	2016-2017	Barcelona	es ESP	1. La Liga	2nd	38	28	6	4	116	37	79	90	78678.0	Lionel Messi - 37	Marc-André ter Stegen	→ UEFA Champions League via league finish

'''

points = df.Pts
games_played = df.MP
wins = df.W
losses = df.L
attendance = df.Attendance.dropna()

# 1
print(games_played.max()) # => 42
# 2
print(attendance.mean()) # => 72579.85714285714
# 3
print(wins.median() - losses.median()) # => 19.0
# 4
print(wins.min()) # => 15
# 5
print(points.max() - points.min()) # => 54
