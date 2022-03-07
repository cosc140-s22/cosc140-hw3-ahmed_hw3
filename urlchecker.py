#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

def urlchecker(url: str):
    # If a # is present, it must appear before the ?, if present
    if(url.find("#") > url.find("?") > -1):
        return False

    if not all([url.count(" ") == 0, url.count("#") <= 1, url.count("?") <= 1, 1 <= url.count(":") <= 2]):
        '''
            There cannot be any spaces in the URL
            There can only be a single #
            There can only be a single ?
            There must be at least one and at most 2 colons (one for scheme and an optional for port)
        '''
        return False

    if (url.startswith(("http://", "https://"))):  # scheme must be http or https;
        url_split = url.split("://")
        if(len(url_split) == 2):
            remain = url_split[1]
            if(remain.find(":") < remain.find("/") > -1):  # there must be a slash after the hostname (and optional port)
                hp = remain.split("/")[0].split(":")
                hostname, port = (hp[0], None) if len(hp) == 1 else (hp[0], hp[1])
                if(len(hostname) >= 1):  # hostname must not be empty
                    return True if not port else port.isdigit()  # Port, if present, must only be digits
    return False


def testurl():
    urls = [  # valid
        ['https://example.com/', True],
        ['http://example.com/', True],
        ['http://example.com/?query', True],
        ['http://example.com/#fragment', True],
        ['http://example/', True],
        ['http://example/path/', True],
        ['http://example/path', True],
        ['https://example.com:3000/path#fragment?query', True],
        ['https://example.com/path#fragment?query', True],
        # invalid
        ['htt://example/', False],
        ['httpss://example/', False],
        ['https://example/:3000', False],
        ['https://example/?:3000?', False],
        ['https://example/?:3000#', False],
        ['https://example/xy z', False],
        ['https://example/xyz:', False],
        ['https://example', False],
    ]
    for url, expected in urls:
        if urlchecker(url) != expected:
            print(f"{url} is not valid, but your function claimed the opposite")
        else:
            print(f"{url} - ok")


testurl()
