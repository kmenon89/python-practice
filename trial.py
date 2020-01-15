#_ _is the _ _ _so if you are not _a _make sure to _

import itertools

words=['Experience','Battlefield','Owning','Someone','Customer','Serves','Competitors','2020']
perm=list(itertools.permutations(words))
#perm.encode()


# string='_ _ is the _ _ _ so if you are not _ a _ make sure to _'
string='{} {} is the {} {} {} so if you are not {} a {} make sure to {}'

#print(string)

for words in perm:
    if words[0] != "2020":
        continue
    if words[5] != "Owning":
        continue
    if words[6] != "Battlefield":
        continue
    if words[7] != "Experience":
        continue
    print(string.format(*words))

# import csv

# with open('combinations.csv', 'wb') as csvfile:
#     filewriter = csv.writer(csvfile)
#     for i in perm:
#         filewriter.writerow(i)
# csvFile.close()


