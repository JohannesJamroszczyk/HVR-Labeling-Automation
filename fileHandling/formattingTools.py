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
    date = ["Time"]
    for i in range(1, len(matrix)):
        dat = arr[i][0:8]
        date.append(dat)
    return date


def get_time(arr, matrix):
    time = ["Date"]
    for i in range(1, len(matrix)):
        t = arr[i][9:len(arr[i])]
        if len(arr[i]) == 16:
            tim = f"{0}{t}"
        else:
            tim = t
        time.append(tim)
    return time
