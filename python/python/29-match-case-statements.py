def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Teusday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _: # any other statements
            return "Invalid"

print(day_of_week(1))
print(day_of_week(7))
print(day_of_week("Monkey"))

def day_of_week(day):
    match day:
        case "Saturday" | "Sunday": # | means or
            return "It is a weekend"
        case "Monday" | "Teusday" | "Wednesday" | "Thursday" | "Friday":
            return "It is a weekday"
        case _:
            return "Invalid"
 
print(day_of_week("Saturday"))
print(day_of_week(input("What day is it today: ")))
print(day_of_week("Monkey"))
