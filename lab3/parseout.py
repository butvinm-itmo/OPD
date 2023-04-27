from dataclasses import dataclass


@dataclass
class Tick:
    ip: str
    cr: str
    ar: str
    dr: str
    sp: str
    br: str
    ac: str
    nzvc: str


mtrace: list[Tick] = []

with open('out.txt', 'r') as f:
    for line in f:
        _, _, ip, cr, ar, dr, sp, br, ac, nzvc, _ = line.split()
        mtrace.append(Tick(ip, cr, ar, dr, sp, br, ac, nzvc))

print(*mtrace, sep='\n')

trace: list[Tick] = []
for i in range(len(mtrace) - 1):
    if int(mtrace[i].ip, 16) < int(mtrace[i + 1].ip, 16):
        trace.append(mtrace[i])

# print(*trace, sep='\n')

print('DM')
for tick in trace:
    if tick.cr[0] == 'E':
        print(tick.cr, tick.ar, tick.dr)
