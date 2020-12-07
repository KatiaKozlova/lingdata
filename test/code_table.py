import string
with open('ozhegov.tsv', 'r', encoding='utf-8') as ozhegov:
    with open('new_ozhegov.tsv', 'a', encoding='utf-8') as new_ozhegov:
        for line in ozhegov:
            line = line.split('\t')
            definition = line[1].split()
            if definition[0].startswith('\=') or definition[0].startswith('\+') or definition[0].startswith('<'):
                if len(definition) != 1:
                    definition[0] = definition[1]
            if definition[0].endswith(tuple(string.punctuation)):
                definition[0] = definition[0].strip(string.punctuation)
            new_line = line[0] + '\t' + definition[0] + '\n'
            new_ozhegov.write(new_line)


