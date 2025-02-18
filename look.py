#! Python 3

import sqlite3

connection = sqlite3.connect('dbase.db')
cursor = connection.cursor()

query = 'select class from npc where (class = "Barbarian") or (class = "Warrior") or (class = "Knight") or (class = "Samurai");'
cursor.execute(query)
result = cursor.fetchall()

Warriors = 0
total = len(result)
for i in result:
    print(i)
    if i[0] == "Warrior":
        Warriors += 1
precent = round((Warriors/total) * 100,2)
print(precent)

'''
query = 'select id,strength,intelligence,wisdom,dexterity,constitution,charisma from npc;'
cursor.execute(query)
result = cursor.fetchall()

high = [0,0]
for i in result:
    total = sum((i[1],i[2],i[3],i[4],i[5],i[6]))
    if total > high[1]:
        high[0] = i[0]
        high[1] = total 

print(high)
'''
'''
query = 'select strength,intelligence,wisdom,dexterity,constitution,charisma from npc where class = "Bard" order by strength desc limit 10;'
cursor.execute(query)
result = cursor.fetchall()
print(f"strength : {result[0][0]}, intelligence : {result[0][1]}, wisdom : {result[0][2]}, dexterity : {result[0][3]}, constitution : {result[0][4]}, charisma : {result[0][5]}")
'''
'''
query = 'select gold from npc where level < 5 order by gold desc limit 100;'
cursor.execute(query)
result = cursor.fetchall()
#print(result)

sum = 0
for i in result:
    sum += i[0]
    print(i[0],sum)
'''
'''
query = 'select id,gold,class from npc where class = "Jester" order by gold desc;'
cursor.execute(query)
result = cursor.fetchall()
#print(result)
print(result[0])
'''
'''
classes = {"Warrior":0,"Ranger":0,"Knight":0,"Sorcerer":0,"Sage":0,"Priest":0,"Thief":0,"Bard":0,"Barbarian":0,"Monk":0,"Assassin":0,"Jester":0,"Samurai":0}

for i in classes:
    query = f'select * from npc where class = "{i}";'
    cursor.execute(query)
    result = cursor.fetchall()
    classes[i] = len(result)

print(classes)
'''