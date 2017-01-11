def total_cost(calls):
    import math

    def cash(x, call_day):
        a = math.ceil(x / 60)
        if call_day > 100:
            rez = a * 2 + call_day
        else:
            if call_day + a > 100:
                call2 = call_day + a - 100
                call1 = a - call2
                rez = call2*2 + call1 + call_day
            else:
                rez = a + call_day
        return rez

    mass_data = {}
    for a in calls:
        data = a[:10]
        len_call = int(a[20:])
        if mass_data.get(data):
            mass_data[data] = cash(len_call, mass_data[data])
        else:
            mass_data[data] = cash(len_call, 0)

    return sum(mass_data.values())

if __name__ == '__main__':
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"

