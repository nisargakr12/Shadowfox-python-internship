#1. Calculate the number of members.

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

number_of_members = len(justice_league)

print("Number of members in the Justice League:", number_of_members)


#2. Add Batgirl and Nightwing

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

justice_league.extend(["Batgirl", "Nightwing"])

print(justice_league)


#3. Remove Wonder Woman and insert at the beginning

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern", "Batgirl", "Nightwing"]

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print(justice_league)


#4. Separate Aquaman and Flash

justice_league = ["Wonder Woman", "Superman", "Batman", "Flash", "Aquaman", "Green Lantern", "Batgirl", "Nightwing"]

justice_league.remove("Green Lantern")

index_aquaman = justice_league.index("Aquaman")
index_flash = justice_league.index("Flash")

justice_league.insert(index_flash + 1, "Green Lantern")

print(justice_league)


#5. Replace justice_league

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]

print(justice_league)


#6. Sort justice_league

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New leader:", justice_league[0])

