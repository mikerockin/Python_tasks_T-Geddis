tuition = 6000
percentage = .02

#Declare Original tuition
print('The tuition for full time student per semester = ${}'.format(tuition))
print

#Projected tuition for 5 years
for year in range(1,6):
	yearlyIncrease = tuition + (tuition * percentage)
	print ('Year {} '.format(year)
	print ('Projected annual tuition increase per semester = ${:,.2f}'.format(yearlyIncrease))
	tuition += tuition * percentage