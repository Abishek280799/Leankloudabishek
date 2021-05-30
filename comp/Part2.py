import csv
from csv import writer
from csv import reader
line1_count=0
ls=[]
with open('Student_marks_list.csv') as csvFile:
    csv_read = csv.reader(csvFile, delimiter=",")

    line2_count = 0
    id_max = []
    value_max = 0
    id1_max = []
    value1_max = 0
    id2_max = []
    value2_max = 0
    id3_max = []
    value3_max = 0
    id4_max = []
    value4_max = 0
    id5_max = []
    value5_max = 0
    id10_max = 0


    for row in csv_read:

        if line2_count == 0:
            line2_count += 1
        else:

            if float(row[1]) > value_max:
                value_max = float(row[1])
            if float(row[2]) > value1_max:
                value1_max = float(row[2])
            if float(row[3]) > value2_max:
                value2_max = float(row[3])
            if float(row[4]) > value3_max:
                value3_max = float(row[4])
            if float(row[5]) > value4_max:
                value4_max = float(row[5])
            if float(row[6]) > value5_max:
                value5_max = float(row[6])

with open('Student_marks_list.csv') as csvFile:
    csvp = csv.reader(csvFile, delimiter=",")
    line3_count = 0
    id_max = []
    for row in csvp:

        if line3_count == 0:
            line3_count += 1
        else:

            if float(row[1]) == value_max:
                id_max.append(row[0])
            if float(row[2]) == value1_max:
                id1_max.append(row[0])
            if float(row[3]) == value2_max:
                id2_max.append(row[0])
            if float(row[4]) == value3_max:
                id3_max.append(row[0])
            if float(row[5]) == value4_max:
                id4_max.append(row[0])
            if float(row[6]) == value5_max:
                id5_max.append(row[0])

    separator = ", "

    print(f'Topper in Maths is {separator.join(id_max)}')

    print(f'Topper in Biology is {separator.join(id1_max)}')

    print(f'Topper in English is {separator.join(id2_max)}')

    print(f'Topper in Physics is {separator.join(id3_max)}')

    print(f'Topper in Chemistry is {separator.join(id4_max)}')

    print(f'Topper in Hindi is {separator.join(id5_max)}')

with open('Student_marks_list.csv', 'r') as read_obj, \
        open('output_1.csv', 'w', newline='') as write_obj:

    csv_reader = reader(read_obj)

    csv_writer = writer(write_obj)

    for row in csv_reader:
        if line1_count == 0:

            row.append('Average')
            line1_count += 1

        else:
            sum = float(row[1]) + float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6])
            avg = sum / 6

            row.append(avg)
            csv_writer.writerow(row)
            ls.append(row[7])

ls.sort(reverse=True)

max,max1,max2=ls[0],ls[1],ls[2]
line_count=0
first=0
second=0
third=0
lsk=[]
with open('output_1.csv') as read_obj:
    csv_read = csv.reader(read_obj, delimiter=",")
    for row in csv_read:

         if line_count==0:
            line_count+=1
         else:

             if float(row[7]) == max:
                 first=row[0]
             if float(row[7]) == max1:
                 second=row[0]
             if float(row[7]) == max2:
                 third=row[0]
lsk=[first,second,third]


separator = ", "


print(f'Best students in the class are ({separator.join(lsk)})')
