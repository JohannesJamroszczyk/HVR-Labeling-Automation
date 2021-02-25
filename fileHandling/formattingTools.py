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
