import os



def create_folders(path):
    if not os.path.exists(path):
        os.makedirs(path)


def write_to_file(file_name , data, path):
    create_folders(path)
    file_new = open(path + "\\" + file_name, 'w')
    print(data, file=file_new)
    file_new.close()
