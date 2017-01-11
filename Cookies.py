def get_cookie(cookie, name):
    import re
    for a in re.findall('\w*=\w*', cookie):
        if a.split("=")[0] == name:
            value = a.split("=")[1]
    return value

if __name__ == "__main__":
    assert get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light', 'theme=light'
    assert get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true', 'ffo=true'
    print("Looks like you know everything. It is time for 'Check'!")

