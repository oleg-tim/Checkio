def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    prefix, zn = '', ''
    if number < 0:
        zn = "-"
    number, answer = abs(number), number

    for i, power in enumerate(powers):
        if number // (base**i) > 0:
            answer = number // (base**i)
            prefix = powers[i]

    if decimals:
        i = powers.index(prefix)
        frac = round(float(number) / (base**i), decimals)
        form = str(frac).split(".")
        answer = form[0] + "." + form[1].ljust(decimals, "0")

    return zn+str(answer)+prefix+suffix

if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'


