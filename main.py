import jobs
import menus
import sys

print ("Welcome to the world!")
print ("Enter your name")
name = input()
print ("Welcome:", name)
selection = False
while selection == False:
    print ("Select a job")
    print (jobs.joblist)
    player_job = input()
    player_job = player_job.upper()
    for job in jobs.joblist:
        if player_job[0]== job[0].upper():
            player_job = job
            selection = True
        if player_job == job.upper():
            selection = True
    if selection == False:
        print ("Invalid input.")

#making an appropriate Object of the Job class
#open jobs.dat
#find the necessary Job that is ==player_job
#pjob = job(player_job)

print ("Behold! A new era is dawning on the continent!")
print ("The fresh hero", name + ", a mighty", player_job, "in the making")
print ("is beginning their adventure! What wonderous deeds they shall lay")
print ("a claim to, what legends their tale will give life!")

print ("View skills? (Y/N)")
answer=input()
#if answer.upper() == "Y":
    #for skill in pjob.skills:
    #   print (skill.description)
if answer.upper() == "N":
    print ("Okay!")
print ("Press enter to continue")
answer = input()
print ("And so the hero looks like this:")
print (name, player_job, "Lvl 1")
print ("May", name + "'s adventure by filled with glory and riches!")

# pull up world map (town or dungeon)
selection = False
while (selection == False):
    print ("Proceed to (T)own or the (D)ungeon? Or (Q)uit?")
    answer = input()
    answer = answer.upper()
    if (answer[0] == 'T'):
        menus.town_menu()
    if (answer[0] == 'D'):
        menus.dungeon_menu()
    if (answer[0] == 'Q'):
        print ("And so the adventurer took a rest.")
        sys.exit()
# town menu -> Inn, Smithy, Shop, Temple
# Inn -> Rest, talk
# Smithy -> Commission, Talk
# Shop -> Buy, Sell, Talk
# Temple -> Pray, Tithe

# dungeon menu -> Venture forth

# Inn - Rest: Recover HP and MP, cure ailments
# Inn - Talk: Hear proprietor's rumors

# Smithy - Commission: Have smith work with materials found in dungeon
# Smithy - Talk: Hear smith's rumors

# Shop - Buy/Sell: Self-explanatory
# Shop - Talk: Hear shopkeep's rumors

# Temple - Pray: Receive buff against evil magic for next venture
# Temple - Tithe: Increases strength of prayer buff

# Dungeon - the dungeon 
