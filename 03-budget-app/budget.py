from category import Category
from chart_utils import get_chart_data_records, get_chart_area, get_chart_x_axis, get_chart_labels

CHART_TITLE = 'Percentage spent by category'


def create_spend_chart(categories):
    chart_data_records = get_chart_data_records(categories)
    chart_area = get_chart_area(chart_data_records)
    chart_x_axis = get_chart_x_axis(chart_data_records)
    chart_labels = get_chart_labels(chart_data_records)

    return CHART_TITLE + '\n' + '\n'.join(chart_area) + '\n' + chart_x_axis + '\n' + '\n'.join(chart_labels)
