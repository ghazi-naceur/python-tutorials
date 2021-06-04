if __name__ == '__main__':
    import datetime
    new_time = datetime.time(15,20,50,20)
    print(new_time)
    print(new_time.hour)
    print(new_time.minute)
    print(new_time.second)
    print(new_time.microsecond)

    new_date = datetime.date.today()
    print(new_date)
    print(new_date.year)
    print(new_date.month)
    print(new_date.day)
    print(new_date.ctime())

    from datetime import datetime

    new_datetime = datetime(2020, 5, 20, 12, 50, 2, 30)
    print(new_datetime)
    print(new_datetime.ctime())

    new_datetime = new_datetime.replace(year=2021)
    print(new_datetime)
    print(new_datetime.ctime())

    from datetime import date
    date1 = date(2021,6,1)
    date2 = date(2020,6,1)

    delta = date1 - date2
    print(delta)
    print(type(delta))
    print(delta.days)

    datetime1 = datetime(2020, 5, 20, 12, 50, 2, 30)
    datetime2 = datetime(2020, 5, 20, 10, 50, 20, 30)

    result = datetime1 - datetime2
    print(result)
    print(type(result))
    print(result.seconds)
    print(result.total_seconds())