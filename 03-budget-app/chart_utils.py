from number_utils import count_percentage_share

CHART_BAR_BUILDING_BLOCK = 'o'
CHART_PERCENTAGE_SHARE_STEP = 10
CHART_X_AXIS_BUILDING_BLOCK = '-'
CHART_Y_AXIS_TICK_LABEL_LENGTH = 4
CHART_Y_AXIS_TICK_LABEL_VALUE_LENGTH = 3
CHART_Y_AXIS_TICK_LABEL_SEPARATOR = '|'


def get_chart_data_records(categories):
    categories_withdrawals = list(map(lambda c: (c.name, c.get_withdrawals_total()), categories))
    withdrawals_total = sum(total for _, total in categories_withdrawals)
    withdrawals_percentage_shares = [_get_percentage_share(r, withdrawals_total) for r in categories_withdrawals]

    return withdrawals_percentage_shares


def get_chart_area(chart_records):
    y_axis_ticks = range(100, -10, -CHART_PERCENTAGE_SHARE_STEP)
    x_axis_length = _get_chart_x_axis_length(chart_records)

    return [_get_chart_area_section(tick, chart_records, x_axis_length) for tick in y_axis_ticks]


def get_chart_x_axis(chart_records):
    x_axis_length = _get_chart_x_axis_length(chart_records)

    return (x_axis_length * CHART_X_AXIS_BUILDING_BLOCK).rjust(x_axis_length + CHART_Y_AXIS_TICK_LABEL_LENGTH)


def get_chart_labels(chart_records):
    max_label_length = max([len(label) for label, _ in chart_records])
    x_axis_length = _get_chart_x_axis_length(chart_records)

    return [_get_chart_labels_section(character, chart_records, x_axis_length) for character in range(max_label_length)]


def _get_percentage_share(chart_record, withdrawals_total):
    label, value = chart_record
    category_withdrawals_percentage_share = count_percentage_share(value, withdrawals_total)

    return label, round(category_withdrawals_percentage_share)


def _get_chart_area_section(tick, chart_records, x_axis_length):
    chart_y_axis_tick_label = str(tick).rjust(CHART_Y_AXIS_TICK_LABEL_VALUE_LENGTH)
    chart_bar_part = [_get_chart_bar_part(value, tick) for _, value in chart_records]
    chart_area_section = chart_y_axis_tick_label + CHART_Y_AXIS_TICK_LABEL_SEPARATOR + ' ' + ''.join(chart_bar_part)

    return chart_area_section.ljust(x_axis_length + CHART_Y_AXIS_TICK_LABEL_LENGTH)


def _get_chart_bar_part(value, tick):
    return CHART_BAR_BUILDING_BLOCK + '  ' if value >= tick else '   '


def _get_chart_labels_section(character, chart_records, x_axis_length):
    chart_label_part = [_get_chart_label_part(label, character) for label, _ in chart_records]

    return ''.join(chart_label_part).rjust(x_axis_length + CHART_Y_AXIS_TICK_LABEL_LENGTH)


def _get_chart_label_part(label, index):
    return label[index] + '  ' if len(label) >= index + 1 else '   '


def _get_chart_x_axis_length(chart_records):
    chart_records_count = len(chart_records)

    return chart_records_count + chart_records_count * 2 + 1
