#Saqif Abedin (with Maddy Andersen and Ian Chen Adamczyk)
#SoftDev
#K05 -- Teamwork, but Better This Time/Team Name is User input, Output is random name from said team
#2020-09-30

import random

KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDY', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

teamName = str(input("Choose a team from orpheus, rex, or endymion: ")).lower()
while teamName not in KREWES:
    teamName = input("Please enter either orpheus, rex, or endymion: ").lower()


print(random.choice(KREWES[teamName]))