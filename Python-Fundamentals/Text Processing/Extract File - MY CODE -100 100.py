line = input().split(chr(92))
file_name, file_extension = line[-1].split('.')

print(f'File name: {file_name}\nFile extension: {file_extension}')