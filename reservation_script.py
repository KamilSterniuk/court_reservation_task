import datetime
import json
import csv

reservations = []

def make_reservation():

    name = input("What's your Name? ")

    while True:
        date = input("When would you like to book? (DD.MM.YYYY HH:MM) ")

        try:
            dt = datetime.datetime.strptime(date, "%d.%m.%Y %H:%M")
            break

        except ValueError:
            print("Invalid date format!")

    hours = [30, 60, 90]
    duration = int(input("How long would you like to book court?\n1) 30 Minutes\n2) 60 Minutes\n3) 90 Minutes\nYour choice:  "))

    while duration not in hours:
        print("Invalid duration. Choose 30, 60 or 90 minutes.")
        duration = int(input("How long would you like to book court?\n1) 30 Minutes\n2) 60 Minutes\n3) 90 Minutes\nYour choice:  "))
        
    now = datetime.datetime.now()
    if dt < now + datetime.timedelta(hours=1):
        print("\nReservation should be made over 1 hour before.")
        return
    
    weekly_reservations = 0
    for reservation in reservations:
        if reservation["name"] == name and reservation["date"].isocalendar()[1] == dt.isocalendar()[1]:
            weekly_reservations += 1
    if weekly_reservations >= 2:
        print("You can only make 2 reservation in one week")
        return
    
    for r in reservations:
        if r["date"] <= dt < r["date"] + datetime.timedelta(minutes=r["duration"]):
            dt = r["date"] + datetime.timedelta(minutes=r["duration"])
            print("The time you chose is unavailable. Next possible hour is: ", dt.strftime("%d.%m.%Y %H:%M"))
            choice = input("Would you like to make a reservation for this hour? (yes/no) ")
            if choice.lower() != "yes":
                return

    reservations.append({"name": name, "date": dt, "duration": duration})
    print("Your reservation has been added succesfully.")

def reservation_canceling():
    name = input("What's your Name? ")

    while True:
        date = input("Enter the date and time of the reservation to be canceled (DD.MM.YYYY HH:MM): ")
        try:
            dt = datetime.datetime.strptime(date, "%d.%m.%Y %H:%M")
            break

        except ValueError:
            print("Invalid date format!")

    now = datetime.datetime.now()
    if dt < now + datetime.timedelta(hours=1):
        print("You can't cancel your reservation for less than 1 hour from now.")
        return

    found = False

    for r in reservations:
        if r["name"] == name and r["date"] == dt:
            found = True
            reservations.remove(r)
            print("The reservation has been canceled.")
            break

    if not found:
        print("Reservation for this name and date not found.")

def print_schedule():

    begining = input("Enter a start date (DD.MM.YYYY): ")
    end = input("Enter an end date (DD.MM.YYYY): ")
    
    if not reservations:
        print("No reservations!")
        return
    
    try:
        db = datetime.datetime.strptime(begining, "%d.%m.%Y")
        de = datetime.datetime.strptime(end, "%d.%m.%Y")

    except ValueError:
        print("Invalid date format!")
        return
        
    print("\nReservations schedule:\n")

    reservation_amount = 0
    for r in sorted(reservations, key=lambda x: x["date"]):
        if db <= r["date"] <= de:
            reservation_amount += 1
            print(r["date"].strftime("%A %d.%m.%Y %H:%M"), f"\n{r['name']}", f"{r['duration']} minutes\n")
    if reservation_amount == 0:
        print("No reservation for the dates you chose.")
def save_csv(start_date, end_date):

    filename = input("Enter the name of the file to save (without extension): ")

    with open(f"{filename}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Date", "Hour", "Duration"])

        for r in reservations:
            if start_date <= r["date"] <= end_date:
                writer.writerow([r["name"], r["date"].strftime("%d.%m.%Y"),
                                 r["date"].strftime("%H:%M"), r["duration"]])

def save_json(start_date, end_date):

    schedule = []
    for r in sorted(reservations, key=lambda x: x["date"]):
        if start_date <= r["date"] <= end_date + datetime.timedelta(days=1):
            schedule.append(r)
    
    filename = input("Enter the name of the file to save (without extension): ")           
    with open(filename + ".json", "w") as f:
        json.dump([{"name": r["name"], "date": r["date"].strftime("%d.%m.%Y %H:%M"), "duration" : f"{r['duration']} minut"} for r in schedule], f)
    
while True:
    print("\nMenu:")
    print("1. Make a reservation")
    print("2. Cancel a reservation")
    print("3. Print schedule")
    print("4. Save schedule to a file")
    print("5. Exit")

    choice = int(input("Choose the option: "))

    if choice == 1:
        make_reservation()

    elif choice == 2:
        reservation_canceling()

    elif choice == 3:
        print_schedule()

    elif choice == 4:
        begining_str = input("Enter the start date for the booking interval to be saved (DD.MM.YYYY): ")
        end_str = input("Enter the end date for the slot to book to save (DD.MM.YYYY): ")

        try:
            begining = datetime.datetime.strptime(begining_str, "%d.%m.%Y")
            end = datetime.datetime.strptime(end_str, "%d.%m.%Y")

        except ValueError:
            print("Invalid date format!")
            continue

        while True:
            file_format = input("Choose a file format (csv/json): ")

            if file_format.lower() == "csv":
                save_csv(begining, end)
                break

            elif file_format.lower() == "json":
                save_json(begining, end)
                break

            else:
                print("Invalid file format!")

    elif choice == 5:
        break

    else:
        print("Invalid selection. Try again.")