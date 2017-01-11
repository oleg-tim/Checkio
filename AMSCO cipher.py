def decode_amsco(message, key):
    import math
    mass = {}
    dlina_pass = len(message)
    key_str = str(key)
    dlina_stroki = len(key_str)*1.5
    kol_strok = int(dlina_pass / dlina_stroki)
    kol_posled_sim = dlina_pass-int(kol_strok*dlina_stroki)
    for i, nomer in enumerate(key_str, 1):
        nomer_stolbca = int(nomer)
        kol_bukv_do = int((i-1) * 1.5 + (kol_strok % 2) / 2)
        stolbec = key_str.index(str(i))+1
        stolbec_kol = int(kol_strok * 1.5 + (0 if (i % 2) else 0.5))
        bukv_ost = kol_posled_sim - kol_bukv_do
        dostupno_sim_v_pozition = int((i+kol_strok+1)%2+1.5)
        if bukv_ost > dostupno_sim_v_pozition:
            berem = dostupno_sim_v_pozition
        else:
            if bukv_ost < 0:
                berem = 0
            else:
                berem = bukv_ost
        vsego_sim = berem+stolbec_kol
        mass[nomer_stolbca] = vsego_sim
    for i in range(1, len(key_str)+1):
        mass[i], message = message[:mass[i]], message[mass[i]:]
    all_strok = math.ceil(dlina_pass / dlina_stroki)
    result = ''
    for nomer_stroki in range(1, all_strok+1):
        for i, nomer in enumerate(key_str, 1):
            nomer_stolbca = int(nomer)
            kol_sim = int((nomer_stroki+i)%2+1.5)
            result += mass[nomer_stolbca][:kol_sim]
            mass[nomer_stolbca] = mass[nomer_stolbca][kol_sim:]
    return result

if __name__ == '__main__':
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"

