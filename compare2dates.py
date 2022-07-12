import time

raw_date_last_tag = '2021-06-21T09:12:11.000+03:00'
raw_date_new_tag = '2021-06-21T09:12:11.000+03:00'

# формат даты: '2021-06-21T09:12:11'
date1 = raw_date_last_tag.split('.')[0]
date2 = raw_date_new_tag.split('.')[0]

new_date_format_1_lastTag = time.strptime(date1, '%Y-%m-%dT%H:%M:%S')
new_date_format_2_lastTag = time.strptime(date2, '%Y-%m-%dT%H:%M:%S')

if new_date_format_1_lastTag < new_date_format_2_lastTag:
    print('more than')
else:
    print('less than')