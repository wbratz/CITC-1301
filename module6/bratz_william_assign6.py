print("How many days did you collect gems?")

days_collected = int(input())
total_gems = 0
day_number = 1

while(day_number <= days_collected):
    print("Enter the number of gems collected on day:", day_number)
    total_gems += int(input())
    day_number += 1

print("Total gems collected:", total_gems)
print("Average gems collected per day:", total_gems / days_collected)

## not sure on this assignment if you wanted to see it terminated to two decimal places (like in the sample output)
## or if you wanted just the full average, the instructions didn't explicitly say, so I did it both ways 
## I went with the the above actually running because it offered the greatest amount of precision

## below is a couple ways to do it just based on how you wanted the output

## Rounding up which is technically more accurate then the sample output in the assignment
# print("Average gems collected per day:", round(total_gems / days_collected, 2))

## Matching the sample output exactly
# print("Average gems collected per day:", float(str(total_gems / days_collected)[:4]))






