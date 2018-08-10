


marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

print (line.find (marker))
position = line.find (marker)
first_part = line[0:position]
second_part = line[len(marker)+position:]
print (first_part + replacement + second_part)

