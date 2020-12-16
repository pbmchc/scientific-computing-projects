from constants import AM, CLOCK_HOURS, DAYS_OF_WEEK, ONE_HOUR_IN_MINUTES, PM
import time_utils

NEXT_DAY_SUFFIX = 'next day'
DAYS_LATER_SUFFIX = 'days later'


def add_time(start, duration, start_day=None):
    start_time, start_day_period = start.split(' ')
    start_hours, start_minutes = time_utils.split_time(start_time)
    start_hours = start_hours if start_day_period == AM else start_hours + CLOCK_HOURS
    end_hours, end_minutes = get_end_time_parts(start_hours, start_minutes, duration)

    passed_periods = time_utils.count_passed_periods(start_hours, end_hours)
    passed_days = time_utils.count_passed_days(passed_periods, start_day_period)

    end_day = get_end_day(start_day, passed_days)
    end_day_period = get_end_day_period(passed_periods, start_day_period)
    end_relative_part_suffix = get_end_relative_part_suffix(passed_days)
    end_time = time_utils.format_clock_hours(end_hours) + ':' + time_utils.format_clock_minutes(end_minutes)
    separator = ', ' if end_day else ''

    return (end_time + ' ' + end_day_period + separator + end_day + ' ' + end_relative_part_suffix).strip()


def get_end_time_parts(start_hours, start_minutes, duration):
    duration_hours, duration_minutes = time_utils.split_time(duration)
    end_hours = start_hours + duration_hours
    end_minutes = start_minutes + duration_minutes

    if end_minutes > ONE_HOUR_IN_MINUTES:
        end_hours += 1
        end_minutes -= ONE_HOUR_IN_MINUTES

    return end_hours, end_minutes


def get_end_day(start_day, passed_days):
    if start_day is None:
        return ''

    start_day_index = [day.lower() for day in DAYS_OF_WEEK].index(start_day.lower())
    end_day_index = (start_day_index + passed_days) % len(DAYS_OF_WEEK)

    return DAYS_OF_WEEK[end_day_index]


def get_end_day_period(passed_periods, start_day_period):
    if passed_periods % 2 == 0:
        return start_day_period

    return AM if start_day_period == PM else PM


def get_end_relative_part_suffix(passed_days):
    if passed_days == 0:
        return ''

    suffix = str(passed_days) + ' ' + DAYS_LATER_SUFFIX if passed_days > 1 else NEXT_DAY_SUFFIX

    return '(' + suffix + ')'
