time = input("What time is it?: ")
time = time.split(":")
h = int(time[0])
m = int(time[1])


def timeInWords(h, m):

    timeMin =  { 1 :"one", 2 : "two", 3 : "three", 4: "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine",
            10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 
            17 : "seventeen", 18 : "eighteen", 19 : "nineteen", 20 : "twenty", 21 : "twenty one", 22 : "twenty two",
            23 : "twenty three", 24 : "twenty four", 25 : "twenty five", 26 : "twenty six", 27 : "twenty seven",
            28 : "twenty eight", 29 :  "twenty nine"}

    timeHour = { 1 : "one", 13 : "one", 2 : "two", 14 : "two", 3 : "three", 15 : "three", 4 : "four", 16 : "four",
                 5 : "five", 17 : "five", 6 : "six", 18 : "six", 7 : "seven", 19 : "seven", 8 : "eight", 20 : "eight",
                 9 : "nine", 21 : "nine", 10 : "ten", 22 : "ten", 11 : "eleven", 23 : "eleven" , 12 : "twelve", 0 : "twelve"}
            
    if(m == 0):
        return f"{timeHour[h]} o'clock"
    elif(m == 1):
        return f"one minute past {timeHour[h]}"
    elif(m == 59):
        if(h == 23):
            h = 12
            return f"one minute to {timeHour[h]}"
        else:
            return f"one minute to {timeHour[h+1]}"
    elif(m == 15):
        return f"quarter past {timeHour[h]}"
    elif(m == 30):
        return f"half past {timeHour[h]}"
    elif(m == 45):
        return f"quarter to {timeHour[h+1]}"
    elif(m <= 30):
        return f"{timeMin[m]} minutes past {timeHour[h]} "
    elif(m > 30):
        if(h == 23):
            h = 12
            return f"{timeMin[60-m]} minute to {timeHour[h]}"
        else:
            return f"{timeMin[60-m]} minutes to {timeHour[h+1]}"
     
        
if( h > 0 and h < 24 ):
    if( m >=0 and m < 60 ):
        print(timeInWords(h, m))
    else:
        print("The minute value must be between 0 and 59.")
        time = input("Enter the value again")
        time = time.split(":")
        h = int(time[0])
        m = int(time[1])            
else:
    print("The hour value must be between 1 and 23.")
    time = input("Enter the value again: ")   
    time = time.split(":")
    h = int(time[0])
    m = int(time[1]) 
    print(timeInWords(h, m))



