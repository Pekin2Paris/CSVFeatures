import csv
# import mycsvtools

# with open('dataset/test.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     column = [row['DepartmentDescription'] for row in reader]
#     print(len(column))
#     features = ["TripType","VisitNumber", "Weekday"] + list(set(column))
#     print(len(features))

# with open('dataset/train.csv', newline='') as csvFile:
#     reader = csv.reader(csvFile)
#     for i,row in enumerate(reader):
#         if i == 0:
#             header = row
# print(header)

# len_to_read = 10
# f_csv = open('dataset/train.csv', 'r')
# headline = f_csv.readline()
# print(headline)
# print([headline])
# print([row for row in csv.reader([headline])][0])
# print("\n\n")
#
# with open('dataset/train.csv', newline='') as csvFile:
#     reader = csv.reader(csvFile)
#     for i,row in enumerate(reader):
#         if i < 10:
#             print(row)
# print("\n\n")
# #
# retlist, current_position = mycsvtools.readcsv2list('dataset/train.csv', [], 0, 10)
# for list in retlist:
#     print(list)

# ind = 0
# columnListTrain = [[] for i in range(2)]
# with open('dataset/train.csv', newline='') as csvFile:
#     reader = csv.DictReader(csvFile)
#     for row in reader:
#         ind += 1
#         print(ind)
#         columnListTrain[0].append(row['DepartmentDescription'])
#         columnListTrain[1].append(row['FinelineNumber'])
#
# columnListTest = [[] for i in range(2)]
# with open('dataset/test.csv', newline='') as csvFile:
#     reader = csv.DictReader(csvFile)
#     for row in reader:
#         ind += 1
#         print(ind)
#         columnListTest[0].append(row['DepartmentDescription'])
#         columnListTest[1].append(row['FinelineNumber'])
#
# features = ['TripType','VisitNumber', 'Weekday'] + list(set(columnListTrain[0] + columnListTest[0])) + list(set(columnListTrain[1] + columnListTest[1]))
# print(len(features))

# ind = 0
# featureList = [[] for i in range(len(features))]
# # for i in range(len(features)):
# #     featureList[i].append(0)
# #     print(featureList[i])
# with open('dataset/train.csv', newline='') as csvFile:
#     reader = csv.DictReader(csvFile)
#     for row in reader:
#         ind += 1
#         print(ind)
#         if row['VisitNumber'] in featureList[features.index('VisitNumber')]:
#             featureList[features.index(row['DepartmentDescription'])][-1] += int(row['ScanCount'])
#             featureList[features.index(row['FinelineNumber'])][-1] += int(row['ScanCount'])
#         else:
#             for i in range(len(features)):
#                 featureList[i].append(0)
#             featureList[features.index('TripType')][-1] = row['TripType']
#             featureList[features.index('VisitNumber')][-1] = row['VisitNumber']
#             featureList[features.index('Weekday')][-1] = row['Weekday']
#             featureList[features.index(row['DepartmentDescription'])][-1] = int(row['ScanCount'])
#             featureList[features.index(row['FinelineNumber'])][-1] = int(row['ScanCount'])

# ind = 0
# featureList = [[] for i in range(len(features))]
# with open('dataset/train.csv', newline='') as csvFile:
#     reader = csv.DictReader(csvFile)
#     for row in reader:
#         ind += 1
#         print(ind,"\t\t")
#         if row['VisitNumber'] in featureList[features.index('VisitNumber')]:
#             for feature in features:
#                 if feature in [row['DepartmentDescription'], row['FinelineNumber']]:
#                     # print(featureList[features.index(feature)], "\n")
#                     featureList[features.index(feature)][-1] += int(row['ScanCount'])
#         else:
#             for feature in features:
#                 if feature in ['TripType','VisitNumber', 'Weekday']:
#                     featureList[features.index(feature)].append(row[feature])
#                 elif feature in [row['DepartmentDescription'], row['FinelineNumber']]:
#                     #if feature == "1511":
#                         # print(features.index(feature))
#                         # print(int(row['ScanCount']))
#                     featureList[features.index(feature)].append(int(row['ScanCount']))
#                 else:
#                     featureList[features.index(feature)].append(0)

# print(ind)
# print(len(featureList))
# print(len(featureList[0]))

# f = open("dataset/feature.train.csv", 'w')
#
# for j in range(len(features)-1):
#     if "," in features[j]:
#         f.write("\"%s\"," % features[j])
#     else:
#         f.write("%s," % features[j])
# f.write("%s\n" % features[-1])
#
# for i in range(len(featureList[0])):
#     for j in range(len(features)-1):
#         f.write("%s," % featureList[j][i])
#     f.write("%s\n" % featureList[-1][i])
# f.close()

# ind = 0
# featureList = [[] for i in range(len(features))]
# # for i in range(len(features)):
# #     featureList[i].append(0)
# #     print(featureList[i])
# with open('dataset/test.csv', newline='') as csvFile:
#     reader = csv.DictReader(csvFile)
#     for row in reader:
#         ind += 1
#         print(ind)
#         if row['VisitNumber'] in featureList[features.index('VisitNumber')]:
#             featureList[features.index(row['DepartmentDescription'])][-1] += int(row['ScanCount'])
#             featureList[features.index(row['FinelineNumber'])][-1] += int(row['ScanCount'])
#         else:
#             for i in range(len(features)):
#                 featureList[i].append(0)
#             featureList[features.index('TripType')][-1] = -1
#             featureList[features.index('VisitNumber')][-1] = row['VisitNumber']
#             featureList[features.index('Weekday')][-1] = row['Weekday']
#             featureList[features.index(row['DepartmentDescription'])][-1] = int(row['ScanCount'])
#             featureList[features.index(row['FinelineNumber'])][-1] = int(row['ScanCount'])
#
#
# f = open("dataset/feature.test.csv", 'w')
#
# for j in range(len(features)-1):
#     if "," in features[j]:
#         f.write("\"%s\"," % features[j])
#     else:
#         f.write("%s," % features[j])
# f.write("%s\n" % features[-1])
#
# for i in range(len(featureList[0])):
#     for j in range(len(features)-1):
#         f.write("%s," % featureList[j][i])
#     f.write("%s\n" % featureList[-1][i])
# f.close()
