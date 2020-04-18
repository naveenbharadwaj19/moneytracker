import json
import datetime
from datetime import date
import os
from time import sleep

class Json_file():
    dd_mm_yyyy = date.today()
    def __init__(self):
        self.date = self.dd_mm_yyyy.strftime("%d/%m/%Y")
        self.month = self.dd_mm_yyyy.strftime("%B")
        self.reason = input("Enter the reason for spending: ")
        self.amt_spent = int(input("Enter the amount spent: "))

    def initialize(self):
        try:
            with open("trackmoney.json",'r') as read_json:
                main_data = []
                data = json.load(read_json)
                for i in data:
                    main_data.append(i)
                for i in self.write_json():
                    get_data = i
                    main_data.append(get_data)
            with open("trackmoney.json",'w') as write_file:
                json.dump(main_data,write_file,indent=4)
        except Exception:
            print("No Data so making one!")
            return self.first_time_Serialize()
    
    def write_json(self):
        money = [{
            "Date": self.date,
            "Month": self.month,
            "Reason": self.reason,
            "Amount Spent": self.amt_spent,
            "Total amt Spent": "Amt spent until now %d"%self.get_amt_spent()
        }]
        return money

    def first_time_Serialize(self):
        money = [{
            "Date": self.date,
            "Month": self.month,
            "Reason": self.reason,
            "Amount Spent": self.amt_spent,
            "Total amt Spent": "Amt spent until now %d"%self.amt_spent
        }]
        with open("trackmoney.json",'w') as write_file:
            json.dump(money,write_file,indent=4)

    def get_amt_spent(self):
        with open("trackmoney.json") as read_file:
            data = json.load(read_file)
            fetch_json = []
            track_amt_spent = []
            fetch_json.append(data)
            for i in fetch_json[0]:
                track_amt_spent.append(i["Amount Spent"])
        total_amt_spent = sum(track_amt_spent)
        return total_amt_spent + self.amt_spent



track_loop = True
while track_loop:
    try:
        json_file = Json_file()
        json_file.initialize()
    except EOFError:
        track_loop = False
        print("Stopped")


today = str(date.today().strftime("%d"))

choice = int(input("""
Press 1 --- convert json to pdf in month end and will reset the json script
Press 2 --- convert json to pdf now
Press 3 --- Exit the process \n:"""))

if choice == 1:
    if today == "30" or today == "31":
        from pdf import json_pdf
        json_pdf()
        sleep(2)
        os.remove('path/trackmoney.json')
        print("Removed trackmoney json file")
    else:
        print("Date did match press 1 either on 30 or 31")
elif choice == 2:
    from pdf import json_pdf
    json_pdf()
    sleep(2)
    print("Completed")

elif choice == 3:
    print("*"*60)

