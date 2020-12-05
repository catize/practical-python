# Sears
bill_thickness = 0.11 * 0.001 #Meters
sears_hight = 442 #Hight in meters
number_bills = 1
day = 1


while bill_thickness * number_bills < sears_hight:
    print(day, number_bills, bill_thickness * number_bills)
    day = day + 1
    number_bills = number_bills * 2

print('Number of Days:', day )
print('Number of Bills:', number_bills)
print('Final Height:', bill_thickness * number_bills)

