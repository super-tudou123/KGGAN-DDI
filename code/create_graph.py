# 读取包含三元组的文件
with open('../data/DRKG1/ddi_map.tsv', 'r') as file:
    triples = file.readlines()

# 去除关系，只保留头实体和尾实体
filtered_triples = []
for triple in triples:
    parts = triple.strip().split()
    if len(parts) == 3:
        filtered_triples.append(parts[0] + ' ' + parts[2])

# 将处理后的数据写入新文件
with open('../data/DRKG1/drkg', 'w') as file:
    for triple in filtered_triples:
        file.write(triple + '\n')