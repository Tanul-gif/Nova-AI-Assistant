from datetime import datetime

def get_current_time():
    now = datetime.now()
    return now.strftime("This time is %I:%M%p")

def get_current_date():
    now = datetime.now()
    return now.strftime("Today is %A, %d %B %Y")

def get_time_greeting():
    hour = datetime.now().hour
    if 5<=hour<12:
        return "Good Morning"
    elif 12<=hour<17:
        return "Good Afternoon"
    elif 17<=hour<21:
        return "Good Evening"
    else:
        return "Its late dont forget to rest"
    

if __name__ == "__main__":
    print(get_time_greeting())
    print(get_current_time())
    print(get_current_date())