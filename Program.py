year=0
day=0
date=0
month=0
date=int(input("Enter The date:"))
month=int(input("Enter The Month:"))
year=int(input("Enter The Year:"))
print("The Date:{}-{}-{}".format(date,month,year))
year=year-1
if year<=399:
    a=year-0
elif year>=400 and year<=799:
    a=year-400
elif year>=800 and year<=1199:
    a=year-800
elif year>=1200 and year<=1599:
    a=year-1200
elif year>=1600 and year<=1999:
    a=year-1600
elif year>=2000 and year<=2399:
    a=year-2000
elif year>=2400 and year<=2799:
    a=year-2400
elif year>=2800 and year<=3199:
    a=year-2800
elif year>=3200 and year<=3599:
    a=year-3200
elif year>=3600 and year<=3999:
    a=year-3600
if a<=99:
    a=a-0
    odd=0
elif a<=199:
    a=a-100
    odd=5
elif a<=299:
    a=a-200
    odd=3
elif a<=399:
    a=a-300
    odd=1
b=int(a/4)
c=a-b
d=int(((c*1)+(b*2))%7)
if year%4!=0 or year%400!=0:
    if month==1:
        e=0
    elif month==2:
        e=3
    elif month==3:
        e=3
    elif month==4:
        e=6
    elif month==5:
        e=8
    elif month==6:
        e=11
    elif month==7:
        e=13
    elif month==8:
        e=16
    elif month==9:
        e=19
    elif month==10:
        e=21
    elif month==11:
        e=24
    elif month==12:
        e=26
else:
    if month==1:
        e=0
    elif month==2:
        e=3
    elif month==3:
        e=4
    elif month==4:
        e=7
    elif month==5:
        e=9
    elif month==6:
        e=12
    elif month==7:
        e=14
    elif month==8:
        e=17
    elif month==9:
        e=20
    elif month==10:
        e=22
    elif month==11:
        e=25
    elif month==12:
        e=27
date=date%7
count=int((e+date+odd+d)%7)
if count==1:
    day="Monday"
elif count==2:
    day="Tuesday"
elif count==3:
    day="Wednesday"
elif count==4:
    day="Thursday"
elif count==5:
    day="Friday"
elif count==6:
    day="Saturday"
elif count==0 or 7:
    day="Sunday"
print("{}".format(day))
    

    







    



