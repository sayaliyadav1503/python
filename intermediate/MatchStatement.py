day=4
match day:
    case 1:
        print("monday")
    case 2 :
        print("tuesday")
    case 3:
          print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

#combine value
day = 4
match day:
    case 1|2|3|4|5:
        print("today is a weekday")
    case 6|7:
        print("i love weekends...")

#if statement as guards

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")