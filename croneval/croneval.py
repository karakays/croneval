DT_FIELD_RANGES = {
    'min':  '0-59',
    'hour': '0-23',
    'day':  '1-31',
    'mon':  '1-12',
    'week': '0-6'
}


def evaluate(cron):
    expr_parts = {
        'min':  cron[0],
        'hour': cron[1],
        'day':  cron[2],
        'mon':  cron[3],
        'week': cron[4]
    }

    cron_dict = {}

    for field, val in expr_parts.items():
        values = []
        # Parse list items
        for v in val.split(','):
            # Parse ranges with possible step values
            if '-' in v:
                _range = v
                step = 1
                if '/' in v:
                    _range, step = v.split('/')
                    step = int(step)
                first, last = [int(s) for s in _range.split('-')]
                values.extend(list(
                              range(int(first), int(last) + 1, step)))
            elif '*' in v:
                _range = v
                step = 1
                if '/' in v:
                    _range, step = v.split('/')
                    step = int(step)
                first, last = [int(s) for s in
                               DT_FIELD_RANGES[field].split('-')]
                values.extend(list(
                    range(int(first), int(last) + 1, step)))
            else:
                values.append(int(v))
        cron_dict[field] = values

    return cron_dict


def run(args):
    if not len(args) == 2:
        help()

    cron = args[1].split()
    if not len(cron) == 6:
        help()

    cron_dict = evaluate(cron[0:5])
    command = cron[5]

    label_minute = 'minute'
    label_hour = 'hour'
    label_day = 'day of month'
    label_month = 'month'
    label_week = 'day of week'
    label_command = 'command'

    output = f'''{label_minute:14}{' '.join([str(s) for s in cron_dict['min']])}
{label_hour:14}{' '.join([str(s) for s in cron_dict['hour']])}
{label_day:14}{' '.join([str(s) for s in cron_dict['day']])}
{label_month:14}{' '.join([str(s) for s in cron_dict['mon']])}
{label_week:14}{' '.join([str(s) for s in cron_dict['week']])}
{label_command:14}{command}
'''
    print(output)


def help():
    print("Usage: croneval \"* * * * * [COMMAND]\"")
    exit(1)
