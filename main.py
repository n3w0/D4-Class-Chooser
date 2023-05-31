import sys
import re
import webbrowser 

###I found all these builds from Wudijo's Discord, used bard to help with my wording, and found the ascii art off the internet###
###I made this for the release of diablo 4 for fun to help my lan party decide what classes to build. It will probably break. 

# Title
print ("Welcome to Diablo IV Class Chooser")
# ASCII Art
print ("""              ⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣤⣤⠄⢀⣤⠀⣾⣿⣿⣿⠀⣀⠀⢠⣤⣤⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣶⣿⣿⣿⠃⣰⣿⣿⣄⠙⠿⠿⠋⣠⣿⣷⡄⠹⣿⣿⣿⣶⡀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⠇⢰⣿⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⡀⢹⣿⣿⣿⣿⣄⠀⠀
⠀⢸⣿⣿⡿⠋⠀⠀⣿⡏⠀⠙⠻⣿⣿⣿⣿⠟⠁⠀⣿⣧⠀⠀⠙⢿⣿⣿⡆⠀
⠀⣿⣿⡿⠀⠀⠀⢰⣿⣿⣤⣤⣴⣿⣿⣿⣿⣦⣤⣴⣿⣿⠀⠀⠀⠈⣿⣿⡇⠀
⠀⢹⣿⣇⠀⠀⠀⢸⣿⣿⣿⣿⣷⡙⠻⠟⢩⣿⣿⣿⣿⣿⠀⠀⠀⠀⣼⣿⡇⠀
⠀⠈⠻⣿⣆⠀⠀⠈⠉⠉⠉⣿⣿⣷⡀⢠⣿⣿⡏⠉⠉⠉⠀⠀⠀⣰⣿⠟⠀⠀
⠀⠀⠀⠈⠉⠓⠂⠀⠀⠀⠀⣿⣿⣿⣷⣿⣿⣿⡇⠀⠀⠀⠀⠐⠛⠉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢿⡟⠈⣿⡿⠈⢿⡇⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡆⠘⢀⡆⠸⠃⣠⠈⠃⢸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡇⠀⣾⣷⠀⢀⣿⣧⠀⣼⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⠇⠸⣿⣿⠀⠸⣿⣿⠆⢻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀""")
# Background
print ("""The world of Sanctuary is in chaos. The forces of the Burning Hells have invaded, and only the Nephalem stand in their way. As a Nephalem, you must rise up and face the armies of Hell.
You will travel across Sanctuary, exploring its many lands and battling its many enemies. You will face fearsome demons, powerful bosses, and even other Nephalem who have been corrupted by the forces of evil.
But you will not be alone. You will have the help of your allies, and you will also have the power of the Nephalem. With your strength and courage, you can defeat the forces of Hell and save Sanctuary.
""")

# Class Dictionaries
Barbarian = {"Rend Build":"https://d4builds.gg/builds/1a3bca3b-d9ac-4fb8-a71c-2cfbb15351e1/", "Upheaval Build":"https://d4builds.gg/builds/eaf9e06b-955e-4579-a048-874b6107eeef/", "Whirlwind Build":"https://d4builds.gg/builds/1890b5e7-5763-46f9-a529-826a5f6f9ea6/", "Double Swing Build":"https://d4builds.gg/builds/d22b0233-7b6d-4ec6-8792-7478184bd41d/"}
Rogue = {'Penetrating Shot Build':'https://d4builds.gg/builds/0d0b0f22-7e7c-4ecd-bde2-6c82ab45729f/', 'Twisting Blades Build':'https://d4builds.gg/builds/541c5610-a763-41f1-967a-9704decf0e2a/', 'Flurry Build':'https://d4builds.gg/builds/20de0cce-3d25-45b4-a1aa-4cfeb3895348/', 'Rapid Fire Build': 'https://d4builds.gg/builds/f8ca3f29-8a89-4955-b41f-1b5e6438e173/'}
Necromancer = {'Bone Spear Build':'https://d4builds.gg/builds/34b2b997-50f8-4a50-99ea-129767063a56/', 'Sever Build':'https://d4builds.gg/builds/fe27088c-bd82-4eb0-a8e1-61616bebbb22/', 'Blood Lance Build':'https://d4builds.gg/builds/c32c449a-f328-4d46-9056-9b5a54943841/', 'Blight Build':'https://d4builds.gg/builds/6d23b15c-35cf-4644-87d7-324cb3baeaa4/'}
Sorceress = {'Arc Lash Build':'https://d4builds.gg/builds/4334762d-269a-4ed0-852f-3508178e7aa8/', 'Ice Shards Build':'https://d4builds.gg/builds/2aa4d8d1-641b-4a2c-9d12-e65f7f8b692d/', 'Firewall Build':'https://d4builds.gg/builds/1f1d3b8a-0efe-4b33-b9a5-df20499b1d8a/', 'Meteor Build':'https://d4builds.gg/builds/5bf25084-796b-415e-90b2-2f7d0e84f472/'}
Druid = {'Tornado Build':'https://d4builds.gg/builds/c555f989-c669-4347-8e04-5a62c1c018e4/', 'Lightning Storm Build':'https://d4builds.gg/builds/5e6244e4-83db-4926-a964-519ee8505975/', 'Shred Build':'https://d4builds.gg/builds/4534cd6d-aad5-4124-9bce-acf1e018b65c/', 'Pulverize Build':'https://d4builds.gg/builds/d4cc83e8-be91-4dcd-931c-8769c3bddedd/' }

Classes = { "Barbarian" : Barbarian, "Rogue": Rogue, "Necromancer": Necromancer, "Sorceress":Sorceress, "Druid": Druid }

# How many players are in the party and a list of players so I can pull the index easily.
numbers = { "one": 1, "two":2, "three":3, "four":4, "uno":1, "dos":2, "tres":3, "cuatro":4}
roman = {"I":1, "II":2, "III":3, "IV":4, "IIII":4, "i":1, "ii":2, "iii":3, "iiii":4, "iv":4}

#Statement to force users input into a list of 1-4
while True:
    player_amount = input("How many players are currently in your party?\nYour Answer: ").strip()
    
    if player_amount in numbers:
        player_amount = numbers[player_amount]
        break
    
    elif player_amount in roman: 
        player_amount = roman[player_amount]
        break

    elif player_amount.isdigit() and int(player_amount) < 5 and int(player_amount) > 0:
        player_amount = int(player_amount)
        break
    elif not (player_amount in numbers or player_amount.isdigit() and int(player_amount) < 5 and int(player_amount) > 0):
        print ("\nPlease enter 1-4 in anyway you can think of please.\n")

player_amount_list = []
for i in range(player_amount):
    player_amount_list.append(i+1)


