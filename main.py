import requests
def selections(seq, n):
    if n == 0:
        yield []
    else:
        for i in range(len(seq)):
            for ss in selections(seq, n - 1):
                yield [seq[i]] + ss


iterable = '0123456789_abcdefghijklmnopqrstuvwxyz'
sample_size = len(iterable)
sel = list(selections(iterable, 3))

for item in sel:
    s = "".join(item)
    response = requests.get("https://api.mojang.com/users/profiles/minecraft/{0}".format(s))
    if response.status_code == 204:
        print("[INFO] {0} is not taken.".format(s))
    else:
        print("[INFO] {0} is taken.".format(s))
