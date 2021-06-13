print("How many days did you collect gems?")

days_collected = int(input())
total_gems = 0
day_number = 1

while day_number <= days_collected:
    print("Enter the number of gems collected on day:", day_number)
    total_gems += int(input())
    day_number += 1

print("Total gems collected:", total_gems)

print("Average gems collected per day:", round(total_gems / days_collected, 2))