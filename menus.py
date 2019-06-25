def town_menu():
    title = "The Towne of Ang"
    option_listing = (
    "(I)nn, (S)hoppe, S(m)ithy, (T)emple or back to Staging?(Q)"
    )
    submenus = {
            'I': inn_menu, 'S': shoppe_menu, 'M': smithy_menu,
            'T': temple_menu
    }
    master_menu(title, option_listing, submenus)

#easy menus, always use (Q) for return option in option_listing
def master_menu(title, option_listing, submenus):
    print (title)
    quitting = False
    while quitting == False:
        print (option_listing)
        answer = input()
        answer = (answer.upper())[0]
        for option, callee in submenus.items():
            if answer == option:
                callee()
            if answer == 'Q':
                quitting = True
                break

def dungeon_menu():
    title = "The Ominious Dungeon"
    option_listing = (
            "(C)heck status, (V)enture forth, or back to Staging(Q)?"
    )
    submenus = {
            'C': status, 'V': dungeon
    }
    master_menu(title, option_listing, submenus)

def inn_menu():
    title = (
            """The Diligent Ass
            Homer: Welcome to my establishment! We have the finest ale!"""
    )
    option_listing = (
            "(R)est, R(u)mours, or back to Town(Q)?"
    )
    submenus = {
            'R':inn_rest, 'U': inn_rumours
    }
    master_menu(title, option_listing, submenus)

def smithy_menu():
    title = (
            """The Furious Blaze
            Wilhelm: Come, let me show you what wonders 
            the union of ore and flame can produce!"""
            )
    option_listing = (
            "(C)ommission, (R)umours, or back to Town(Q)?"
    )
    submenus = {
            'C': smithy_commission, 'R': smithy_rumours
    }
    master_menu(title, option_listing, submenus)

def shoppe_menu():
    title = (
            """ Gofer's Gaudy Goods and Godly Gums
            Gofer: Welcome!
            All antidotes for any altercation avaliable for all adventurers!"""
            )
    option_listing = (
            "(B)uy, (S)ell, (R)umours, or back to Town(Q)?"
    )
    submenus = {
            'B': shoppe_buy, 'S': shoppe_sell, 'R': shoppe_rumours
    }
    master_menu(title, option_listing, submenus)

def temple_menu():
    title = (
"""Home of the Divine, Shelter to the Disaffected, Refuge from Evil
Temple of Eternity
Luther: Peace everlasting, child. 
Come rest your weary soul from the conflict eternal, 
that your soul be emboldened and your salvation secured.
"""
    )
    option_listing = (
            "(P)ray, (T)ithe, (S)ermon, or back to Town(Q)?"
    )
    submenus = {
            'P': temple_pray, 'T': temple_tithe, 'S': temple_sermon
    }
    master_menu(title, option_listing, submenus)

def inn_rest():
    print ("You now feel very well rested!")
    #max out hp, mp, trigger level up if exp gains are good

def inn_rumours():
    print ("The innkeep lets you in on a juicy bit of gossip")
    #something different depending on the level of the player

def status():
    print ("The adventurer's status:")
    #print (name)
    #print (player_job, "Level", player_level)
    #print player_hp
    #print player_mp
    #print player_illnesses

def dungeon():
    print ("And so the daring adventurer delved deep into the darkness!")
    #lots of stuff here for sure!

def smithy_commission():
    print ("A true artisan never rests until potential has been exhausted!")
    # check player's job
    # show items that can be made
    # when player selects one, display required materials
    # if they do, ask before consuming them

def smithy_rumours():
    print ("The smithy lets you in on a juicy bit of gossip")
    # something different depending on the level of the player

def shoppe_buy():
    print ("Ah, finally, a customer!")
    # check player level
    # display items suitable for that level
    # buy function is exclusive here, commission consumes items

def shoppe_sell():
    print ("Ah, finally, a restock!")
    # display prices for player's inventory
    # sell function exclusive here

def shoppe_rumours():
    print ("The shopkeep lets you in on a juicy bit of gossip")
    # something different dpeneding on the level of the player

def temple_pray():
    print (
            """"The favor of the gods are upon you. 
            Righteousness fills your soul."""
    )
    #check tithe level
    #multiple prayer buff by tithe level, store result as temp stat
    #print some different, additional text depending on tithe level

def temple_tithe():
    # ask for value of tithe (check range on this)
    # check player's gold
    # remove player's gold if avaliable
    # add to tithe total by the amount removed
    # if amount > 0
    print ("The priest nods towards you, grateful for your generosity")

def temple_sermon():
    # check player's level, deliver different sermon at each one
    print ("Oh faithful, blah blah blah")


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
