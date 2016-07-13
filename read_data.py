import csv


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

count = 0
count_total = 0

with open("./5gram-edits-train.tsv") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        count_total += 1
        #print(line[5])



        if line[3] == 'true' and '[[' not in line[6] and '{{' not in line[6] and '[[' not in line[6] and '{{' not in line[7] and  '[[' not in line[7] and levenshtein(line[6],line[7])>=4 and len(line[6].split(' '))<2 and len(line[7].split(' '))<6:
            print(line[6])
            print(line[7])
            print(line[9])
            print('------------')
            count += 1

print(count)
print(count_total)