import ner

def read_text_file_class(filename):
    data = {}
    current_key = None

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:

        if line.startswith('\t'):  # 带有缩进的行作为值
            if current_key is not None:
                line = line.strip()
                data[current_key].append(line)
        else:  # 没有缩进的行作为键

            if '总频次' in line:
                total_frequency = line.split('总频次：', 1)[1]  # 提取总频次后面的数值部分

                keyword = "总频次"
                line = line.split(keyword)[0].strip() + '|' + str(total_frequency)

            line = line.strip()
            current_key = line
            data[current_key] = []

    return data


filename = 'info.txt'
result = read_text_file_class(filename)
print(result)

# # 写入结果到文本文件
output_filename = 'output2.txt'  # 替换成你想要输出的文件名
with open(output_filename, 'w', encoding='utf-8') as output_file:
    for key, value in result.items():
        count = int(key.split('|')[1])

        if count < 10:
            ner.extract_loc()
            output_file.write(f'Key: {key}\n')
            output_file.write('Value:\n')
            for line in value:
                output_file.write(line + '\n')
            output_file.write('\n')
