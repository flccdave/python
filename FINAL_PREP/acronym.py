# ACRONYM TESTER

# CIA
# Central Intelligence Agency #true

# NSA
# National Security Investigators #false

# FBI
# Federal Investigators #false

# CIA
# Central Intelligence Agency
# ['Central', 'Intelligence', 'Agency' ]

# word = input("Enter the acronym: ")
# words = input("Proposed words: ")

word = 'cia'
words = 'Central Intelligence agency'

acronym = words.split() #'e'

isAcronym = True

if len(word) != len(acronym):
    isAcronym = False
else:
    for x in range(len(word)):
        if word[x].upper() != acronym[x][0].upper():
            isAcronym = False

if isAcronym == True:
    print("This is a valid acronym")
else:
    print("This is NOT a valid acronym")

# print(word)
# print(words)
# print(acronym)







