#DBZ
majinbuu= ["Powers: Renegeration", "Description: An ancient, pink, magical genie-like villain"]
goku= ["Powers: Ki", "Description:A cheerful, pure-hearted Saiyan martial artist"]
master_pogi=["Powers: Charisma" , "Description: A flamboyant, cowardly yet surprisingly loyal"]
trunks=["Powers: Swordsmanship", "Description: A brave, sword-wielding time traveler from an apocalyptic future"]
#NARUTO
sasuke=["Powers: Sharingan", "Description: abandons his village in pursuit of power before ultimately being redeemed by his lifelong bond with his best friend "]
kakashi=["Powers: Copy Ninja","Description: mentors Team 7 and later becomes the Sixth Hokage"]
hashirama=["Powers: God of Shinobi","Description: wielding unmatched Wood Release kekkei genkai and Sage Mode to unite the warring shinobi clans."]
minato=["Powers: Speed" ,"Description: brilliant and compassionate Fourth Hokage who sacrificed his life to seal the Nine-Tails inside his newborn son"]
#HxH
netero=["Powers: Bodhisattva" ,"Description: eccentric, battle-hungry 12th Chairman of the Hunter Association in Hunter x Hunter"]
gon=["Powers: Enhancement","Description: is a cheerful, fiercely determined, yet morally complex young boy who becomes an elite Hunter to track down his absentee father, "]
killua=["Powers: Lightning" ,"Description: fiercely loyal, lightning-powered boy from an infamous assassin family "]
mereum=["Powers: Synthesis","Description: ruthless, god-like King of the Chimera Ants and the main antagonist of Hunter x Hunter's Chimera Ant arc"]

#demonslayer
tanjiro=["Powers: Sun breathing" ,"Description: kindhearted and determined protagonist of Demon Slayer: Kimetsu no Yaiba"]
zenitsu=["Powers: Lightning breathing","Description: is a cowardly yet loyal Demon Slayer who hides an extraordinary mastery of lightning-fast Thunder Breathing swordsmanship"]
nezuko=["Powers: Exploding Blood","Description: is the kindhearted younger sister of Tanjiro in Demon Slayer: Kimetsu no Yaiba"]
inosuke=["Powers: Beast breathing"," Description: is a brash, muscular Demon Slayer who wears a hollowed-out boar's head mask"]
#jjk
gojo=["Powers: Limitless cursed technique","Description:  playful, arrogant yet deeply caring special-grade jujutsu sorcerer and teacher at Tokyo Jujutsu High in Jujutsu Kaisen"]
yuji=["Powers: superhuman physical abilities","Description: a kind-hearted teenager with superhuman strength who becomes a jujutsu sorcerer to fight curses and save people"]
megumi=["Powers: Ten Shadows Technique","Description: a stoic, fiercely loyal, and morally driven young jujutsu sorcerer"]
nanami=["Powers: Innate Technique: Ratio Technique (7:3)","Description: pragmatic, stoic Grade 1 jujutsu sorcerer and former corporate salaryman in Jujutsu Kaisen"]

#solo leveling
sung_jin_woo=["Powers: Shadow","Description: main protagonist of Solo Leveling, who rises from the weakest E-rank hunter to become the world's strongest hunter and the Shadow Monarch with a shadow army"]
cha_hae_in=["Powers: Swordsmanship","Description: renowned as The Dancer for her graceful, high-speed swordsmanship and unique ability to smell mana."]
thomas=["Powers: Strength","Description: towering, prideful National Level S-Rank hunter and Scavenger Guild master from the United States"]
go_gun_hee=["Powers: Telekinesis","Description: is the elderly S-Rank Chairman of the Korean Hunters Association in Solo Leveling "]

#tower of god
jin_mori=["Powers: Omnipotence","Description: is a carefree martial arts prodigy who evolves from a seemingly low-level Taekwondo fighter into the all-powerful Supreme God Maitreya."]
han_daewi=["Powers: Physics","Description: is a fiercely loyal, sleepy-eyed Full-Contact Karate prodigy from The God of High School "]
yu_mira=["Powers: Swordsmanship","Description: is a fiercely determined 17-year-old swordswoman and the 25th master of the Moon Light Sword Style"]
park=["Powers: Traitor","Description: is the ruthless, calculating founder of the God of High School tournament who rises from a corrupt politician to become the World President "]

