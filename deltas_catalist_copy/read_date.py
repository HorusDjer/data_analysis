path = '/Users/ejikeobineme/Documents/data_analysis/deltas_catalist_copy/catalist_import_log2.txt'

with open(path, 'r', encoding='utf-8') as file_object:
    contents = file_object.readlines()
    print(type(contents), '\n')
    print(contents)
