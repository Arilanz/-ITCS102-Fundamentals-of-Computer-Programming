#DBZ
majinbuu= ["Renegeration"]
goku= ["Ki"]
Master_pogi=["Charisma"]
trunks=["Swordsmanship"]
#NARUTO
sasuke=["Sharingan"]
kakashi=["Copy Ninja"]
hashirama=["God of Shinobi"]
minato=["Speed"]
#HxH
netero=["Bodhisattva"]
gon=["Enhancement"]
killua=["Lightning"]
mereum=["Synthesis"]

#demonslayer
tanjiro=["Sun breathing"]
zenitsu=["Lightning breathing"]
nezuko=["Exploding Blood"]
inosuke=["Beast breathing"]
#jjk
gojo=["Limitless cursed technique"]
yuji=["superhuman physical abilities"]
megumi=["Ten Shadows Technique"]
nanami=["Innate Technique: Ratio Technique (7:3)"]

#solo leveling
sung_jin_woo=["Shadow"]
cha_hae_in=["Swordsmanship"]
thomas=["Strength"]
Go_Gun_hee=["Telekinesis"]

#tower of god
jin_mori=["Omnipotence"]
Han_Daewi=["Physics"]
Yu_mira=["Swordsmanship"]
park=["Traitor"]

#old
dragonball=[trunks,majinbuu,goku,Master_pogi,]
naruto=[sasuke,kakashi,hashirama,minato,]
hxh=[netero,gon,killua,mereum,]

#new
demonslayer=[tanjiro,zenitsu,nezuko,inosuke,]
jjk=[gojo,yuji,megumi,nanami,]

#korea
solo_leveling=[sung_jin_woo,cha_hae_in,thomas,Go_Gun_hee,]
god_highschool=[jin_mori,Han_Daewi,thomas,Go_Gun_hee]

luma=[dragonball,naruto,hxh,]
bago=[demonslayer,jjk,]
korean=[solo_leveling,god_highschool,]

anime={"old school":luma , "new anime":bago , "over rated": korean}

print(anime["new anime"][1][1])
print(anime["new anime"][1])
print(anime["old school"][2][3])
