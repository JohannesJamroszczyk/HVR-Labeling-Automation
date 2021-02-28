def str_to_time(stri, interval):
    # This function takes in a time string of the format hh%mm%ss and return a time string that is x minutes earlier
    timeInt = int(stri[0:2]) * 60 + int(stri[3:5]) - interval  # converts hours and minutes to minute sum
    hours = int(timeInt / 60)  # singles out minutes and hours
    minutes = timeInt % 60
    if len(str(hours)) == 1:  # identifies weather hour is of format X or XX
        hourStr = "0" + str(hours)  # converts X format into 0X format
    else:
        hourStr = str(hours)
    if len(str(minutes)) == 1:  # identifies weather minute is of format X or XX
        minutesStr = "0" + str(minutes)  # converts X format into 0X format
    else:
        minutesStr = str(minutes)
    time = f"{hourStr}:{minutesStr}:{stri[6] + stri[7]}"  # Reestablishes original time string format for return
    return time


def popped_matrix(matrix, index):
    # accepts a matrix and an index and returns a matrix where
    # the value at the index of all sublists is popped
    for i in matrix:  # pops values at indicated indexes
        i.pop(index)
    return matrix


def labelList(matrix):
    labels = [[], []]
    number = 10
    for i in range(0, len(matrix[0])):
        for j in range(1, len(matrix)):
            if matrix[j][i] not in labels[1]:
                labels[0].append(number)
                labels[1].append(matrix[j][i])
                number += 1
    return labels

def matrix_to_config(matrix):
    # Converts matrices to a label-config file for VU-DAMS software. Returns text as string.
    x = ""
    uniques = []
    number = 10
    for i in range(0, len(matrix[0])):
        x += f"#{matrix[0][i]}\n"
        for j in range(1, len(matrix)):
            if matrix[j][i] not in uniques:
                uniques.append(matrix[j][i])
                x += f"{number} {matrix[j][i]}\n"
                number += 1
        x += "\n"
    return x


def matrix_to_label(labels, matrix, timearr, intervaltimearr, datearr, version, lablename, start, end):
    # This function creates the text structure of a label file and returns it as a string
    # Label text structure:
    cfg_str = f"Label Data File version {version}\n" \
              f"{lablename} {start} {end}\n" \
              f" Begin date/time    End date/time   Labelcode\n\n"
    for i in range(1, len(matrix)):
        cfg_str += f" {datearr[i]}/{intervaltimearr[i]}  {datearr[i]}/{timearr[i]} "
        s_line = ""
        for j in range(0,len(matrix[0])):
            if matrix[i][j] in labels[1]:
                cfg_str += f"  {labels[0][labels[1].index(matrix[i][j])]}"
                s_line += f"{labels[0][labels[1].index(matrix[i][j])]}={labels[1][labels[1].index(matrix[i][j])]}; "
        cfg_str += "\n"
        cfg_str += f"{s_line}\n\n"



    return cfg_str


def interval_time(timearr, interval):  #
    # Takes an array of string times with format 'hh:mm:ss' and returns an array of time strings x minutes earlier
    inTimeArr = ["Time"]
    for i in range(1, len(timearr)):  # iterates over array and appends new time to new array
        inTimeArr.append(str_to_time(timearr[i], interval))
    return inTimeArr


def get_date_time(matrix, index):
    # Creates an array with date times
    dateTime = []
    for i in matrix:
        dateTime.append(i[index])
    return dateTime


def copy_arry(array):
    # Returns a copy of an array
    new = []
    for i in array:
        new.append(i)
    return new


def get_date(arr, matrix):
    # Extracts the dates from date time array with form dd:mm:yy
    date = ["Date"]
    for i in range(1, len(matrix)):
        dat = arr[i][0:8]
        date.append(dat)
    return date


def get_time(arr, matrix):
    # Extracts the dates from date time array with form hh:mm:ss
    time = ["Time"]
    for i in range(1, len(matrix)):
        t = arr[i][9:len(arr[i])]
        if len(arr[i]) == 16:
            tim = f"{0}{t}"
        else:
            tim = t
        time.append(tim)
    return time
