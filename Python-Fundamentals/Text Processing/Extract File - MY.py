line = input().split(chr(92))
needed_fail = line[-1].split('.')
file_name = needed_fail[0]
file_extension = needed_fail[-1]
print(f'File name: {file_name}\nFile extension: {file_extension}')

