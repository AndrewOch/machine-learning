import pandas as pd


def parse_datetime(x):
    for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S"):
        try:
            return pd.to_datetime(x, format=fmt)
        except ValueError:
            continue
    raise ValueError('no valid date format found')


def calculate_stats(grouped_data):
    mean = grouped_data.mean()
    variance = grouped_data.var()
    return mean, variance


def assign_labels(row):
    day_in_month = row[timestamp_column_name].day
    return 1 + ((day_in_month - 1) % 3)


def get_week_number(date):
    return date.isocalendar()[1]


def hourly(data_target_month):
    data_target_month['day_group'] = data_target_month.apply(assign_labels, axis=1)
    hourly_counts = (data_target_month.groupby([data_target_month[timestamp_column_name].dt.hour, 'day_group'])
                     .size().reset_index(name='count'))
    result = hourly_counts.pivot(index='day_group', columns=timestamp_column_name, values='count').fillna(0)
    result_1x72 = result.melt(ignore_index=True)
    result_1x72['row_number'] = range(1, 73)
    result_1x72 = result_1x72.drop(columns=[timestamp_column_name])
    result_1x72.to_csv('result_hourly.csv', index=False)
    print(result_1x72)


def daily(data_target_month):
    daily_counts = data_target_month.groupby(data_target_month[timestamp_column_name].dt.date).size().reset_index(
        name='count')
    daily_counts['day_number'] = range(1, len(daily_counts) + 1)
    daily_counts.drop(columns=[timestamp_column_name], inplace=True)
    daily_counts.to_csv('result_daily_counts.csv', index=False)
    print(daily_counts)


def mondays(data_3_months):
    mondays = data_3_months[data_3_months[timestamp_column_name].dt.weekday == 0]
    weekly_counts = mondays.groupby(mondays[timestamp_column_name].dt.date).size().reset_index(name='count')
    weekly_counts['week_number'] = weekly_counts[timestamp_column_name].apply(get_week_number)
    weekly_counts = weekly_counts.drop(columns=[timestamp_column_name])
    weekly_counts.to_csv('result_mondays.csv', index=False)
    print(weekly_counts)


def sundays(data_3_months):
    sundays = data_3_months[data_3_months[timestamp_column_name].dt.weekday == 6]
    weekly_counts = sundays.groupby(sundays[timestamp_column_name].dt.date).size().reset_index(name='count')
    weekly_counts['week_number'] = weekly_counts[timestamp_column_name].apply(get_week_number)
    weekly_counts = weekly_counts.drop(columns=[timestamp_column_name])
    weekly_counts.to_csv('result_sundays.csv', index=False)
    print(weekly_counts)


def weekly(data_3_months):
    data_3_months['week_number'] = data_3_months[timestamp_column_name].dt.isocalendar().week
    weekly_counts = data_3_months.groupby('week_number').size().reset_index(name='count')
    weekly_counts.to_csv('result_weekly.csv', index=False)
    print(weekly_counts)


def total_hours(data):
    data[timestamp_column_name] = pd.to_datetime(data[timestamp_column_name])
    hourly_counts = data.groupby(data[timestamp_column_name].dt.hour).size().reset_index(name='count')
    hourly_counts.rename(columns={timestamp_column_name: 'hour'}, inplace=True)
    hourly_counts.to_csv('result_total.csv', index=False)
    print(hourly_counts)


data = pd.read_csv('order.csv')
timestamp_column_name = 'timestamp_column_name'
data[timestamp_column_name] = data[timestamp_column_name].apply(parse_datetime)

data_2023 = data[data[timestamp_column_name].dt.year == 2022]
# data_2022 = data[data[timestamp_column_name].dt.year == 2022]

data_3_months = data_2023[data_2023[timestamp_column_name].dt.month.isin([4, 5, 6])]
#
# frames = [data_2022[data_2022[timestamp_column_name].dt.month.isin([12])],
#          data_2023[data_2023[timestamp_column_name].dt.month.isin([1, 2])]]
# data_3_months = pd.concat(frames)

data_target_month = data_3_months[data_3_months[timestamp_column_name].dt.month == 5]

hourly(data_target_month)
daily(data_target_month)
mondays(data_3_months)
sundays(data_3_months)
weekly(data_3_months)
# total_hours(data)