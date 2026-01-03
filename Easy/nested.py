#three level nesting

score=60
attendance=50
submission=True

if score>=60:
    if attendance>=80:
        if submission:
            print("pass with good standing.")
        else:
            print("pass with missing assignment")
    else:
        print("pass but low attendance")
else:
    ("fail")