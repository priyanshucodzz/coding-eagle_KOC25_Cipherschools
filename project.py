print("enter the time in 24 hour format please")
hour=int(input("hour--> "))
minutes=int(input("minutes-->"))
diff=0
hour_real=0
min_real=0
min_notreal=0
if(hour<=12):
    hour_real=hour
elif(hour>12):
    hour_real=(hour-12)
if(minutes==0):
    min_real=12
else:
    min_notreal=minutes%5
    min_real=minutes/5
if(hour_real>=min_real):
    diff=hour_real-min_real
elif(min_real>hour_real):
    diff=min_real-hour_real
ans=int((diff*30)+(min_notreal*6))
if(ans>180):
    ans=360-ans

print("the shortest angle between the minutes and the hour hand-->")
print(str(ans)+"  degrees")