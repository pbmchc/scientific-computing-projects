from constants import CLOCK_HOURS, PM, TIME_PARTS_SEPARATOR


def count_passed_days(passed_periods, start_day_period):
    if passed_periods == 0:
        return 0

    passed_days = round(passed_periods / 2 + 0.5)

    return passed_days if start_day_period == PM else passed_days - 1


def count_passed_periods(start_hours, end_hours):
    start_period = start_hours // CLOCK_HOURS
    end_period = end_hours // CLOCK_HOURS

    return end_period - start_period


def format_clock_hours(hours):
    clock_hours = hours if hours <= CLOCK_HOURS else hours % CLOCK_HOURS

    return str(clock_hours) if clock_hours > 0 else str(CLOCK_HOURS)


def format_clock_minutes(minutes):
    clock_minutes = str(minutes)

    return clock_minutes if len(clock_minutes) > 1 else '0' + clock_minutes


def split_time(time):
    return [int(part) for part in time.split(TIME_PARTS_SEPARATOR)]
