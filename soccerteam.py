soccerTeam = {}
menuOption = ''

for n in range(1, 6):
    jerseyNumber = int(input('Enter player %d\'s jersey number:\n' % n))
    rating = int(input('Enter player %d\'s rating:\n' % n))
    soccerTeam[jerseyNumber] = rating
    print('')

sortedListOfJerseyNumbers = sorted(list(soccerTeam.keys()))

print('ROSTER')
for x in sortedListOfJerseyNumbers:
    print('Jersey number: %d, Rating: %d' % (x, soccerTeam[k]))

while menuOption != 'q':
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')

    menuOption = input('Choose an option:\n')

    if menuOption == 'o':
        sortedListOfJerseyNumbers = sorted(list(soccerTeam.keys()))
        print('ROSTER')
        for x in sortedListOfJerseyNumbers:
            print('Jersey number: %d, Rating: %d' % (x, soccerTeam[k]))
    elif menuOption == 'a':
        jerseyNumber = int(input('Enter a new player\'s jersey number:\n'))
        rating = int(input('Enter the player\'s rating:\n'))
        soccerTeam[jerseyNumber] = rating
    elif menuOption == 'd':
        jerseyNumber = int(input('Enter a jersey number:\n'))
        del soccerTeam[jerseyNumber]
    elif menuOption == 'u':
        jerseyNumber = int(input('Enter a jersey number:\n'))
        rating = int(input('Enter a new rating for player:\n'))
        soccerTeam[jerseyNumber] = rating
    elif menuOption == 'r':
        rating = int(input('Enter a rating:\n'))
        sortedListOfJerseyNumbers = sorted(list(soccerTeam.keys()))
        print('ABOVE', rating)
        for x in sortedListOfJerseyNumbers:
            if soccerTeam[x] > rating:
                print('Jersey number: %d, Rating: %d' % (x, soccerTeam[k]))