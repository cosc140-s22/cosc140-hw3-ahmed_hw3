#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

def urlchecker(url: str):
    if(url.count(":") > 2):  # Aside from port and scheme, no other colons may be present in the url
        return False

    if(url.count(" ") > 0):  # There cannot be any spaces in the URL
        return False

    # there can only be a single #
    if(url.count("#") > 1):
        return False

    # there can only be a single ?
    if(url.count("?") > 1):
        return False

    # If a # is present, it must appear before the ?, if present
    if ("?" in url and "#" in url):
        if(url.find("#") > url.find("?")):
            return False

    if (url.startswith(("http://", "https://"))):  # scheme must be http or https;
        url_split = url.split("://")
        if(len(url_split) == 2):
            remain = url_split[1]
            # Port must be before the slash
            if(":" in remain and ":" in remain):
                if(remain.find(":") > remain.find("/")):
                    return False
            if(remain.count("/") > 0):  # there must be a slash after the hostname (and optional port)
                hp = remain.split("/")[0]
                hp_split = hp.split(":")
                hostname = hp_split[0]
                if(len(hostname) >= 1):  # hostname must not be empty
                    if(len(hp_split) == 2):
                        # port, if present, must only be digits
                        port = hp_split[1]
                        if (port.isdigit()):
                            return True
                    else:
                        return True
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
