def transform(ifile, ofile):
    with open(ifile, 'r') as reader, open(ofile, 'w') as writer:
        prev = 'O'
        for line in reader:
            line = line.strip()
            if len(line) == 0:
                prev = 'O'
                writer.write('\n')
                continue

            tokens = line.split()
            # print tokens
            label = tokens[-1]
            if label != 'O' and label != prev:
                if prev == 'O':
                    label = 'B-' + label[2:]
                elif label[2:] != prev[2:]:
                    label = 'B-' + label[2:]
                else:
                    label = label
            writer.write(" ".join(tokens[:-1]) + " " + label)
            writer.write('\n')
            prev = tokens[-1]


if __name__ == '__main__':
    transform('data/conll2003/english/eng.train', 'data/conll2003/english/eng.train.bios')
    transform('data/conll2003/english/eng.testa', 'data/conll2003/english/eng.testa.bios')
    transform('data/conll2003/english/eng.testb', 'data/conll2003/english/eng.testb.bios')
