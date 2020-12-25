from number_utils import count_percentage_share

CHART_PERCENTAGE_SHARE_STEP = 10


def get_chart_data_records(categories):
    categories_withdrawals = list(map(lambda c: (c.name, c.get_withdrawals_total()), categories))
    withdrawals_total = sum(total for _, total in categories_withdrawals)
    withdrawals_percentage_shares = [_get_percentage_share(r, withdrawals_total) for r in categories_withdrawals]

    return withdrawals_percentage_shares


def _get_percentage_share(record, withdrawals_total):
    name, category_total = record
    category_withdrawals_percentage_share = count_percentage_share(category_total, withdrawals_total)

    return name, round(category_withdrawals_percentage_share)