#old
dragonball={"Trunks":trunks,"Majinbuu": majinbuu,"Goku":goku,"Master_pogi":master_pogi,}
naruto={"Sasuke":sasuke,"Kakashi":kakashi,"Hashirama":hashirama,"Minato": minato,}
hxh={"Netero":netero,"Gon":gon,"Killua":killua,"Mereum":mereum,}

#new
demonslayer={"Tanjiro":tanjiro,"Zenitsu":zenitsu,"Nezuko":nezuko,"Inosuke":inosuke,}
jjk={"Gojo":gojo,"Yuji":yuji,"Megumi":megumi,"Nanami":nanami,}

#korea
solo_leveling={"Sung jin woo":sung_jin_woo,"Cha hae in":cha_hae_in,"Thomas": thomas,"Go gun hee": go_gun_hee,}
god_highschool={"Jin mori":jin_mori,"Han daewi": han_daewi,"Yu mira": yu_mira,"Park":park}

luma={"DBZ":dragonball,"Naruto":naruto,"HxH": hxh,}
bago={"Demon slayer":demonslayer,"JJK":jjk,}
korean={"Solo Leveling":solo_leveling,"God Highschool":god_highschool,}



anime={"old school":luma , "new anime":bago , "over rated": korean}

# ===== FUNCTIONS =====

def choose(dictionary, label, allow_new=False):

    options = []

    for key in dictionary:
        options.append(key)

    if allow_new:
        print("0 - New", label)

    for i in range(len(options)):
        print(i + 1, "-", options[i])

    while True:

        try:
            number = int(input("Enter " + label + " number: "))

        except ValueError:
            print("Numbers only.")
            continue

        if allow_new and number == 0:
            new_key = input("Enter new " + label + ": ")
            dictionary[new_key] = {}
            return new_key

        if number >= 1 and number <= len(options):
            return options[number - 1]

        print("Invalid number. Try again.")


def show_character(name, info):

    print("   ", name)
    print("      Power:", info[0])
    print("      Description:", info[1])


def visit_anime():

    print("\nSELECT CATEGORY")
    category = choose(anime, "category")

    print("\nSELECT ANIME IN", category)
    title = choose(anime[category], "anime")

    characters = anime[category][title]

    print("\nWELCOME TO", title)
    print("CHARACTERS:")

    for name in characters:
        print("*", name)

    print("\nWHO DO YOU WANT TO MEET?")
    name = choose(characters, "character")

    show_character(name, characters[name])


def show_all():

    for category, titles in anime.items():

        print("\nCATEGORY:", category)

        for title, characters in titles.items():

            print("  ANIME:", title)

            for name, info in characters.items():

                show_character(name, info)


def count_characters():

    count = 0

    for titles in anime.values():

        for characters in titles.values():

            count = count + len(characters)

    return count


def search_character(search):

    found = False

    for category, titles in anime.items():

        for title, characters in titles.items():

            if search in characters:

                print("\n", search, "is from", title,
                      "(" + category + ")")

                show_character(search, characters[search])

                found = True

    if found == False:
        print(search, "not found.")


def add_character():

    print("\nWHERE DOES THE CHARACTER BELONG?")

    category = choose(anime, "category", allow_new=True)

    print("\nSELECT ANIME IN", category)

    title = choose(anime[category], "anime", allow_new=True)

    name = input("Enter character name: ")
    power = input("Enter character power: ")
    description = input("Enter character description: ")

    anime[category][title][name] = [power, description]

    print("\n", name, "successfully added!")
    print("Category:", category)
    print("Anime:", title)


# ===== MAIN PROGRAM =====

while True:

    print("\n======= ANIME DATABASE =======")
    print("1 - Visit an Anime")
    print("2 - Show Everything")
    print("3 - Search a Character")
    print("4 - Add a Character")
    print("5 - Count Characters")
    print("6 - Exit")

    choice = input("Enter your choice ---> ")

    if choice == "1":

        visit_anime()

    elif choice == "2":

        show_all()

    elif choice == "3":

        name = input("Enter character name: ")
        search_character(name)

    elif choice == "4":

        add_character()

    elif choice == "5":

        print("Total characters:", count_characters())

    elif choice == "6":

        print("SYSTEM EXIT")
        break

    else:

        print("INVALID CHOICE")
