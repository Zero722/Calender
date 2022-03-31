WEEK = ('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')
MONTHS =	{
    "JANUARY": 31,
    "FEBRUARY": 28,
    "MARCH": 31,
    "APRIL": 30,
    "MAY": 31,
    "JUNE": 30,
    "JULY": 31,
    "AUGUST": 31,
    "SEPTEMBER": 30,
    "OCTOBER": 31,
    "NOVEMBER": 30,
    "DECEMBER": 31,    
}


def calculate_gap(year):
# Formula might be wrong
    y = year - 1
    gap1 = 1
    gap = (gap1 + y*365 + int(y/4) - int(y/100) + int(y/400))%7
    return gap

def leap_year(year):

    if year%100 == 0:
        if year%400 == 0:
            MONTHS["FEBRUARY"] = 29
    elif year%4 == 0:
        MONTHS["FEBRUARY"] = 29



def display(year,gap):
    
    
    print("\n\n\t\t\t",year,end='')
    for x in MONTHS:
        print("\n\n")
        print(x,end="\n")

        for y in WEEK:
            print(y,end="\t")
        
        print("\t")
        for g in range(0,gap):
            print("\t",end='')
        for i in range(1,MONTHS[x]+1):
            print(i,end="\t")
            if (gap+i)%7==0:
                print()

        gap = (gap+MONTHS[x])%7


def main():
 
    global WEEK   
    global MONTHS
    
    year = int(input("Enter the year:"))
    gap = calculate_gap(year)
    leap_year(year)
    display(year,gap)
    print("\n")
    input("Press enter to exit")


 

main()
