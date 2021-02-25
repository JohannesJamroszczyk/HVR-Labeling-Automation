def mk_text_file(name):

    # This read in or makes a new text based file

    cfg_file = open(name, "w+")  # either accesses an existing file or creating a new one
    return cfg_file

def csv_to_matrix(location):
    from csv import reader
    with open(location, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        return list(csv_reader)