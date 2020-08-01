import csv
from collections import defaultdict


result = defaultdict(int)
for src in ['jingansi', 'lujiazui', 'caohejing','zhangjiang']:
    with open('{}.csv'.format(src), newline='') as csvfile:
        tmp_res = []
        line = csv.reader(csvfile, delimiter=',')
        for row in line:
            expense = "0"
            stop = row[1]
            if len(row) > 2 and row[2]:
                expense = row[2]
            if int(expense) <= 2000:
                tmp_res.append(stop)
        for _ in set(tmp_res):
            result[_] += 1

with open("res.csv", "w") as output:
    output.write('stop,weight\n')
    for stop in result:
        output.write('{},{}\n'.format(stop, result[stop]))

print(result)
