def write(file_path, data):
    try:
        with open(file_path, 'a') as fw:
            fw.write(data)
    except FileNotFoundError as e:
        print('File can t be open -> {e}')