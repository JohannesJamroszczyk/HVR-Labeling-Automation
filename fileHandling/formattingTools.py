def str_to_time(stri, interval):
    timeInt = int(stri[0:2]) * 60 + int(stri[3:5]) - interval
    hours = int(timeInt / 60)
    minutes = timeInt % 60
    if len(str(hours)) == 1:
        hourStr = "0" + str(hours)
    else:
        hourStr = str(hours)
    if len(str(minutes)) == 1:
        minutesStr = "0" + str(minutes)
    else:
        minutesStr = str(minutes)
    time = f"{hourStr}:{minutesStr}:{stri[6] + stri[7]}"
    return time


def popped_matrix(matrix, index):
    # accepts a matrix and an index and returns a matrix where
    # the value at the index of all sublists is popped

    for i in matrix:  # pops values at indicated indexes
        i.pop(index)
    return matrix


def matrix_to_config(matrix):
    # Converts matrices to a label-config file for VU-DAMS software
    configString = ""                                       # base content
    number = 10                                             # starting value for numbering of category labels
    for i in range(0, len(matrix[0])):                      # category level
        configString += f"#{str(matrix[0][i])}\n"
        for j in range(1, len(matrix)):                     # label level
            configString += f"{number} {matrix[j][i]}\n"
        configString += "\n"
    return configString


def interval_time(timearr, interval):
    inTimeArr = ["Time"]
    for i in range(1, len(timearr)):
        inTimeArr.append(str_to_time(timearr[i], interval))
    return inTimeArr


def matrix_to_label(matrix, timearr, intervaltimearr, datearr, version, lablename):
    cfg_str = f"Label Data File version {version}\n" \
              f"{lablename} {datearr[1]}/{timearr[1]} {datearr[len(datearr)-1]}/{timearr[len(timearr)-1]}\n" \
              f" Begin date/time    End date/time    Labelcode\n\n"
    for i in range(1, len(matrix)):
        cfg_str += f" {datearr[i]}/{intervaltimearr[i]}  {datearr[i]}/{timearr[i]}\n\n"
    return cfg_str

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
    # Extracts the dates from date time array with form dd%m%yy
    date = ["Date"]
    for i in range(1, len(matrix)):
        dat = arr[i][0:8]
        date.append(dat)
    return date


def get_time(arr, matrix):
    time = ["Time"]
    for i in range(1, len(matrix)):
        t = arr[i][9:len(arr[i])]
        if len(arr[i]) == 16:
            tim = f"{0}{t}"
        else:
            tim = t
        time.append(tim)
    return time
