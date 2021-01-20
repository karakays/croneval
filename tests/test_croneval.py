from croneval import croneval


DT_FIELD_RANGES = {
    'min':  list(range(0, 60)),
    'hour': list(range(0, 24)),
    'day':  list(range(1, 32)),
    'mon':  list(range(1, 13)),
    'week': list(range(0, 7))
}


def test_cron_at_every_minute():
    cron = '* * * * *'
    cron = cron.split(' ')
    cron_dict = croneval.evaluate(cron)
    assert len(cron_dict) == 5
    assert DT_FIELD_RANGES['min'] == cron_dict['min']
    assert DT_FIELD_RANGES['hour'] == cron_dict['hour']
    assert DT_FIELD_RANGES['day'] == cron_dict['day']
    assert DT_FIELD_RANGES['mon'] == cron_dict['mon']
    assert DT_FIELD_RANGES['week'] == cron_dict['week']


def test_cron_at_every_hour():
    cron = '0 * * * *'
    cron = cron.split(' ')
    cron_dict = croneval.evaluate(cron)
    assert len(cron_dict) == 5
    assert list([0]) == cron_dict['min']
    assert DT_FIELD_RANGES['hour'] == cron_dict['hour']
    assert DT_FIELD_RANGES['day'] == cron_dict['day']
    assert DT_FIELD_RANGES['mon'] == cron_dict['mon']
    assert DT_FIELD_RANGES['week'] == cron_dict['week']


def test_cron_at_every_two_hour():
    cron = '0 */2 * * *'
    cron = cron.split(' ')
    cron_dict = croneval.evaluate(cron)
    assert len(cron_dict) == 5
    assert list([0]) == cron_dict['min']
    assert list(range(0, 24, 2)) == cron_dict['hour']
    assert DT_FIELD_RANGES['day'] == cron_dict['day']
    assert DT_FIELD_RANGES['mon'] == cron_dict['mon']
    assert DT_FIELD_RANGES['week'] == cron_dict['week']


def test_cron_at_midnight_on_weekend():
    cron = "0 0,1,2 * * 6,0"
    cron = cron.split(' ')
    cron_dict = croneval.evaluate(cron)
    assert len(cron_dict) == 5
    assert list([0]) == cron_dict['min']
    assert list(range(0, 3)) == cron_dict['hour']
    assert DT_FIELD_RANGES['day'] == cron_dict['day']
    assert DT_FIELD_RANGES['mon'] == cron_dict['mon']
    assert list([6, 0]) == cron_dict['week']


def test_cron_at_midnight_on_weekdays_and_sunday():
    cron = "0 2 * * 0,1-5"
    cron = cron.split(' ')
    cron_dict = croneval.evaluate(cron)
    assert len(cron_dict) == 5
    assert list([0]) == cron_dict['min']
    assert list([2]) == cron_dict['hour']
    assert DT_FIELD_RANGES['day'] == cron_dict['day']
    assert DT_FIELD_RANGES['mon'] == cron_dict['mon']
    assert list([0, 1, 2, 3, 4, 5]) == cron_dict['week']


def test_cron_at_workhours_on_weekdays():
    cron = "0 8-17/2 * * 1-5"
    cron = cron.split(' ')
    cron_dict = croneval.evaluate(cron)
    assert len(cron_dict) == 5
    assert list([0]) == cron_dict['min']
    assert list(range(8, 17, 2)) == cron_dict['hour']
    assert DT_FIELD_RANGES['day'] == cron_dict['day']
    assert DT_FIELD_RANGES['mon'] == cron_dict['mon']
    assert list(range(1, 6)) == cron_dict['week']
