paintColors = {'red':35, 'blue':25, 'green':23}
height = float(input('Enter wall height (feet):\n'))
width = float(input('Enter wall width (feet):\n'))
wall_area = int(height*width)
paint_needed = wall_area/350
cans = round(paint_needed)
print('Wall area: '+str(wall_area),'square feet')
print('Paint needed: %.2f gallons'% paint_needed)
print('Cans needed:', cans, 'can(s)')
color = input('\nChoose a color to paint the wall:')
print('\nCost of purchasing', color, 'paint: $'+str(cans * paintColors[color]))

