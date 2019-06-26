def battle(player, enemy_party):
    alive = True
    while alive == True:
        # present information to player
        print ("")
        for enemy in enemy_party:
            print (enemy.name)
        title = player.name + " " + player.current_hp + "/" + player.max_hp
        option_listing = (
        "(A)ttack, (S)kill, or (F)lee?"
        )
        submenus = {
        'A':attack_menu , 'S':skill_menu , 'F':flee
        }


        # ask for player input
        # iterate through enemies, determine their action
        #   attack, run away, cast magic spell
        # execute actions based on initiative
        # check if any enemies died, add exp to player if they did
        # check if player died
    if player.status == "Dead":
        print("")
        input()
        sys.exit()
        # check if all enemies died, if they did, alive = False
    return player

def enemy_gen(location, number):
    enemy_party = {} # enemy name is the key, value is the number of that type
    # open enemy file
    # randomly pick that many enemies from the file that match location info
    return enemy_party

def attack_menu():
    print ("A vicious blow to the enemy!")
def skill_menu():
    print ("A blistering skill crushes the enemy!")
    num = 1
    for skill in player.skills:
        print (num, skill.name)
        num++
    print ("Or (E)xit to previous menu.")
    answer = input()
    answer = answer.upper()[0]
    if answer == 'E':
        return

def flee():
    print ("Discretion is the better part of valor...")
    roll = False
    #roll to escape
    print (result)
    if roll == True:
        alive = False
        print ("A successful retreat!")
        print ("Press enter to continue")
        input()
    elif roll == False:
        print ("Few circumstances are more dire than a failed escape...")
        print ("Press enter to continute")
        input()
