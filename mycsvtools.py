def readcsv2list(filename, rows, last_position, max_line):

    import csv

    fileobj = open(filename, 'r')
    fileobj.seek(last_position)
    datalines = []

    for i in range(max_line):
        line_itme = fileobj.readline()
        if len(line_itme) > 0:
            datalines.append(line_itme)
        else:
            break

    csvreader = csv.reader(datalines)
    retlist = []

    for row in csvreader:
        clist = []
        selected_rows = [ic for ic in range(len(row)) if ic not in rows]
        for c in selected_rows:
            clist.append(row[c])
        retlist.append(clist)

    current_position = fileobj.tell()
    fileobj.close()

    return retlist, current_position