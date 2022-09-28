import application.salary
import application.db.people
from datetime import datetime


def timenow():
    nowdate = datetime.now()
    print(nowdate)


if __name__ == '__main__':
    timenow()