# Main Loop
while player_amount > 0: 
    if ("Rogue" in Classes or "Barbarian" in Classes) and ("Necromancer" in Classes or "Druid" in Classes or "Sorceress" in Classes):
        answer_1 = input ("\nPlayer " + str(player_amount_list[0]) + ", Will you stride into the heart of battle, feeling the clash of steel in close quarters, or are you drawn to the boundless arcane powers that shape the elements and manipulate life and death?\nYour Answer: ")
    
    
    #Melee 
        if "Barbarian" in Classes and "Rogue" in Classes and re.findall("clash|steel|close|quarters", answer_1.lower()):
            weapons_1 = input("Will you stand your ground or strike from the shadows?\nYour Answer: ")

         
        #Barbarian
            if "Barbarian" in Classes and re.findall("stand|your|ground", weapons_1.lower()):
             
             #Barbarian Final Question
                barb_build = input("\nWill you morph into a walking apocalypse and inflict mortal wounds on your enemies, shatter your enemies with the power of earth, become a cyclone of death, or behold the power of the twin blades?\nYour Answer: ")
                
                #Rend 
                if re.findall("walking|apocalypse|inflict|mortal|wounds", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe rend build uses the rend skill to inflict a bleed effect on enemies, which deals damage over time")
                    print ("Wanna learn how to tear through demons like a hot knife through butter?\nHere's a site to learn more about the rend build!\n") 
                    webbrowser.open(Classes["Barbarian"]["Rend Build"])
                    
                #Upheaval
                elif re.findall("shatter|enemies|power|earth", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Upheaval build is a powerful and versatile build that can be used to crush your enemies.\n")
                    print ("This build relies on the Upheaval skill, which allows you to slam the ground and create a shockwave that deals damage to enemies in an area.\nHere's a site to learn more and start sending demons flying!\n") 
                    webbrowser.open(Classes["Barbarian"]["Upheaval Build"])

                #Whirlwind
                elif re.findall("cyclone|death", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Whirlwind build is a devastating and unstoppable build that can be used to tear through your enemies.")
                    print ("If you're looking for a build that can deal massive damage and clear hordes of enemies quickly, then the Whirlwind build is the perfect choice for you. \nHere's a site to learn more and start spinning your way to victory!\n") 
                    webbrowser.open(Classes["Barbarian"]["Whirlwind Build"])
                
            #Double Swing
                elif re.findall("behold|power|twin|blades", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Double Swing build is a powerful and efficient build that can be used to deal massive damage.")
                    print ("This build relies on the Double Swing skill, which allows you to attack twice in rapid succession.\nHere's a site to learn more and start cleaving demons in half!\n") 
                    webbrowser.open(Classes["Barbarian"]["Double Swing Build"])

                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Barbarian')
        
        
        #Rogue 
            elif "Rogue" in Classes and re.findall("strike|shadows", weapons_1.lower()):
            
            #Final Rogue Question
                rogue_build = input("\nWould you rather pierce through enemies with your arrows, unleash a flurry of deadly blades, attack with incredible speed unleashing a barrage of blows, or shred through your foes with pinpoint accuracy?\nYour Answer: ")

            #Penetrating Shot
                if re.findall("piercing|enemies|pierce|through|arrows", rogue_build.lower()):
                    print ("""\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nYou've chosen a powerful and versatile class that is sure to bring you hours of fun.\nThe Penetrating Shot build is an awesome build for the Rogue class.\nIt allows you to deal massive damage from a distance, and it's perfect for those who want to play a Spellcasters character.\nWith this build, you'll be able to pierce through enemies with your arrows, dealing devastating damage.\nJust be sure to stay out of reach, or you'll be in for a world of hurt.""")
                    print ("\nBecome a master of the bow with the Penetrating Shot build! Here's a site to learn more.\n") 
                    webbrowser.open(Classes["Rogue"]["Penetrating Shot Build"])
                
            #Flurry 
                elif re.findall("flurry|deadly|blades", rogue_build.lower()):
                    print("\nCongratulations, brave adventurer, on embracing the path of the Rogue! \nThe Rogue is a fast and agile class that specializes in dealing damage from a distance.\nThe Flurry build is a powerful build that allows you to quickly and easily dispatch your enemies.")
                    print("\nWith the Flurry build, you will become a whirlwind of death, leaving nothing but carnage in your wake.\nSo what are you waiting for? Here's a site to start your journey to mastery!\n")
                    webbrowser.open(Classes["Rogue"]["Flurry Build"])
                
            #Twisting Blades
                elif re.findall("attack|incredible|speed|barrage|blows|reeling", rogue_build.lower()):
                    print ("\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nThe rogue is a fast and agile class that specializes in dealing damage from a distance.\nThe Twisting Blades build is a powerful build that allows you to quickly and easily dispatch your enemies.")
                    print ("\nWith the Twisting Blades build, you will become a deadly whirlwind, leaving nothing but destruction in your wake.\nSo what are you waiting for? Here's a site to learn more!\n")
                    webbrowser.open(Classes["Rogue"]["Twisting Blades Build"])

            #Rapid Fire
                elif re.findall("shred|foes|pinpoint|accuracy", rogue_build.lower()):
                    print ("\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nWithin the chaos of battle, Rapid Fire will become your symphony of destruction.\nThis technique allows you to unleash a torrent of arrows upon your foes, striking them down with relentless precision.\nWith each arrow unleashed, your enemies will tremble in fear as they succumb to the might of your unyielding barrage.")
                    print ("\nTo further refine your understanding of this devastating build, I invite you to embark on a journey of knowledge.\nHere's a site to helpembrace the secrets of Rapid Fire.\nUncover the arcane techniques, the synergistic equipment, and the strategic prowess that will allow you to unleash the true potential of this lethal art.\n") 
                    webbrowser.open(Classes["Rogue"]["Rapid Fire Build"])

            player_amount = player_amount - 1
            player_amount_list.remove(player_amount_list[0])
            Classes.pop('Rogue')
    
    #ONLY BARB
        elif "Rogue" not in Classes and re.findall("clash|steel|close|quarters", answer_1.lower()):
            weapons_1 = ("stand your ground")
        #Barbarian
            if "Barbarian" in Classes and re.findall("stand|your|ground", weapons_1.lower()):
             
             #Barbarian Final Question
                barb_build = input("\nWill you morph into a walking apocalypse and inflict mortal wounds on your enemies, shatter your enemies with the power of earth, become a cyclone of death, or behold the power of the twin blades?\nYour Answer: ")
                
                #Rend 
                if re.findall("walking|apocalypse|inflict|mortal|wounds", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe rend build uses the rend skill to inflict a bleed effect on enemies, which deals damage over time")
                    print ("Wanna learn how to tear through demons like a hot knife through butter?\nHere's a site to learn more about the rend build!\n")
                    webbrowser.open(Classes["Barbarian"]["Rend Build"])
                    
                #Upheaval
                elif re.findall("shatter|enemies|power|earth", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Upheaval build is a powerful and versatile build that can be used to crush your enemies.\n")
                    print ("This build relies on the Upheaval skill, which allows you to slam the ground and create a shockwave that deals damage to enemies in an area.\nHere's a site to learn more and start sending demons flying!\n")
                    webbrowser.open(Classes["Barbarian"]["Upheaval Build"])

                #Whirlwind
                elif re.findall("cyclone|death", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Whirlwind build is a devastating and unstoppable build that can be used to tear through your enemies.")
                    print ("If you're looking for a build that can deal massive damage and clear hordes of enemies quickly, then the Whirlwind build is the perfect choice for you. \nHere's a site to learn more and start spinning your way to victory!\n")
                    webbrowser.open(Classes["Barbarian"]["Whirlwind Build"])
                
            #Double Swing
                elif re.findall("behold|power|twin|blades", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Double Swing build is a powerful and efficient build that can be used to deal massive damage.")
                    print ("This build relies on the Double Swing skill, which allows you to attack twice in rapid succession.\nHere's a site to learn more and start cleaving demons in half!\n")
                    webbrowser.open(Classes["Barbarian"]["Double Swing Build"])

                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Barbarian')
        
    #ONLY ROGUE
        elif "Barbarian" not in Classes and re.findall("clash|steel|close|quarters", answer_1.lower()):
            weapons_1 = ("strike from the shadows")
        #Rogue 
            if "Rogue" in Classes and re.findall("strike|shadows", weapons_1.lower()):
            
            #Final Rogue Question
                rogue_build = input("\nWould you rather pierce through enemies with your arrows, unleash a flurry of deadly blades, attack with incredible speed unleashing a barrage of blows, or shred through your foes with pinpoint accuracy?\nYour Answer: ")

            #Penetrating Shot
                if re.findall("piercing|enemies|pierce|through|arrows", rogue_build.lower()):
                    print ("""\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nYou've chosen a powerful and versatile class that is sure to bring you hours of fun.\nThe Penetrating Shot build is an awesome build for the Rogue class.\nIt allows you to deal massive damage from a distance, and it's perfect for those who want to play a Spellcasters character.\nWith this build, you'll be able to pierce through enemies with your arrows, dealing devastating damage.\nJust be sure to stay out of reach, or you'll be in for a world of hurt.""")
                    print ("\nBecome a master of the bow with the Penetrating Shot build! Here's a site to learn more.\n")
                    webbrowser.open(Classes["Rogue"]["Penetrating Shot Build"])
                
            #Flurry 
                elif re.findall("flurry|deadly|blades", rogue_build.lower()):
                    print("\nCongratulations, brave adventurer, on embracing the path of the Rogue! \nThe Rogue is a fast and agile class that specializes in dealing damage from a distance.\nThe Flurry build is a powerful build that allows you to quickly and easily dispatch your enemies.")
                    print("\nWith the Flurry build, you will become a whirlwind of death, leaving nothing but carnage in your wake.\nSo what are you waiting for? Here's a site to help start your journey to mastery!\n")
                    webbrowser.open(Classes["Rogue"]["Flurry Build"])
                
            #Twisting Blades
                elif re.findall("attack|incredible|speed|barrage|blows|reeling", rogue_build.lower()):
                    print ("\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nThe rogue is a fast and agile class that specializes in dealing damage from a distance.\nThe Twisting Blades build is a powerful build that allows you to quickly and easily dispatch your enemies.")
                    print ("\nWith the Twisting Blades build, you will become a deadly whirlwind, leaving nothing but destruction in your wake.\nSo what are you waiting for? Here's a site to learn more!\n")
                    webbrowser.open(Classes["Rogue"]["Twisting Blades Build"])

            #Rapid Fire
                elif re.findall("shred|foes|pinpoint|accuracy", rogue_build.lower()):
                    print ("\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nWithin the chaos of battle, Rapid Fire will become your symphony of destruction.\nThis technique allows you to unleash a torrent of arrows upon your foes, striking them down with relentless precision.\nWith each arrow unleashed, your enemies will tremble in fear as they succumb to the might of your unyielding barrage.")
                    print ("\nTo further refine your understanding of this devastating build, I invite you to embark on a journey of knowledge.\nHere's a site, brave Rogue, and embrace the secrets of Rapid Fire.\nUncover the arcane techniques, the synergistic equipment, and the strategic prowess that will allow you to unleash the true potential of this lethal art.\n")
                    webbrowser.open(Classes["Rogue"]["Rapid Fire Build"])

                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Rogue')
    
    
    #Spellcasters
        elif "Sorceress" in Classes and "Necromancer" in Classes and "Druid" in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = input("\nWill you embrace the primal harmony of nature, unleash the arcane forces of magic, or delve into the forbidden arts of life and death to shape your path?\nYour Answer: ")
        
        
        #Necromancer
            if "Necromancer" in Classes and re.findall("life|death|shape|path", elements_1):
                necro_build = input("Which sinister manifestation shall you command, wielding the deadly piercing essence of bone, inflicting ruthless severance upon your enemies, harnessing the unholy power of blood to lance through their defenses, or casting a vile blight that corrodes all life in its path?\nYour Answer: ")
            
        #Bone Spear
                if re.findall("wielding|deadly|piercing|essence|bone", necro_build.lower()):
                    print ("\nCongratulations, revered master of the dark arts, for embracing the necromantic path within the realms of Sanctuary!\nYour choice to harness the arcane powers of bone and wield the deadly precision of the Bone Spear build is a testament to your command over life and death.")
                    print ("May your path be adorned with the echoes of fallen foes, and may the spoils of victory be yours to claim.\nHere's a site to unveil the dread power of the Bone Spear build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Bone Spear Build"])

        #Sever
                elif re.findall("inflicting|ruthless|severance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for venturing into the shadows of Sanctuary as a devoted practitioner of the dark arts!\nYou have tapped into the boundless power of life and death.\nEmbrace your destiny and wield the devastating Sever build with unforgiving precision.")
                    print ("May your path be shrouded in the echoes of vanquished souls, and may the spoils of your triumphs be abundant.\nHere's a site to unleash the relentless power of the Sever build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Sever Build"])
        
        #Blood Lance
                elif re.findall("harnessing|unholy|power|blood|lance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the forbidden powers that flow through your veins!\nYour choice to wield the dark and insidious might of the Blood Lance build is a testament to your command over the very essence of life itself.")
                    print ("May your path be drenched in the crimson hues of sacrifice, and may the spoils of your conquests flow abundantly.\nHere's a site to unleash the unholy power of the Blood Lance build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blood Lance Build"])
        #Blight
                elif re.findall("casting|vile|blight|corrodes|life", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the darkness that shrouds the realm of Sanctuary!\nYou have delved into the forbidden depths of life and death, and now, you wield the malignant power of the Blight build, casting an unrelenting plague upon your enemies.")
                    print ("May your path be cloaked in the suffocating embrace of blight, and may the spoils of your conquests reek of decay.\nHere's a site to unleash the unrelenting power of the Blight build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blight Build"])
            
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Necromancer')


        #Sorceress
            elif "Sorceress" in Classes and re.findall("arcane|forces|magic", elements_1):
                sorc_build = input("\nWhose power shall you embrace, wielding the chilling forces of icy devastation, conjuring infernal flames to engulf your enemies, channeling the crackling energy of lightning's wrath, or harnessing the cataclysmic might of celestial fire from the heavens above?\nYour Answer: ")
            
            #Ice Shards
                if re.findall("chilling|forces|icy|devastation", sorc_build.lower()):

                    print("\nCongratulations, formidable sorceress, on your unwavering dedication to the path of magic!\nYour choice to wield the chilling might of Ice Shards speaks volumes of your profound mastery over the elements.")
                    print("May your path be adorned with frozen grandeur, and may your enemies quiver in the face of your unyielding power.\nHere's a site to explore the chilling art of Ice Shards and claim your rightful place among the most esteemed sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Ice Shards Build"])
                
            #Firewall
                elif re.findall("conjuring|infernal|flames|engulf", sorc_build.lower()):

                    print ("\nCongratulations, mighty sorceress, on your unwavering dedication to the mystical arts!\nYour choice to embrace the scorching power of the Firewall build is a testament to your fiery spirit and insatiable hunger for destruction.")
                    print ("May your path be forged in the crucible of flames, and may your enemies tremble in the face of your unrelenting power.\nHere's a site to immerse yourself in the scorching art of the Firewall build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Firewall Build"])
                
            #Arc Lash
                elif re.findall("crackling|energy|wrath|lightning", sorc_build.lower()): 
                
                    print ("\nCongratulations, esteemed sorceress, on your unwavering dedication to the arcane arts!\nYour choice to embrace the electrifying power of the Arc Lash build is a testament to your mastery over the forces of lightning and your thirst for unparalleled devastation.")
                    print ("May your path be illuminated by the electrifying brilliance of Arc Lash, and may your enemies tremble in the face of your overwhelming might.\nHere's a site to immerse yourself in the electrifying art of the Arc Lash build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Arc Lash Build"])
                
            #Meteor
                elif re.findall("harnessing|cataclysmic|might|celestial|fire|heavens", sorc_build.lower()): 
                
                    print ("\nCongratulations, illustrious sorceress, on your unwavering devotion to the arcane arts!\nYour choice to harness the cataclysmic might of the Meteor build is a testament to your command over celestial forces and your insatiable thirst for destruction.")
                    print ("May your path be illuminated by the celestial brilliance of Meteor, and may your enemies quiver in the face of your unrelenting power.\nHere's a site to delve into the cataclysmic art of the Meteor build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Meteor Build"])
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Sorceress')
            
            
        #Druid
            elif "Druid" in Classes and re.findall("primal|harmony|nature", elements_1):
                druid_build = input("\nWhich path shall you embrace, summoning the chaotic might of swirling tempests, unleashing the untamed ferocity of nature's wrath, channeling the unyielding strength of the earth's core, or commanding the electrifying fury of celestial storms?\nYour Answer: ")
            
            #Tornado
                if re.findall("summoning|chaotic|might|swirling|tempests", druid_build.lower()):
                    print ("\nCongratulations, mighty druid, on your primal connection to nature!\nYour choice to embody the relentless force of the Tornado build is a testament to your mastery over the elements and your unwavering spirit.")
                    print ("May your path be woven in harmony with the winds, and may your enemies tremble in the face of your indomitable power.\nHere's a site to delve into the tempestuous art of the Tornado build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Tornado Build"])
                
            #Shred
                if re.findall("unleashing|untamed|ferocity|wrath", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the savage might of the Shred build is a testament to your primal ferocity and unwavering resolve.")
                    print ("May your path be entwined with the raw fury of nature, and may your enemies tremble in the face of your untamed power.\nHere's a site to delve into the savage art of the Shred build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Shred Build"])

            #Pulverize
                if re.findall("channeling|unyielding|strength|core", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the unyielding might of the Pulverize build is a testament to your indomitable strength and unwavering determination.")
                    print ("May your path be paved with the unyielding strength of the mountains, and may your enemies tremble in the face of your unstoppable force.\nHere's a site to delve into the earth-shaking art of the Pulverize build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Pulverize Build"])
                
            #Lightning Storm
                if re.findall("commanding|electrifying|fury|celestial|storms", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to harness the electrifying might of the Lightning Storm build is a testament to your mastery over the storms and your unwavering connection to the very essence of lightning.")
                    print ("May your path be illuminated by the crackling brilliance of Lightning Storm, and may your enemies tremble in the face of your electrifying power.\nHere's a site to delve into the electrifying art of the Lightning Storm build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Lightning Storm Build"])
                
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Druid')




        #ONLY DRUIDS
        elif "Sorceress" not in Classes and "Necromancer" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = "Will you embrace the primal harmony of nature"
        #Druid
            if "Druid" in Classes and re.findall("primal|harmony|nature", elements_1):
                druid_build = input("Which path shall you embrace, summoning the chaotic might of swirling tempests, unleashing the untamed ferocity of nature's wrath, channeling the unyielding strength of the earth's core, or commanding the electrifying fury of celestial storms?\nYour Answer: ")
            
            #Tornado
                if re.findall("summoning|chaotic|might|swirling|tempests", druid_build.lower()):
                    print ("\nCongratulations, mighty druid, on your primal connection to nature!\nYour choice to embody the relentless force of the Tornado build is a testament to your mastery over the elements and your unwavering spirit.")
                    print ("May your path be woven in harmony with the winds, and may your enemies tremble in the face of your indomitable power.\nHere's a site to delve into the tempestuous art of the Tornado build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Tornado Build"])
                
            #Shred
                if re.findall("unleashing|untamed|ferocity|wrath", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the savage might of the Shred build is a testament to your primal ferocity and unwavering resolve.")
                    print ("May your path be entwined with the raw fury of nature, and may your enemies tremble in the face of your untamed power.\nHere's a site to delve into the savage art of the Shred build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Shred Build"])

            #Pulverize
                if re.findall("channeling|unyielding|strength|core", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the unyielding might of the Pulverize build is a testament to your indomitable strength and unwavering determination.")
                    print ("May your path be paved with the unyielding strength of the mountains, and may your enemies tremble in the face of your unstoppable force.\nHere's a site to delve into the earth-shaking art of the Pulverize build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Pulverize Build"])
                
            #Lightning Storm
                if re.findall("commanding|electrifying|fury|celestial|storms", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to harness the electrifying might of the Lightning Storm build is a testament to your mastery over the storms and your unwavering connection to the very essence of lightning.")
                    print ("May your path be illuminated by the crackling brilliance of Lightning Storm, and may your enemies tremble in the face of your electrifying power.\nHere's a site to delve into the electrifying art of the Lightning Storm build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Lightning Storm Build"])
                
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Druid')

        #ONLY NECROS
        elif "Sorceress" not in Classes and "Druid" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = "delve into the forbidden arts of life and death to shape your path?"
        
        #Necromancer
            if "Necromancer" in Classes and re.findall("life|death|shape|path", elements_1):
                necro_build = input("\nWhich sinister manifestation shall you command, wielding the deadly piercing essence of bone, inflicting ruthless severance upon your enemies, harnessing the unholy power of blood to lance through their defenses, or casting a vile blight that corrodes all life in its path?\nYour Answer: ")
            
        #Bone Spear
                if re.findall("wielding|deadly|piercing|essence|bone", necro_build.lower()):
                    print ("\nCongratulations, revered master of the dark arts, for embracing the necromantic path within the realms of Sanctuary!\nYour choice to harness the arcane powers of bone and wield the deadly precision of the Bone Spear build is a testament to your command over life and death.")
                    print ("May your path be adorned with the echoes of fallen foes, and may the spoils of victory be yours to claim.\nHere's a site to unveil the dread power of the Bone Spear build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Bone Spear Build"])

        #Sever
                elif re.findall("inflicting|ruthless|severance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for venturing into the shadows of Sanctuary as a devoted practitioner of the dark arts!\nYou have tapped into the boundless power of life and death.\nEmbrace your destiny and wield the devastating Sever build with unforgiving precision.")
                    print ("May your path be shrouded in the echoes of vanquished souls, and may the spoils of your triumphs be abundant.\nHere's a site to unleash the relentless power of the Sever build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Sever Build"])
        
        #Blood Lance
                elif re.findall("harnessing|unholy|power|blood|lance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the forbidden powers that flow through your veins!\nYour choice to wield the dark and insidious might of the Blood Lance build is a testament to your command over the very essence of life itself.")
                    print ("May your path be drenched in the crimson hues of sacrifice, and may the spoils of your conquests flow abundantly.\nHere's a site to unleash the unholy power of the Blood Lance build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blood Lance Build"])
        #Blight
                elif re.findall("casting|vile|blight|corrodes|life", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the darkness that shrouds the realm of Sanctuary!\nYou have delved into the forbidden depths of life and death, and now, you wield the malignant power of the Blight build, casting an unrelenting plague upon your enemies.")
                    print ("May your path be cloaked in the suffocating embrace of blight, and may the spoils of your conquests reek of decay.\nHere's a site to unleash the unrelenting power of the Blight build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blight Build"])
            
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Necromancer')

        #ONLY SORCS
        elif "Necromancer" not in Classes and "Druid" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = "unleash the arcane forces of magic"
        #Sorceress
            if "Sorceress" in Classes and re.findall("arcane|forces|magic", elements_1):
                sorc_build = input("\nWhose power shall you embrace, wielding the chilling forces of icy devastation, conjuring infernal flames to engulf your enemies, channeling the crackling energy of lightning's wrath, or harnessing the cataclysmic might of celestial fire from the heavens above?\nYour Answer: ")
            
            #Ice Shards
                if re.findall("chilling|forces|icy|devastation", sorc_build.lower()):

                    print("\nCongratulations, formidable sorceress, on your unwavering dedication to the path of magic!\nYour choice to wield the chilling might of Ice Shards speaks volumes of your profound mastery over the elements.")
                    print("May your path be adorned with frozen grandeur, and may your enemies quiver in the face of your unyielding power.\nHere's a site to explore the chilling art of Ice Shards and claim your rightful place among the most esteemed sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Ice Shards Build"])
                
            #Firewall
                elif re.findall("conjuring|infernal|flames|engulf", sorc_build.lower()):

                    print ("\nCongratulations, mighty sorceress, on your unwavering dedication to the mystical arts!\nYour choice to embrace the scorching power of the Firewall build is a testament to your fiery spirit and insatiable hunger for destruction.")
                    print ("May your path be forged in the crucible of flames, and may your enemies tremble in the face of your unrelenting power.\nHere's a site to immerse yourself in the scorching art of the Firewall build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Firewall Build"])
                
            #Arc Lash
                elif re.findall("crackling|energy|wrath|lightning", sorc_build.lower()): 
                
                    print ("\nCongratulations, esteemed sorceress, on your unwavering dedication to the arcane arts!\nYour choice to embrace the electrifying power of the Arc Lash build is a testament to your mastery over the forces of lightning and your thirst for unparalleled devastation.")
                    print ("May your path be illuminated by the electrifying brilliance of Arc Lash, and may your enemies tremble in the face of your overwhelming might.\nHere's a site to immerse yourself in the electrifying art of the Arc Lash build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Arc Lash Build"])
                
            #Meteor
                elif re.findall("harnessing|cataclysmic|might|celestial|fire|heavens", sorc_build.lower()): 
                
                    print ("\nCongratulations, illustrious sorceress, on your unwavering devotion to the arcane arts!\nYour choice to harness the cataclysmic might of the Meteor build is a testament to your command over celestial forces and your insatiable thirst for destruction.")
                    print ("May your path be illuminated by the celestial brilliance of Meteor, and may your enemies quiver in the face of your unrelenting power.\nHere's a site to delve into the cataclysmic art of the Meteor build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Meteor Build"])
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Sorceress')

            
    #Spellcasters without Sorcs
        elif "Sorceress" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = input("\nWill you embrace the primal harmony of nature or delve into the forbidden arts of life and death to shape your path?\nYour Answer: ")
        
        #Necromancer
            if "Necromancer" in Classes and re.findall("life|death|shape|path", elements_1):
                necro_build = input("Which sinister manifestation shall you command, wielding the deadly piercing essence of bone, inflicting ruthless severance upon your enemies, harnessing the unholy power of blood to lance through their defenses, or casting a vile blight that corrodes all life in its path?\nYour Answer: ")
            
        #Bone Spear
                if re.findall("wielding|deadly|piercing|essence|bone", necro_build.lower()):
                    print ("\nCongratulations, revered master of the dark arts, for embracing the necromantic path within the realms of Sanctuary!\nYour choice to harness the arcane powers of bone and wield the deadly precision of the Bone Spear build is a testament to your command over life and death.")
                    print ("May your path be adorned with the echoes of fallen foes, and may the spoils of victory be yours to claim.\nHere's a site to unveil the dread power of the Bone Spear build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Bone Spear Build"])

        #Sever
                elif re.findall("inflicting|ruthless|severance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for venturing into the shadows of Sanctuary as a devoted practitioner of the dark arts!\nYou have tapped into the boundless power of life and death.\nEmbrace your destiny and wield the devastating Sever build with unforgiving precision.")
                    print ("May your path be shrouded in the echoes of vanquished souls, and may the spoils of your triumphs be abundant.\nHere's a site to unleash the relentless power of the Sever build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Sever Build"])
        
        #Blood Lance
                elif re.findall("harnessing|unholy|power|blood|lance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the forbidden powers that flow through your veins!\nYour choice to wield the dark and insidious might of the Blood Lance build is a testament to your command over the very essence of life itself.")
                    print ("May your path be drenched in the crimson hues of sacrifice, and may the spoils of your conquests flow abundantly.\nHere's a site to unleash the unholy power of the Blood Lance build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blood Lance Build"])
        #Blight
                elif re.findall("casting|vile|blight|corrodes|life", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the darkness that shrouds the realm of Sanctuary!\nYou have delved into the forbidden depths of life and death, and now, you wield the malignant power of the Blight build, casting an unrelenting plague upon your enemies.")
                    print ("May your path be cloaked in the suffocating embrace of blight, and may the spoils of your conquests reek of decay.\nHere's a site to unleash the unrelenting power of the Blight build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blight Build"])
            
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Necromancer')


        #Druid
            elif "Druid" in Classes and re.findall("primal|harmony|nature", elements_1):
                druid_build = input("\nWhich path shall you embrace, summoning the chaotic might of swirling tempests, unleashing the untamed ferocity of nature's wrath, channeling the unyielding strength of the earth's core, or commanding the electrifying fury of celestial storms?\nYour Answer: ")
            
            #Tornado
                if re.findall("summoning|chaotic|might|swirling|tempests", druid_build.lower()):
                    print ("\nCongratulations, mighty druid, on your primal connection to nature!\nYour choice to embody the relentless force of the Tornado build is a testament to your mastery over the elements and your unwavering spirit.")
                    print ("May your path be woven in harmony with the winds, and may your enemies tremble in the face of your indomitable power.\nHere's a site to delve into the tempestuous art of the Tornado build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Tornado Build"])
                
            #Shred
                if re.findall("unleashing|untamed|ferocity|wrath", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the savage might of the Shred build is a testament to your primal ferocity and unwavering resolve.")
                    print ("May your path be entwined with the raw fury of nature, and may your enemies tremble in the face of your untamed power.\nHere's a site to delve into the savage art of the Shred build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Shred Build"])

            #Pulverize
                if re.findall("channeling|unyielding|strength|core", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the unyielding might of the Pulverize build is a testament to your indomitable strength and unwavering determination.")
                    print ("May your path be paved with the unyielding strength of the mountains, and may your enemies tremble in the face of your unstoppable force.\nHere's a site to delve into the earth-shaking art of the Pulverize build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Pulverize Build"])
                
            #Lightning Storm
                if re.findall("commanding|electrifying|fury|celestial|storms", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to harness the electrifying might of the Lightning Storm build is a testament to your mastery over the storms and your unwavering connection to the very essence of lightning.")
                    print ("May your path be illuminated by the crackling brilliance of Lightning Storm, and may your enemies tremble in the face of your electrifying power.\nHere's a site to delve into the electrifying art of the Lightning Storm build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Lightning Storm Build"])
                
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Druid')

        #Spellcasters without Necromancers
        elif "Necromancer" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = input("\nWill you embrace the primal harmony of nature or unleash the arcane forces of magic?\nYour Answer: ")
        
        #Sorceress
            if "Sorceress" in Classes and re.findall("arcane|forces|magic", elements_1):
                sorc_build = input("Whose power shall you embrace, wielding the chilling forces of icy devastation, conjuring infernal flames to engulf your enemies, channeling the crackling energy of lightning's wrath, or harnessing the cataclysmic might of celestial fire from the heavens above?\nYour Answer: ")
            
            #Ice Shards
                if re.findall("chilling|forces|icy|devastation", sorc_build.lower()):

                    print("\nCongratulations, formidable sorceress, on your unwavering dedication to the path of magic!\nYour choice to wield the chilling might of Ice Shards speaks volumes of your profound mastery over the elements.")
                    print("May your path be adorned with frozen grandeur, and may your enemies quiver in the face of your unyielding power.\nHere's a site to explore the chilling art of Ice Shards and claim your rightful place among the most esteemed sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Ice Shards Build"])
                
            #Firewall
                elif re.findall("conjuring|infernal|flames|engulf", sorc_build.lower()):

                    print ("\nCongratulations, mighty sorceress, on your unwavering dedication to the mystical arts!\nYour choice to embrace the scorching power of the Firewall build is a testament to your fiery spirit and insatiable hunger for destruction.")
                    print ("May your path be forged in the crucible of flames, and may your enemies tremble in the face of your unrelenting power.\nHere's a site to immerse yourself in the scorching art of the Firewall build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Firewall Build"])
                
            #Arc Lash
                elif re.findall("crackling|energy|wrath|lightning", sorc_build.lower()): 
                
                    print ("\nCongratulations, esteemed sorceress, on your unwavering dedication to the arcane arts!\nYour choice to embrace the electrifying power of the Arc Lash build is a testament to your mastery over the forces of lightning and your thirst for unparalleled devastation.")
                    print ("May your path be illuminated by the electrifying brilliance of Arc Lash, and may your enemies tremble in the face of your overwhelming might.\nHere's a site to immerse yourself in the electrifying art of the Arc Lash build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Arc Lash Build"])
                
            #Meteor
                elif re.findall("harnessing|cataclysmic|might|celestial|fire|heavens", sorc_build.lower()): 
                
                    print ("\nCongratulations, illustrious sorceress, on your unwavering devotion to the arcane arts!\nYour choice to harness the cataclysmic might of the Meteor build is a testament to your command over celestial forces and your insatiable thirst for destruction.")
                    print ("May your path be illuminated by the celestial brilliance of Meteor, and may your enemies quiver in the face of your unrelenting power.\nHere's a site to delve into the cataclysmic art of the Meteor build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Meteor Build"])
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Sorceress')
                
        #Druid
            elif "Druid" in Classes and re.findall("primal|harmony|nature", elements_1):
                druid_build = input("\nWhich path shall you embrace, summoning the chaotic might of swirling tempests, unleashing the untamed ferocity of nature's wrath, channeling the unyielding strength of the earth's core, or commanding the electrifying fury of celestial storms?\nYour Answer: ")
            
            #Tornado
                if re.findall("summoning|chaotic|might|swirling|tempests", druid_build.lower()):
                    print ("\nCongratulations, mighty druid, on your primal connection to nature!\nYour choice to embody the relentless force of the Tornado build is a testament to your mastery over the elements and your unwavering spirit.")
                    print ("May your path be woven in harmony with the winds, and may your enemies tremble in the face of your indomitable power.\nHere's a site to delve into the tempestuous art of the Tornado build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Tornado Build"])
                
            #Shred
                if re.findall("unleashing|untamed|ferocity|wrath", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the savage might of the Shred build is a testament to your primal ferocity and unwavering resolve.")
                    print ("May your path be entwined with the raw fury of nature, and may your enemies tremble in the face of your untamed power.\nHere's a site to delve into the savage art of the Shred build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Shred Build"])

            #Pulverize
                if re.findall("channeling|unyielding|strength|core", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the unyielding might of the Pulverize build is a testament to your indomitable strength and unwavering determination.")
                    print ("May your path be paved with the unyielding strength of the mountains, and may your enemies tremble in the face of your unstoppable force.\nHere's a site to delve into the earth-shaking art of the Pulverize build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Pulverize Build"])
                
            #Lightning Storm
                if re.findall("commanding|electrifying|fury|celestial|storms", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to harness the electrifying might of the Lightning Storm build is a testament to your mastery over the storms and your unwavering connection to the very essence of lightning.")
                    print ("May your path be illuminated by the crackling brilliance of Lightning Storm, and may your enemies tremble in the face of your electrifying power.\nHere's a site to delve into the electrifying art of the Lightning Storm build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Lightning Storm Build"])
                
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Druid')
        
        #Spellcasters without Druids
        elif  "Druid" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = input("\nWill you unleash the arcane forces of magic, or delve into the forbidden arts of life and death to shape your path?\nYour Answer: ")
        
        #Necromancer
            if "Necromancer" in Classes and re.findall("life|death|shape|path", elements_1):
                necro_build = input("Which sinister manifestation shall you command, wielding the deadly piercing essence of bone, inflicting ruthless severance upon your enemies, harnessing the unholy power of blood to lance through their defenses, or casting a vile blight that corrodes all life in its path?\nYour Answer: ")
            
        #Bone Spear
                if re.findall("wielding|deadly|piercing|essence|bone", necro_build.lower()):
                    print ("\nCongratulations, revered master of the dark arts, for embracing the necromantic path within the realms of Sanctuary!\nYour choice to harness the arcane powers of bone and wield the deadly precision of the Bone Spear build is a testament to your command over life and death.")
                    print ("May your path be adorned with the echoes of fallen foes, and may the spoils of victory be yours to claim.\nHere's a site to unveil the dread power of the Bone Spear build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Bone Spear Build"])

        #Sever
                elif re.findall("inflicting|ruthless|severance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for venturing into the shadows of Sanctuary as a devoted practitioner of the dark arts!\nYou have tapped into the boundless power of life and death.\nEmbrace your destiny and wield the devastating Sever build with unforgiving precision.")
                    print ("May your path be shrouded in the echoes of vanquished souls, and may the spoils of your triumphs be abundant.\nHere's a site to unleash the relentless power of the Sever build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Sever Build"])
        
        #Blood Lance
                elif re.findall("harnessing|unholy|power|blood|lance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the forbidden powers that flow through your veins!\nYour choice to wield the dark and insidious might of the Blood Lance build is a testament to your command over the very essence of life itself.")
                    print ("May your path be drenched in the crimson hues of sacrifice, and may the spoils of your conquests flow abundantly.\nHere's a site to unleash the unholy power of the Blood Lance build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blood Lance Build"])
        #Blight
                elif re.findall("casting|vile|blight|corrodes|life", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the darkness that shrouds the realm of Sanctuary!\nYou have delved into the forbidden depths of life and death, and now, you wield the malignant power of the Blight build, casting an unrelenting plague upon your enemies.")
                    print ("May your path be cloaked in the suffocating embrace of blight, and may the spoils of your conquests reek of decay.\nHere's a site to unleash the unrelenting power of the Blight build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blight Build"])
            
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Necromancer')


        #Sorceress
            elif "Sorceress" in Classes and re.findall("arcane|forces|magic", elements_1):
                sorc_build = input("\nWhose power shall you embrace, wielding the chilling forces of icy devastation, conjuring infernal flames to engulf your enemies, channeling the crackling energy of lightning's wrath, or harnessing the cataclysmic might of celestial fire from the heavens above?\nYour Answer: ")
            
            #Ice Shards
                if re.findall("chilling|forces|icy|devastation", sorc_build.lower()):

                    print("\nCongratulations, formidable sorceress, on your unwavering dedication to the path of magic!\nYour choice to wield the chilling might of Ice Shards speaks volumes of your profound mastery over the elements.")
                    print("May your path be adorned with frozen grandeur, and may your enemies quiver in the face of your unyielding power.\nHere's a site to explore the chilling art of Ice Shards and claim your rightful place among the most esteemed sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Ice Shards Build"])
                
            #Firewall
                elif re.findall("conjuring|infernal|flames|engulf", sorc_build.lower()):

                    print ("\nCongratulations, mighty sorceress, on your unwavering dedication to the mystical arts!\nYour choice to embrace the scorching power of the Firewall build is a testament to your fiery spirit and insatiable hunger for destruction.")
                    print ("May your path be forged in the crucible of flames, and may your enemies tremble in the face of your unrelenting power.\nHere's a site to immerse yourself in the scorching art of the Firewall build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Firewall Build"])
                
            #Arc Lash
                elif re.findall("crackling|energy|wrath|lightning", sorc_build.lower()): 
                
                    print ("\nCongratulations, esteemed sorceress, on your unwavering dedication to the arcane arts!\nYour choice to embrace the electrifying power of the Arc Lash build is a testament to your mastery over the forces of lightning and your thirst for unparalleled devastation.")
                    print ("May your path be illuminated by the electrifying brilliance of Arc Lash, and may your enemies tremble in the face of your overwhelming might.\nHere's a site to immerse yourself in the electrifying art of the Arc Lash build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Arc Lash Build"])
                
            #Meteor
                elif re.findall("harnessing|cataclysmic|might|celestial|fire|heavens", sorc_build.lower()): 
                
                    print ("\nCongratulations, illustrious sorceress, on your unwavering devotion to the arcane arts!\nYour choice to harness the cataclysmic might of the Meteor build is a testament to your command over celestial forces and your insatiable thirst for destruction.")
                    print ("May your path be illuminated by the celestial brilliance of Meteor, and may your enemies quiver in the face of your unrelenting power.\nHere's a site to delve into the cataclysmic art of the Meteor build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Meteor Build"])
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Sorceress')
        
    
    
    
    #Second Loop Melee Only
    elif "Barbarian" in Classes or "Rogue" in Classes:
        answer_1 = ("stride into the heart of battle, feeling the clash of steel in close quarters")
    
    
    #Melee if both classes still in dictionary
        if "Barbarian" in Classes and "Rogue" in Classes and re.findall("clash|steel|close|quarters", answer_1.lower()):
            weapons_1 = input("Will you stand your ground or strike from the shadows?\nYour Answer: ")
  
        #Barbarian
            if "Barbarian" in Classes and re.findall("stand|your|ground", weapons_1.lower()):
             
             #Barbarian Final Question
                barb_build = input("\nWill you morph into a walking apocalypse and inflict mortal wounds on your enemies, shatter your enemies with the power of earth, become a cyclone of death, or behold the power of the twin blades?\nYour Answer: ")
                
                #Rend 
                if re.findall("walking|apocalypse|inflict|mortal|wounds", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe rend build uses the rend skill to inflict a bleed effect on enemies, which deals damage over time")
                    print ("Wanna learn how to tear through demons like a hot knife through butter?\nHere's a site to learn more about the rend build!\n") 
                    webbrowser.open(Classes["Barbarian"]["Rend Build"])
                    
                #Upheaval
                elif re.findall("shatter|enemies|power|earth", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Upheaval build is a powerful and versatile build that can be used to crush your enemies.\n")
                    print ("This build relies on the Upheaval skill, which allows you to slam the ground and create a shockwave that deals damage to enemies in an area.\nHere's a site to learn more and start sending demons flying!\n") 
                    webbrowser.open(Classes["Barbarian"]["Upheaval Build"])

                #Whirlwind
                elif re.findall("cyclone|death", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Whirlwind build is a devastating and unstoppable build that can be used to tear through your enemies.")
                    print ("If you're looking for a build that can deal massive damage and clear hordes of enemies quickly, then the Whirlwind build is the perfect choice for you. \nHere's a site to learn more and start spinning your way to victory!\n") 
                    webbrowser.open(Classes["Barbarian"]["Whirlwind Build"])
                
            #Double Swing
                elif re.findall("behold|power|twin|blades", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Double Swing build is a powerful and efficient build that can be used to deal massive damage.")
                    print ("This build relies on the Double Swing skill, which allows you to attack twice in rapid succession.\nHere's a site to learn more and start cleaving demons in half!\n") 
                    webbrowser.open(Classes["Barbarian"]["Double Swing Build"])

                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Barbarian')
        
        
        #Rogue 
            elif "Rogue" in Classes and re.findall("strike|shadows", weapons_1.lower()):
            
            #Final Rogue Question
                rogue_build = input("\nWould you rather pierce through enemies with your arrows, unleash a flurry of deadly blades, attack with incredible speed unleashing a barrage of blows, or shred through your foes with pinpoint accuracy?\nYour Answer: ")

            #Penetrating Shot
                if re.findall("piercing|enemies|pierce|through|arrows", rogue_build.lower()):
                    print ("""\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nYou've chosen a powerful and versatile class that is sure to bring you hours of fun.\nThe Penetrating Shot build is an awesome build for the Rogue class.\nIt allows you to deal massive damage from a distance, and it's perfect for those who want to play a Spellcasters character.\nWith this build, you'll be able to pierce through enemies with your arrows, dealing devastating damage.\nJust be sure to stay out of reach, or you'll be in for a world of hurt.""")
                    print ("\nBecome a master of the bow with the Penetrating Shot build! Here's a site to learn more.\n") 
                    webbrowser.open(Classes["Rogue"]["Penetrating Shot Build"])
                
            #Flurry 
                elif re.findall("flurry|deadly|blades", rogue_build.lower()):
                    print("\nCongratulations, brave adventurer, on embracing the path of the Rogue! \nThe Rogue is a fast and agile class that specializes in dealing damage from a distance.\nThe Flurry build is a powerful build that allows you to quickly and easily dispatch your enemies.")
                    print("\nWith the Flurry build, you will become a whirlwind of death, leaving nothing but carnage in your wake.\nSo what are you waiting for? Here's a site to help start your journey to mastery!\n") 
                    webbrowser.open(Classes["Rogue"]["Flurry Build"])
                
            #Twisting Blades
                elif re.findall("attack|incredible|speed|barrage|blows|reeling", rogue_build.lower()):
                    print ("\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nThe rogue is a fast and agile class that specializes in dealing damage from a distance.\nThe Twisting Blades build is a powerful build that allows you to quickly and easily dispatch your enemies.")
                    print ("\nWith the Twisting Blades build, you will become a deadly whirlwind, leaving nothing but destruction in your wake.\nSo what are you waiting for? Here's a site to learn more!\n") 
                    webbrowser.open(Classes["Rogue"]["Twisting Blades Build"])

            #Rapid Fire
                elif re.findall("shred|foes|pinpoint|accuracy", rogue_build.lower()):
                    print ("\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nWithin the chaos of battle, Rapid Fire will become your symphony of destruction.\nThis technique allows you to unleash a torrent of arrows upon your foes, striking them down with relentless precision.\nWith each arrow unleashed, your enemies will tremble in fear as they succumb to the might of your unyielding barrage.")
                    print ("\nTo further refine your understanding of this devastating build, I invite you to embark on a journey of knowledge.\nHere's a site, brave Rogue, and embrace the secrets of Rapid Fire.\nUncover the arcane techniques, the synergistic equipment, and the strategic prowess that will allow you to unleash the true potential of this lethal art.\n") 
                    webbrowser.open(Classes["Rogue"]["Rapid Fire Build"])

            player_amount = player_amount - 1
            player_amount_list.remove(player_amount_list[0])
            Classes.pop('Rogue')
    
    #Melee if Rogue already chosen
        elif "Rogue" not in Classes and re.findall("clash|steel|close|quarters", answer_1.lower()):
            weapons_1 = ("stand your ground")
        #Barbarian
            if "Barbarian" in Classes and re.findall("stand|your|ground", weapons_1.lower()):
             
             #Barbarian Final Question
                barb_build = input("\nWill you morph into a walking apocalypse and inflict mortal wounds on your enemies, shatter your enemies with the power of earth, become a cyclone of death, or behold the power of the twin blades?\nYour Answer: ")
                
                #Rend 
                if re.findall("walking|apocalypse|inflict|mortal|wounds", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe rend build uses the rend skill to inflict a bleed effect on enemies, which deals damage over time")
                    print ("Wanna learn how to tear through demons like a hot knife through butter?\nHere's a site to learn more about the rend build!\n") 
                    webbrowser.open(Classes["Barbarian"]["Rend Build"])
                    
                #Upheaval
                elif re.findall("shatter|enemies|power|earth", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Upheaval build is a powerful and versatile build that can be used to crush your enemies.\n")
                    print ("This build relies on the Upheaval skill, which allows you to slam the ground and create a shockwave that deals damage to enemies in an area.\nHere's a site to learn more and start sending demons flying!\n") 
                    webbrowser.open(Classes["Barbarian"]["Upheaval Build"])

                #Whirlwind
                elif re.findall("cyclone|death", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Whirlwind build is a devastating and unstoppable build that can be used to tear through your enemies.")
                    print ("If you're looking for a build that can deal massive damage and clear hordes of enemies quickly, then the Whirlwind build is the perfect choice for you. \nHere's a site to learn more and start spinning your way to victory!\n") 
                    webbrowser.open(Classes["Barbarian"]["Whirlwind Build"])
                
            #Double Swing
                elif re.findall("behold|power|twin|blades", barb_build.lower()):
                    print ("\nCongratulations on choosing the barbarian class!\nThe Double Swing build is a powerful and efficient build that can be used to deal massive damage.")
                    print ("This build relies on the Double Swing skill, which allows you to attack twice in rapid succession.\nHere's a site to learn more and start cleaving demons in half!\n") 
                    webbrowser.open(Classes["Barbarian"]["Double Swing Build"])

                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Barbarian')
        
    #Melee if Barb alredy chosen
        elif "Barbarian" not in Classes and re.findall("clash|steel|close|quarters", answer_1.lower()):
            weapons_1 = ("strike from the shadows")
        #Rogue 
            if "Rogue" in Classes and re.findall("strike|shadows", weapons_1.lower()):
            
            #Final Rogue Question
                rogue_build = input("\nWould you rather pierce through enemies with your arrows, unleash a flurry of deadly blades, attack with incredible speed unleashing a barrage of blows, or shred through your foes with pinpoint accuracy?\nYour Answer: ")

            #Penetrating Shot
                if re.findall("piercing|enemies|pierce|through|arrows", rogue_build.lower()):
                    print ("""\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nYou've chosen a powerful and versatile class that is sure to bring you hours of fun.\nThe Penetrating Shot build is an awesome build for the Rogue class.\nIt allows you to deal massive damage from a distance, and it's perfect for those who want to play a Spellcasters character.\nWith this build, you'll be able to pierce through enemies with your arrows, dealing devastating damage.\nJust be sure to stay out of reach, or you'll be in for a world of hurt.""")
                    print ("\nBecome a master of the bow with the Penetrating Shot build! Here's a site to learn more.\n") 
                    webbrowser.open(Classes["Rogue"]["Penetrating Shot Build"])
                
            #Flurry 
                elif re.findall("flurry|deadly|blades", rogue_build.lower()):
                    print("\nCongratulations, brave adventurer, on embracing the path of the Rogue! \nThe Rogue is a fast and agile class that specializes in dealing damage from a distance.\nThe Flurry build is a powerful build that allows you to quickly and easily dispatch your enemies.")
                    print("\nWith the Flurry build, you will become a whirlwind of death, leaving nothing but carnage in your wake.\nSo what are you waiting for? Here's a site to help start your journey to mastery!\n") 
                    webbrowser.open(Classes["Rogue"]["Flurry Build"])
                
            #Twisting Blades
                elif re.findall("attack|incredible|speed|barrage|blows|reeling", rogue_build.lower()):
                    print ("\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nThe rogue is a fast and agile class that specializes in dealing damage from a distance.\nThe Twisting Blades build is a powerful build that allows you to quickly and easily dispatch your enemies.")
                    print ("\nWith the Twisting Blades build, you will become a deadly whirlwind, leaving nothing but destruction in your wake.\nSo what are you waiting for? Here's a site to learn more!\n") 
                    webbrowser.open(Classes["Rogue"]["Twisting Blades Build"])

            #Rapid Fire
                elif re.findall("shred|foes|pinpoint|accuracy", rogue_build.lower()):
                    print ("\nCongratulations, brave adventurer, on embracing the path of the Rogue!\nWithin the chaos of battle, Rapid Fire will become your symphony of destruction.\nThis technique allows you to unleash a torrent of arrows upon your foes, striking them down with relentless precision.\nWith each arrow unleashed, your enemies will tremble in fear as they succumb to the might of your unyielding barrage.")
                    print ("\nTo further refine your understanding of this devastating build, I invite you to embark on a journey of knowledge.\nHere's a site, brave Rogue, and embrace the secrets of Rapid Fire.\nUncover the arcane techniques, the synergistic equipment, and the strategic prowess that will allow you to unleash the true potential of this lethal art.\n") 
                    webbrowser.open(Classes["Rogue"]["Rapid Fire Build"])

                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Rogue')



#3rd loop Spellcasters Only
    elif "Barbarian" not in Classes and "Rogue" not in Classes:
        answer_1 = ("the boundless arcane powers that shape the elements and manipulate life and death")
    
    
    
    #Spellcasters
        if "Sorceress" in Classes and "Necromancer" in Classes and "Druid" in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = input("\nWill you embrace the primal harmony of nature, unleash the arcane forces of magic, or delve into the forbidden arts of life and death to shape your path?\nYour Answer: ")
        
        #Necromancer
            if "Necromancer" in Classes and re.findall("life|death|shape|path", elements_1):
                necro_build = input("Which sinister manifestation shall you command, wielding the deadly piercing essence of bone, inflicting ruthless severance upon your enemies, harnessing the unholy power of blood to lance through their defenses, or casting a vile blight that corrodes all life in its path?\nYour Answer: ")
            
        #Bone Spear
                if re.findall("wielding|deadly|piercing|essence|bone", necro_build.lower()):
                    print ("\nCongratulations, revered master of the dark arts, for embracing the necromantic path within the realms of Sanctuary!\nYour choice to harness the arcane powers of bone and wield the deadly precision of the Bone Spear build is a testament to your command over life and death.")
                    print ("May your path be adorned with the echoes of fallen foes, and may the spoils of victory be yours to claim.\nHere's a site to unveil the dread power of the Bone Spear build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Bone Spear Build"])

        #Sever
                elif re.findall("inflicting|ruthless|severance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for venturing into the shadows of Sanctuary as a devoted practitioner of the dark arts!\nYou have tapped into the boundless power of life and death.\nEmbrace your destiny and wield the devastating Sever build with unforgiving precision.")
                    print ("May your path be shrouded in the echoes of vanquished souls, and may the spoils of your triumphs be abundant.\nHere's a site to unleash the relentless power of the Sever build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Sever Build"])
        
        #Blood Lance
                elif re.findall("harnessing|unholy|power|blood|lance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the forbidden powers that flow through your veins!\nYour choice to wield the dark and insidious might of the Blood Lance build is a testament to your command over the very essence of life itself.")
                    print ("May your path be drenched in the crimson hues of sacrifice, and may the spoils of your conquests flow abundantly.\nHere's a site to unleash the unholy power of the Blood Lance build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blood Lance Build"])
        #Blight
                elif re.findall("casting|vile|blight|corrodes|life", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the darkness that shrouds the realm of Sanctuary!\nYou have delved into the forbidden depths of life and death, and now, you wield the malignant power of the Blight build, casting an unrelenting plague upon your enemies.")
                    print ("May your path be cloaked in the suffocating embrace of blight, and may the spoils of your conquests reek of decay.\nHere's a site to unleash the unrelenting power of the Blight build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blight Build"])
            
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Necromancer')


        #Sorceress
            elif "Sorceress" in Classes and re.findall("arcane|forces|magic", elements_1):
                sorc_build = input("\nWhose power shall you embrace, wielding the chilling forces of icy devastation, conjuring infernal flames to engulf your enemies, channeling the crackling energy of lightning's wrath, or harnessing the cataclysmic might of celestial fire from the heavens above?\nYour Answer: ")
            
            #Ice Shards
                if re.findall("chilling|forces|icy|devastation", sorc_build.lower()):

                    print("\nCongratulations, formidable sorceress, on your unwavering dedication to the path of magic!\nYour choice to wield the chilling might of Ice Shards speaks volumes of your profound mastery over the elements.")
                    print("May your path be adorned with frozen grandeur, and may your enemies quiver in the face of your unyielding power.\nHere's a site to explore the chilling art of Ice Shards and claim your rightful place among the most esteemed sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Ice Shards Build"])
                
            #Firewall
                elif re.findall("conjuring|infernal|flames|engulf", sorc_build.lower()):

                    print ("\nCongratulations, mighty sorceress, on your unwavering dedication to the mystical arts!\nYour choice to embrace the scorching power of the Firewall build is a testament to your fiery spirit and insatiable hunger for destruction.")
                    print ("May your path be forged in the crucible of flames, and may your enemies tremble in the face of your unrelenting power.\nHere's a site to immerse yourself in the scorching art of the Firewall build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Firewall Build"])
                
            #Arc Lash
                elif re.findall("crackling|energy|wrath|lightning", sorc_build.lower()): 
                
                    print ("\nCongratulations, esteemed sorceress, on your unwavering dedication to the arcane arts!\nYour choice to embrace the electrifying power of the Arc Lash build is a testament to your mastery over the forces of lightning and your thirst for unparalleled devastation.")
                    print ("May your path be illuminated by the electrifying brilliance of Arc Lash, and may your enemies tremble in the face of your overwhelming might.\nHere's a site to immerse yourself in the electrifying art of the Arc Lash build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Arc Lash Build"])
                
            #Meteor
                elif re.findall("harnessing|cataclysmic|might|celestial|fire|heavens", sorc_build.lower()): 
                
                    print ("\nCongratulations, illustrious sorceress, on your unwavering devotion to the arcane arts!\nYour choice to harness the cataclysmic might of the Meteor build is a testament to your command over celestial forces and your insatiable thirst for destruction.")
                    print ("May your path be illuminated by the celestial brilliance of Meteor, and may your enemies quiver in the face of your unrelenting power.\nHere's a site to delve into the cataclysmic art of the Meteor build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Meteor Build"])
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Sorceress')
            
            
        #Druid
            elif "Druid" in Classes and re.findall("primal|harmony|nature", elements_1):
                druid_build = input("Which path shall you embrace, summoning the chaotic might of swirling tempests, unleashing the untamed ferocity of nature's wrath, channeling the unyielding strength of the earth's core, or commanding the electrifying fury of celestial storms?\nYour Answer: ")
            
            #Tornado
                if re.findall("summoning|chaotic|might|swirling|tempests", druid_build.lower()):
                    print ("\nCongratulations, mighty druid, on your primal connection to nature!\nYour choice to embody the relentless force of the Tornado build is a testament to your mastery over the elements and your unwavering spirit.")
                    print ("May your path be woven in harmony with the winds, and may your enemies tremble in the face of your indomitable power.\nHere's a site to delve into the tempestuous art of the Tornado build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Tornado Build"])
                
            #Shred
                if re.findall("unleashing|untamed|ferocity|wrath", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the savage might of the Shred build is a testament to your primal ferocity and unwavering resolve.")
                    print ("May your path be entwined with the raw fury of nature, and may your enemies tremble in the face of your untamed power.\nHere's a site to delve into the savage art of the Shred build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Shred Build"])

            #Pulverize
                if re.findall("channeling|unyielding|strength|core", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the unyielding might of the Pulverize build is a testament to your indomitable strength and unwavering determination.")
                    print ("May your path be paved with the unyielding strength of the mountains, and may your enemies tremble in the face of your unstoppable force.\nHere's a site to delve into the earth-shaking art of the Pulverize build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Pulverize Build"])
                
            #Lightning Storm
                if re.findall("commanding|electrifying|fury|celestial|storms", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to harness the electrifying might of the Lightning Storm build is a testament to your mastery over the storms and your unwavering connection to the very essence of lightning.")
                    print ("May your path be illuminated by the crackling brilliance of Lightning Storm, and may your enemies tremble in the face of your electrifying power.\nHere's a site to delve into the electrifying art of the Lightning Storm build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Lightning Storm Build"])
                
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Druid')




        #ONLY DRUIDS
        elif "Sorceress" not in Classes and "Necromancer" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = "Will you embrace the primal harmony of nature"
        #Druid
            if "Druid" in Classes and re.findall("primal|harmony|nature", elements_1):
                druid_build = input("\nWhich path shall you embrace, summoning the chaotic might of swirling tempests, unleashing the untamed ferocity of nature's wrath, channeling the unyielding strength of the earth's core, or commanding the electrifying fury of celestial storms?\nYour Answer: ")
            
            #Tornado
                if re.findall("summoning|chaotic|might|swirling|tempests", druid_build.lower()):
                    print ("\nCongratulations, mighty druid, on your primal connection to nature!\nYour choice to embody the relentless force of the Tornado build is a testament to your mastery over the elements and your unwavering spirit.")
                    print ("May your path be woven in harmony with the winds, and may your enemies tremble in the face of your indomitable power.\nHere's a site to delve into the tempestuous art of the Tornado build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Tornado Build"])
                
            #Shred
                if re.findall("unleashing|untamed|ferocity|wrath", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the savage might of the Shred build is a testament to your primal ferocity and unwavering resolve.")
                    print ("May your path be entwined with the raw fury of nature, and may your enemies tremble in the face of your untamed power.\nHere's a site to delve into the savage art of the Shred build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Shred Build"])

            #Pulverize
                if re.findall("channeling|unyielding|strength|core", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the unyielding might of the Pulverize build is a testament to your indomitable strength and unwavering determination.")
                    print ("May your path be paved with the unyielding strength of the mountains, and may your enemies tremble in the face of your unstoppable force.\nHere's a site to delve into the earth-shaking art of the Pulverize build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Pulverize Build"])
                
            #Lightning Storm
                if re.findall("commanding|electrifying|fury|celestial|storms", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to harness the electrifying might of the Lightning Storm build is a testament to your mastery over the storms and your unwavering connection to the very essence of lightning.")
                    print ("May your path be illuminated by the crackling brilliance of Lightning Storm, and may your enemies tremble in the face of your electrifying power.\nHere's a site to delve into the electrifying art of the Lightning Storm build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Lightning Storm Build"])
                
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Druid')

        #ONLY NECROS
        elif "Sorceress" not in Classes and "Druid" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = "delve into the forbidden arts of life and death to shape your path?"
        
        #Necromancer
            if "Necromancer" in Classes and re.findall("life|death|shape|path", elements_1):
                necro_build = input("\nWhich sinister manifestation shall you command, wielding the deadly piercing essence of bone, inflicting ruthless severance upon your enemies, harnessing the unholy power of blood to lance through their defenses, or casting a vile blight that corrodes all life in its path?\nYour Answer: ")
            
        #Bone Spear
                if re.findall("wielding|deadly|piercing|essence|bone", necro_build.lower()):
                    print ("\nCongratulations, revered master of the dark arts, for embracing the necromantic path within the realms of Sanctuary!\nYour choice to harness the arcane powers of bone and wield the deadly precision of the Bone Spear build is a testament to your command over life and death.")
                    print ("May your path be adorned with the echoes of fallen foes, and may the spoils of victory be yours to claim.\nHere's a site to unveil the dread power of the Bone Spear build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Bone Spear Build"])

        #Sever
                elif re.findall("inflicting|ruthless|severance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for venturing into the shadows of Sanctuary as a devoted practitioner of the dark arts!\nYou have tapped into the boundless power of life and death.\nEmbrace your destiny and wield the devastating Sever build with unforgiving precision.")
                    print ("May your path be shrouded in the echoes of vanquished souls, and may the spoils of your triumphs be abundant.\nHere's a site to unleash the relentless power of the Sever build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Sever Build"])
        
        #Blood Lance
                elif re.findall("harnessing|unholy|power|blood|lance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the forbidden powers that flow through your veins!\nYour choice to wield the dark and insidious might of the Blood Lance build is a testament to your command over the very essence of life itself.")
                    print ("May your path be drenched in the crimson hues of sacrifice, and may the spoils of your conquests flow abundantly.\nHere's a site to unleash the unholy power of the Blood Lance build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blood Lance Build"])
        #Blight
                elif re.findall("casting|vile|blight|corrodes|life", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the darkness that shrouds the realm of Sanctuary!\nYou have delved into the forbidden depths of life and death, and now, you wield the malignant power of the Blight build, casting an unrelenting plague upon your enemies.")
                    print ("May your path be cloaked in the suffocating embrace of blight, and may the spoils of your conquests reek of decay.\nHere's a site to unleash the unrelenting power of the Blight build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blight Build"])
            
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Necromancer')

        #ONLY SORCS
        if "Necromancer" not in Classes and "Druid" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = "unleash the arcane forces of magic"
        #Sorceress
            if "Sorceress" in Classes and re.findall("arcane|forces|magic", elements_1):
                sorc_build = input("\nWhose power shall you embrace, wielding the chilling forces of icy devastation, conjuring infernal flames to engulf your enemies, channeling the crackling energy of lightning's wrath, or harnessing the cataclysmic might of celestial fire from the heavens above?\nYour Answer: ")
            
            #Ice Shards
                if re.findall("chilling|forces|icy|devastation", sorc_build.lower()):

                    print("\nCongratulations, formidable sorceress, on your unwavering dedication to the path of magic!\nYour choice to wield the chilling might of Ice Shards speaks volumes of your profound mastery over the elements.")
                    print("May your path be adorned with frozen grandeur, and may your enemies quiver in the face of your unyielding power.\nHere's a site to explore the chilling art of Ice Shards and claim your rightful place among the most esteemed sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Ice Shards Build"])
                
            #Firewall
                elif re.findall("conjuring|infernal|flames|engulf", sorc_build.lower()):

                    print ("\nCongratulations, mighty sorceress, on your unwavering dedication to the mystical arts!\nYour choice to embrace the scorching power of the Firewall build is a testament to your fiery spirit and insatiable hunger for destruction.")
                    print ("May your path be forged in the crucible of flames, and may your enemies tremble in the face of your unrelenting power.\nHere's a site to immerse yourself in the scorching art of the Firewall build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Firewall Build"])
                
            #Arc Lash
                elif re.findall("crackling|energy|wrath|lightning", sorc_build.lower()): 
                
                    print ("\nCongratulations, esteemed sorceress, on your unwavering dedication to the arcane arts!\nYour choice to embrace the electrifying power of the Arc Lash build is a testament to your mastery over the forces of lightning and your thirst for unparalleled devastation.")
                    print ("May your path be illuminated by the electrifying brilliance of Arc Lash, and may your enemies tremble in the face of your overwhelming might.\nHere's a site to immerse yourself in the electrifying art of the Arc Lash build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Arc Lash Build"])
                
            #Meteor
                elif re.findall("harnessing|cataclysmic|might|celestial|fire|heavens", sorc_build.lower()): 
                
                    print ("\nCongratulations, illustrious sorceress, on your unwavering devotion to the arcane arts!\nYour choice to harness the cataclysmic might of the Meteor build is a testament to your command over celestial forces and your insatiable thirst for destruction.")
                    print ("May your path be illuminated by the celestial brilliance of Meteor, and may your enemies quiver in the face of your unrelenting power.\nHere's a site to delve into the cataclysmic art of the Meteor build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Meteor Build"])
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Sorceress')

            
    #Spellcasters without Sorcs
        elif "Sorceress" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = input("\nWill you embrace the primal harmony of nature or delve into the forbidden arts of life and death to shape your path?\nYour Answer: ")
        
        #Necromancer
            if "Necromancer" in Classes and re.findall("life|death|shape|path", elements_1):
                necro_build = input("Which sinister manifestation shall you command, wielding the deadly piercing essence of bone, inflicting ruthless severance upon your enemies, harnessing the unholy power of blood to lance through their defenses, or casting a vile blight that corrodes all life in its path?\nYour Answer: ")
            
        #Bone Spear
                if re.findall("wielding|deadly|piercing|essence|bone", necro_build.lower()):
                    print ("\nCongratulations, revered master of the dark arts, for embracing the necromantic path within the realms of Sanctuary!\nYour choice to harness the arcane powers of bone and wield the deadly precision of the Bone Spear build is a testament to your command over life and death.")
                    print ("May your path be adorned with the echoes of fallen foes, and may the spoils of victory be yours to claim.\nHere's a site to unveil the dread power of the Bone Spear build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Bone Spear Build"])

        #Sever
                elif re.findall("inflicting|ruthless|severance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for venturing into the shadows of Sanctuary as a devoted practitioner of the dark arts!\nYou have tapped into the boundless power of life and death.\nEmbrace your destiny and wield the devastating Sever build with unforgiving precision.")
                    print ("May your path be shrouded in the echoes of vanquished souls, and may the spoils of your triumphs be abundant.\nHere's a site to unleash the relentless power of the Sever build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Sever Build"])
        
        #Blood Lance
                elif re.findall("harnessing|unholy|power|blood|lance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the forbidden powers that flow through your veins!\nYour choice to wield the dark and insidious might of the Blood Lance build is a testament to your command over the very essence of life itself.")
                    print ("May your path be drenched in the crimson hues of sacrifice, and may the spoils of your conquests flow abundantly.\nHere's a site to unleash the unholy power of the Blood Lance build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blood Lance Build"])
        #Blight
                elif re.findall("casting|vile|blight|corrodes|life", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the darkness that shrouds the realm of Sanctuary!\nYou have delved into the forbidden depths of life and death, and now, you wield the malignant power of the Blight build, casting an unrelenting plague upon your enemies.")
                    print ("May your path be cloaked in the suffocating embrace of blight, and may the spoils of your conquests reek of decay.\nHere's a site to unleash the unrelenting power of the Blight build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blight Build"])
            
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Necromancer')


        #Druid
            elif "Druid" in Classes and re.findall("primal|harmony|nature", elements_1):
                druid_build = input("\nWhich path shall you embrace, summoning the chaotic might of swirling tempests, unleashing the untamed ferocity of nature's wrath, channeling the unyielding strength of the earth's core, or commanding the electrifying fury of celestial storms?\nYour Answer: ")
            
            #Tornado
                if re.findall("summoning|chaotic|might|swirling|tempests", druid_build.lower()):
                    print ("\nCongratulations, mighty druid, on your primal connection to nature!\nYour choice to embody the relentless force of the Tornado build is a testament to your mastery over the elements and your unwavering spirit.")
                    print ("May your path be woven in harmony with the winds, and may your enemies tremble in the face of your indomitable power.\nHere's a site to delve into the tempestuous art of the Tornado build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Tornado Build"])
                
            #Shred
                if re.findall("unleashing|untamed|ferocity|wrath", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the savage might of the Shred build is a testament to your primal ferocity and unwavering resolve.")
                    print ("May your path be entwined with the raw fury of nature, and may your enemies tremble in the face of your untamed power.\nHere's a site to delve into the savage art of the Shred build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Shred Build"])

            #Pulverize
                if re.findall("channeling|unyielding|strength|core", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the unyielding might of the Pulverize build is a testament to your indomitable strength and unwavering determination.")
                    print ("May your path be paved with the unyielding strength of the mountains, and may your enemies tremble in the face of your unstoppable force.\nHere's a site to delve into the earth-shaking art of the Pulverize build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Pulverize Build"])
                
            #Lightning Storm
                if re.findall("commanding|electrifying|fury|celestial|storms", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to harness the electrifying might of the Lightning Storm build is a testament to your mastery over the storms and your unwavering connection to the very essence of lightning.")
                    print ("May your path be illuminated by the crackling brilliance of Lightning Storm, and may your enemies tremble in the face of your electrifying power.\nHere's a site to delve into the electrifying art of the Lightning Storm build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Lightning Storm Build"])
                
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Druid')

        #Spellcasters without Necromancers
        elif "Necromancer" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = input("\nWill you embrace the primal harmony of nature or unleash the arcane forces of magic?\nYour Answer: ")
        
        #Sorceress
            if "Sorceress" in Classes and re.findall("arcane|forces|magic", elements_1):
                sorc_build = input("Whose power shall you embrace, wielding the chilling forces of icy devastation, conjuring infernal flames to engulf your enemies, channeling the crackling energy of lightning's wrath, or harnessing the cataclysmic might of celestial fire from the heavens above?\nYour Answer: ")
            
            #Ice Shards
                if re.findall("chilling|forces|icy|devastation", sorc_build.lower()):

                    print("\nCongratulations, formidable sorceress, on your unwavering dedication to the path of magic!\nYour choice to wield the chilling might of Ice Shards speaks volumes of your profound mastery over the elements.")
                    print("May your path be adorned with frozen grandeur, and may your enemies quiver in the face of your unyielding power.\nHere's a site to explore the chilling art of Ice Shards and claim your rightful place among the most esteemed sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Ice Shards Build"])
                
            #Firewall
                elif re.findall("conjuring|infernal|flames|engulf", sorc_build.lower()):

                    print ("\nCongratulations, mighty sorceress, on your unwavering dedication to the mystical arts!\nYour choice to embrace the scorching power of the Firewall build is a testament to your fiery spirit and insatiable hunger for destruction.")
                    print ("May your path be forged in the crucible of flames, and may your enemies tremble in the face of your unrelenting power.\nHere's a site to immerse yourself in the scorching art of the Firewall build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Firewall Build"])
                
            #Arc Lash
                elif re.findall("crackling|energy|wrath|lightning", sorc_build.lower()): 
                
                    print ("\nCongratulations, esteemed sorceress, on your unwavering dedication to the arcane arts!\nYour choice to embrace the electrifying power of the Arc Lash build is a testament to your mastery over the forces of lightning and your thirst for unparalleled devastation.")
                    print ("May your path be illuminated by the electrifying brilliance of Arc Lash, and may your enemies tremble in the face of your overwhelming might.\nHere's a site to immerse yourself in the electrifying art of the Arc Lash build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Arc Lash Build"])
                
            #Meteor
                elif re.findall("harnessing|cataclysmic|might|celestial|fire|heavens", sorc_build.lower()): 
                
                    print ("\nCongratulations, illustrious sorceress, on your unwavering devotion to the arcane arts!\nYour choice to harness the cataclysmic might of the Meteor build is a testament to your command over celestial forces and your insatiable thirst for destruction.")
                    print ("May your path be illuminated by the celestial brilliance of Meteor, and may your enemies quiver in the face of your unrelenting power.\nHere's a site to delve into the cataclysmic art of the Meteor build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Meteor Build"])
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Sorceress')
            
            
        #Druid
            elif "Druid" in Classes and re.findall("primal|harmony|nature", elements_1):
                druid_build = input("\nWhich path shall you embrace, summoning the chaotic might of swirling tempests, unleashing the untamed ferocity of nature's wrath, channeling the unyielding strength of the earth's core, or commanding the electrifying fury of celestial storms?\nYour Answer: ")
            
            #Tornado
                if re.findall("summoning|chaotic|might|swirling|tempests", druid_build.lower()):
                    print ("\nCongratulations, mighty druid, on your primal connection to nature!\nYour choice to embody the relentless force of the Tornado build is a testament to your mastery over the elements and your unwavering spirit.")
                    print ("May your path be woven in harmony with the winds, and may your enemies tremble in the face of your indomitable power.\nHere's a site to delve into the tempestuous art of the Tornado build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Tornado Build"])
                
            #Shred
                if re.findall("unleashing|untamed|ferocity|wrath", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the savage might of the Shred build is a testament to your primal ferocity and unwavering resolve.")
                    print ("May your path be entwined with the raw fury of nature, and may your enemies tremble in the face of your untamed power.\nHere's a site to delve into the savage art of the Shred build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Shred Build"])

            #Pulverize
                if re.findall("channeling|unyielding|strength|core", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to embody the unyielding might of the Pulverize build is a testament to your indomitable strength and unwavering determination.")
                    print ("May your path be paved with the unyielding strength of the mountains, and may your enemies tremble in the face of your unstoppable force.\nHere's a site to delve into the earth-shaking art of the Pulverize build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Pulverize Build"])
                
            #Lightning Storm
                if re.findall("commanding|electrifying|fury|celestial|storms", druid_build.lower()):
                
                    print ("\nCongratulations, revered druid, on your profound attunement to the primal forces!\nYour choice to harness the electrifying might of the Lightning Storm build is a testament to your mastery over the storms and your unwavering connection to the very essence of lightning.")
                    print ("May your path be illuminated by the crackling brilliance of Lightning Storm, and may your enemies tremble in the face of your electrifying power.\nHere's a site to delve into the electrifying art of the Lightning Storm build and claim your rightful place among the revered druids.\n") 
                    webbrowser.open(Classes["Druid"]["Lightning Storm Build"])
                
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Druid')
        
        #Spellcasters without Druids
        elif  "Druid" not in Classes and re.findall("boundless|arcane|powers|elements|manipulate|life|death", answer_1.lower()):
            elements_1 = input("\nWill you unleash the arcane forces of magic, or delve into the forbidden arts of life and death to shape your path?\nYour Answer: ")
        
        #Necromancer
            if "Necromancer" in Classes and re.findall("life|death|shape|path", elements_1):
                necro_build = input("Which sinister manifestation shall you command, wielding the deadly piercing essence of bone, inflicting ruthless severance upon your enemies, harnessing the unholy power of blood to lance through their defenses, or casting a vile blight that corrodes all life in its path?\nYour Answer: ")
            
        #Bone Spear
                if re.findall("wielding|deadly|piercing|essence|bone", necro_build.lower()):
                    print ("\nCongratulations, revered master of the dark arts, for embracing the necromantic path within the realms of Sanctuary!\nYour choice to harness the arcane powers of bone and wield the deadly precision of the Bone Spear build is a testament to your command over life and death.")
                    print ("May your path be adorned with the echoes of fallen foes, and may the spoils of victory be yours to claim.\nHere's a site to unveil the dread power of the Bone Spear build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Bone Spear Build"])

        #Sever
                elif re.findall("inflicting|ruthless|severance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for venturing into the shadows of Sanctuary as a devoted practitioner of the dark arts!\nYou have tapped into the boundless power of life and death.\nEmbrace your destiny and wield the devastating Sever build with unforgiving precision.")
                    print ("May your path be shrouded in the echoes of vanquished souls, and may the spoils of your triumphs be abundant.\nHere's a site to unleash the relentless power of the Sever build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Sever Build"])
        
        #Blood Lance
                elif re.findall("harnessing|unholy|power|blood|lance", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the forbidden powers that flow through your veins!\nYour choice to wield the dark and insidious might of the Blood Lance build is a testament to your command over the very essence of life itself.")
                    print ("May your path be drenched in the crimson hues of sacrifice, and may the spoils of your conquests flow abundantly.\nHere's a site to unleash the unholy power of the Blood Lance build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blood Lance Build"])
        #Blight
                elif re.findall("casting|vile|blight|corrodes|life", necro_build.lower()):
                    print ("\nCongratulations, esteemed master of the necromantic arts, for embracing the darkness that shrouds the realm of Sanctuary!\nYou have delved into the forbidden depths of life and death, and now, you wield the malignant power of the Blight build, casting an unrelenting plague upon your enemies.")
                    print ("May your path be cloaked in the suffocating embrace of blight, and may the spoils of your conquests reek of decay.\nHere's a site to unleash the unrelenting power of the Blight build and claim your rightful place among the esteemed necromancers.\n") 
                    webbrowser.open(Classes["Necromancer"]["Blight Build"])
            
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Necromancer')


        #Sorceress
            elif "Sorceress" in Classes and re.findall("arcane|forces|magic", elements_1):
                sorc_build = input("\nWhose power shall you embrace, wielding the chilling forces of icy devastation, conjuring infernal flames to engulf your enemies, channeling the crackling energy of lightning's wrath, or harnessing the cataclysmic might of celestial fire from the heavens above?\nYour Answer: ")
            
            #Ice Shards
                if re.findall("chilling|forces|icy|devastation", sorc_build.lower()):

                    print("\nCongratulations, formidable sorceress, on your unwavering dedication to the path of magic!\nYour choice to wield the chilling might of Ice Shards speaks volumes of your profound mastery over the elements.")
                    print("May your path be adorned with frozen grandeur, and may your enemies quiver in the face of your unyielding power.\nHere's a site to explore the chilling art of Ice Shards and claim your rightful place among the most esteemed sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Ice Shards Build"])
                
            #Firewall
                elif re.findall("conjuring|infernal|flames|engulf", sorc_build.lower()):

                    print ("\nCongratulations, mighty sorceress, on your unwavering dedication to the mystical arts!\nYour choice to embrace the scorching power of the Firewall build is a testament to your fiery spirit and insatiable hunger for destruction.")
                    print ("May your path be forged in the crucible of flames, and may your enemies tremble in the face of your unrelenting power.\nHere's a site to immerse yourself in the scorching art of the Firewall build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Firewall Build"])
                
            #Arc Lash
                elif re.findall("crackling|energy|wrath|lightning", sorc_build.lower()): 
                
                    print ("\nCongratulations, esteemed sorceress, on your unwavering dedication to the arcane arts!\nYour choice to embrace the electrifying power of the Arc Lash build is a testament to your mastery over the forces of lightning and your thirst for unparalleled devastation.")
                    print ("May your path be illuminated by the electrifying brilliance of Arc Lash, and may your enemies tremble in the face of your overwhelming might.\nHere's a site to immerse yourself in the electrifying art of the Arc Lash build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Arc Lash Build"])
                
            #Meteor
                elif re.findall("harnessing|cataclysmic|might|celestial|fire|heavens", sorc_build.lower()): 
                
                    print ("\nCongratulations, illustrious sorceress, on your unwavering devotion to the arcane arts!\nYour choice to harness the cataclysmic might of the Meteor build is a testament to your command over celestial forces and your insatiable thirst for destruction.")
                    print ("May your path be illuminated by the celestial brilliance of Meteor, and may your enemies quiver in the face of your unrelenting power.\nHere's a site to delve into the cataclysmic art of the Meteor build and claim your rightful place among the most revered sorceresses.\n") 
                    webbrowser.open(Classes["Sorceress"]["Meteor Build"])
                player_amount = player_amount - 1
                player_amount_list.remove(player_amount_list[0])
                Classes.pop('Sorceress')
        
            
            



#Closing Statement
print("\nMay your chosen path through the realm of Sanctuary be adorned with triumphant victories and abundant treasures, as you navigate treacherous battles and fierce encounters that shape the very fabric of your destiny.\nLet the echoes of battles won and the spoils of conquest propel you forward, for in this vast and perilous realm, true heroes emerge and legends are forged.\n")
#Helpful links
print ("\nSome other help links are: \nMaxroll https://d4.maxroll.gg/\nInteractive Map https://mapgenie.io/diablo-4/maps/sanctuary\nBuild Planner https://d4builds.gg/skill-trees/")
webbrowser.open("https://mapgenie.io/diablo-4/maps/sanctuary/")
