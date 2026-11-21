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


print("=======Going down 1 level at a time========")
print(anime["old school"]["HxH"]["Netero"][1])
print(anime["old school"]["HxH"]["Netero"][0])

print()
print("=== 2. Loop Level 1: Categories ===")

for category in anime:
    print(category)

print()
print("=== 3. Loop Levels 1-2: Categories and Titles ===")

for category, titles in anime.items():
    print(category)

    for title in titles:
        print(" -", title)
print()
print("=== 4. Loop ALL Levels ===")

for category, titles in anime.items():
    print(category)

    for title, characters in titles.items():
        print("  " + title)

        for name, info in characters.items():
            print("     " + name)
            print("       Description:", info[1])
            print("       Power:", info[0])
print()
print("=== 5. Count Every Character ===")

count = 0

for titles in anime.values():
    for characters in titles.values():
        for name in characters:
            count = count + 1

print("Total characters:", count)
print()
print("=== 6. Search for a Character ===")

search = "Netero"
found = False

for category, titles in anime.items():
    for title, characters in titles.items():

        if search in characters:
            print(search, "is from", title, "(" + category + ")")
            print("Power:", characters[search][0])
            found = True

if found == False:
    print(search, "not found.")
