def extract(data_array, start, end, output_file_name):
    file = open(output_file_name,"wb")
    file.write(data_array[start:end])
    file.close()
    return