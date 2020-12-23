from number_utils import count_percentage_share, round_to_nearest

CHART_PERCENTAGE_SHARE_STEP = 10


def get_chart_data_records(categories):
    categories_withdrawals = list(map(lambda c: (c.name, c.get_withdrawals_total()), categories))
    withdrawals_total = sum(total for _, total in categories_withdrawals)
    withdrawals_percentage_shares = [_get_percentage_share(r, withdrawals_total) for r in categories_withdrawals]

    return sorted(withdrawals_percentage_shares, key=lambda r: r[1], reverse=True)


def _get_percentage_share(record, withdrawals_total):
    name, category_total = record
    category_withdrawals_percentage_share = count_percentage_share(category_total, withdrawals_total)

    return name, round_to_nearest(category_withdrawals_percentage_share, step=CHART_PERCENTAGE_SHARE_STEP)
