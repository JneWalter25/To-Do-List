from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
import datetime

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='nothing_to_do')
    date = Column(Date, default=datetime.datetime.today())
    deadline = Column(Date, default=datetime.datetime.today)


class Database1:
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


class Menu(Database1, Table):
    def mes(mes2):

        d = datetime.datetime.now()
        mes = d.strftime("%m")
        intmes = int(mes)
        formula = mes2 - intmes
        intmes = intmes + formula
        if intmes == 1:
            return "Jan"
        elif intmes == 2:
            return "Feb"
        elif intmes == 3:
            return "Mar"
        elif intmes == 4:
            return "Apr"
        elif intmes == 5:
            return "May"
        elif intmes == 6:
            return "Jun"
        elif intmes == 7:
            return "Jul"
        elif intmes == 8:
            return "Aug"
        elif intmes == 9:
            return "Sep"
        elif intmes == 10:
            return "Oct"
        elif intmes == 11:
            return "Nov"
        elif intmes == 12:
            return "Dec"

    while True:
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Missed tasks")
        print("5) Add task")
        print("6) Delete task")
        print("0) Exit")
        d = datetime.datetime.now()
        day = d.strftime("%d")
        elec = int(input())
        if elec == 1:
            today = datetime.datetime.today()
            rows = Database1.session.query(Table).all()
            m = today.strftime('%b')
            print("Today", m, day, ":")
            j = 0
            for row in rows:
                row2 = rows[j]
                print(row2.task)
                print("")
                j += 1
            if j == 0:
                print("Nothing to do!")
                print("")

        elif elec == 2:
            today = datetime.datetime.today()
            pensar = False
            otromes = False
            for i in range(7):
                day = today + timedelta(days=i)
                rows = Database1.session.query(Table).filter(Table.deadline == day.date()).all()
                if rows:
                    for i in rows:
                        days = day.strftime('%A')
                        daysn = day.strftime('%d')
                        mes3 = i.deadline.strftime("%m")
                        mes3 = int(mes3)
                        print(days, daysn, mes(mes3))
                        print(i.task)
                        print("")
                else:
                    days = day.strftime('%A')
                    daysn = day.strftime('%d')
                    # mes3 = j.deadline.strftime("%m")
                    # mes3 = int(mes3)
                    d = datetime.datetime.now()
                    mes1 = d.strftime("%m")
                    mes2 = int(mes1)
                    daysn = str(daysn)
                    x = mes(mes2)
                    if otromes == True:
                        mes2 = mes2 + 1
                    if pensar == True:
                        mes2 = mes2 + 1
                        otromes = True
                    else:
                        otromes = False
                    
                    if x == "Jan" or x == "Mar" or x == "May" or x == "Jul" or x == "Aug" or x == "Oct" or x == "Dec":
                        daysn = int(daysn)
                        if daysn == 31:
                            pensar = True
                        else:
                            pensar = False
                    elif x == "Apr" or x == "Jun" or x == "Sep" or x == "Nov":
                        daysn = int(daysn)
                        if daysn == 30:
                            pensar = True
                        else:
                            pensar = False
                    elif x == "Feb":
                        daysn = int(daysn)
                        if daysn == 28:
                            pensar = True
                        else:
                            pensar = False
                    print(mes2)
                    print(days, daysn, mes(mes2))
                    print('Nothing to do!')
                    print("")

        elif elec == 3:
            rows = Database1.session.query(Table).order_by(Table.deadline).all()
            for i in rows:
                x = i.deadline
                day = i.deadline.strftime("%d")
                day = int(day)
                day = str(day)
                mes3 = i.deadline.strftime("%m")
                mes3 = int(mes3)
                print(i.task + ". " + day + " " + mes(mes3))
                print("")

        elif elec == 4:
            today = datetime.datetime.today()
            rows = Database1.session.query(Table).order_by(Table.deadline).filter(Table.deadline < today.date()).all()
            for i in rows:
                x = i.deadline
                day = i.deadline.strftime("%d")
                mes3 = i.deadline.strftime("%m")
                mes3 = int(mes3)
                print(i.task + ". " + day + " " + mes(mes3))
                print("")


        elif elec == 5:
            print("Enter task")
            taskin = input()
            print("Enter deadline")
            deadlinein = input()
            xs = deadlinein.replace("-", " ")
            deadlist = xs.split()
            year = int(deadlist[0])
            month = int(deadlist[1])
            day = int(deadlist[2])
            deaddate = datetime.datetime(year, month, day)
            new_row = Table(task=taskin,
                            date=datetime.datetime.today().date(),
                            deadline=deaddate)
            Database1.session.add(new_row)
            Database1.session.commit()
            rows = Database1.session.query(Table).all()
            first_row = rows[0]  # In case rows list is not empty
            print("The task has been added!")
            print("")

        elif elec == 6:
            print("Choose the number of the task you want to delete:")
            rows = Database1.session.query(Table).order_by(Table.deadline).all()
            if rows:
                for i in rows:
                    x = i.deadline
                    day = i.deadline.strftime("%d")
                    mes3 = i.deadline.strftime("%m")
                    mes3 = int(mes3)
                    y = i.id
                    y = str(y)
                    print(y + ". " + i.task + ". " + day + " " + mes(mes3))
                    y = int(y)
                delete = int(input())
                Database1.session.query(Table).filter(Table.id == delete).delete()
                Database1.session.commit()
                print("The task has been deleted!")
                print("")

            else:
                print("Nothing is missed!")
                print("")

        elif elec == 0:
            break


Table
Database1
Menu