def count_percentage_share(numerator, denominator):
    return (numerator / denominator) * 100


def format_decimal_places(amount):
    return '{:.2f}'.format(amount)


def round_to_nearest(value, step):
    return round(value / step) * step
