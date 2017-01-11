def power_supply(network, power_plants):

    new_network = []
    new_light = []
    not_light = set([y for x in network for y in x])
    for plant in power_plants:
        light = [plant]
        network = network
        for power_count in range(power_plants[plant]):
            for elem in network:
                if set(elem)&set(light):
                    z = list(set(elem)-set(light))
                    new_light += z
                else:
                    new_network.append(elem)
            light = new_light
            network = new_network
            new_light = []
            new_network = []
        raspakovka = [y for x in network for y in x]
        not_light = not_light&set(set(raspakovka)-set(light))
    return list(not_light)

if __name__ == '__main__':
    assert power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == ['c2'], 'one blackout'
    assert set(power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1})) == set(['c0', 'c3']), 'two blackout'
    assert power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == [], 'no blackout'
    assert set(power_supply([['c0', 'p1'], ['p1', 'c2']], {'p1': 0})) == set(['c0', 'c2']), 'weak power-plant'
    assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['c2', 'c3'], ['c3', 'p4'], ['p4', 'c5']], {'p0': 1, 'p4': 1}) == [], 'cooperation'
    assert set(power_supply([['c0', 'p1'], ['p1', 'c2'], ['c2', 'c3'], ['c2', 'c4'], ['c4', 'c5'],
                         ['c5', 'c6'], ['c5', 'p7']],
                        {'p1': 1, 'p7': 1})) == set(['c3', 'c4', 'c6']), 'complex cities 1'
    assert set(power_supply([['p0', 'c1'], ['p0', 'c2'], ['p0', 'c3'],
                         ['p0', 'c4'], ['c4', 'c9'], ['c4', 'c10'],
                       ['c10', 'c11'], ['c11', 'p12'], ['c2', 'c5'],
                       ['c2', 'c6'], ['c5', 'c7'], ['c5', 'p8']],
                      {'p0': 1, 'p12': 4, 'p8': 1})) == set(['c6', 'c7']), 'complex cities 2'
    assert set(power_supply([['c1', 'c2'], ['c2', 'c3']], {})) == set(['c1', 'c2', 'c3']), 'no power plants'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c4', 'c3'], ['c2', 'c3']], {'p1': 1}) == ['c3'], 'circle'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c2', 'c3']], {'p1': 4}) == [], 'more than enough'
    print("Looks like you know everything. It is time for 'Check'!")

