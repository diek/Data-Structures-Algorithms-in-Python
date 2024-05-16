from datetime import date


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """

    start_date = date(year1, month1, day1)
    end_date = date(year2, month2, day2)

    diff = end_date - start_date

    return diff.days


def testDaysBetweenDates():
    # test same day
    assert daysBetweenDates(2017, 12, 30, 2017, 12, 30) == 0
    # test adjacent days
    assert daysBetweenDates(2017, 12, 30, 2017, 12, 31) == 1
    # test new year
    assert daysBetweenDates(2017, 12, 30, 2018, 1, 1) == 2
    # test full year difference
    assert daysBetweenDates(2012, 6, 29, 2013, 6, 29) == 365

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


testDaysBetweenDates()
