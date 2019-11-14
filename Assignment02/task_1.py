def Mark_sheet():
    sub_1 = float(input("Enter obtained marks of 1st Subject: "))
    sub_2 = float(input("Enter obtained marks of 2nd Subject: "))
    sub_3 = float(input("Enter obtained marks of 3rd Subject: "))
    sub_4 = float(input("Enter obtained marks of 4th Subject: "))
    sub_5 = float(input("Enter obtained marks of 5th Subject: "))

    total_marks = sub_1+sub_2+sub_3+sub_4+sub_5

    print("==========================================================")
    print("Subjects     Obtained Marks      Out of Marks        Grade")
    print("==========================================================")

    Sub_Grade("01",sub_1)
    Sub_Grade("02",sub_2)
    Sub_Grade("03",sub_3)
    Sub_Grade("04",sub_4)
    Sub_Grade("05",sub_5)
    Total_Grade("TOTAL",total_marks)

    print("==========================================================")

def Sub_Grade(a,b):
    if b >= 80:
        print("{}               {}                  100               A+".format(a,b))    

    elif 70 <= b < 80:
        print("{}               {}                  100               A".format(a,b))    

    elif 50 <= b < 70:
        print("{}               {}                  100               B".format(a,b))    
        
    elif b < 50:
        print("{}               {}                  100               FAIL".format(a,b))    
    
def Total_Grade(a,b):
    if b >= 400:
        print("{}            {}                 500               A+".format(a,b))    

    elif 350 <= b < 400:
        print("{}            {}                 500               A".format(a,b))    

    elif 250 <= b < 350:
        print("{}            {}                 500               B".format(a,b))    
        
    elif b < 250:
        print("{}            {}                 500               FAIL".format(a,b))    

Mark_sheet()