def printStats(folderName):
    with open('./' + folderName + '/evaluation') as f:
        lines = f.readlines()
    # Deletes values which are not map, Rprec or P_10; saves substrings inside lines
    f = 0
    while f<len(lines):
        spacePos = lines[f].find(' ')
        lineType = lines[f][:spacePos]
        if (lineType != 'map') and (lineType != 'Rprec') and (lineType != 'P_10'):
            del lines[f]
        else:
            lines[f] = lines[f].split(' ')
            g = 0
            while g<len(lines[f]):
                if lines[f][g] == '':
                    del lines[f][g]
                else:
                    g += 1
            lines[f][1] = lines[f][1].strip()
            temp = lines[f][1].split('\t')
            lines[f][1] = temp[0]
            lines[f].append(temp[1])
            f += 1
    # Deletes general values
    lines = lines[:-1]
    lines = lines[:-1]
    lines = lines[:-1]
    # Separates the three values of every topic, in order to improve the organization of data
    run = []
    for f in range(0, len(lines), 3):
        run.append([lines[f], lines[f+1], lines[f+2]])
    return run


runs = []
runs.append(printStats('Run1_Stopword+Stemmer+BM25'))
runs.append(printStats('Run2_Stopword+Stemmer+TF_IDF'))
runs.append(printStats('Run3_Stemmer+BM25'))
runs.append(printStats('Run4_TF_IDF'))
# Divides the three measures in three different files; every file contains a table of the measure for each run and for every topic
with open('map.txt', 'w+') as f:
    f.write("Run1 Run2 Run3 Run4\n")
    for t in range(len(runs[0])):
        f.write(runs[0][t][0][2] + ' ' + runs[1][t][0][2] + ' ' + runs[2][t][0][2] + ' ' + runs[3][t][0][2] + "\n")
with open('Rprec.txt', 'w+') as f:
    f.write("Run1 Run2 Run3 Run4\n")
    for t in range(len(runs[0])):
        f.write(runs[0][t][1][2] + ' ' + runs[1][t][1][2] + ' ' + runs[2][t][1][2] + ' ' + runs[3][t][1][2] + "\n")
with open('P@10.txt', 'w+') as f:
    f.write("Run1 Run2 Run3 Run4\n")
    for t in range(len(runs[0])):
        f.write(runs[0][t][2][2] + ' ' + runs[1][t][2][2] + ' ' + runs[2][t][2][2] + ' ' + runs[3][t][2][2] + "\n")

