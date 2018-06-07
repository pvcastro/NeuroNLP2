def add_starting_index(ifile, ofile):
    with open(ifile, 'r') as reader, open(ofile, 'w') as writer:
        prev = None
        skip_next = False
        for line in reader:
            if skip_next:
                skip_next = False
                continue
            line = line.strip()
            docstart = line.startswith('-DOCSTART-')
            if docstart:
                skip_next = True
            if len(line) == 0 or docstart:
                prev = None
                if not docstart:
                    writer.write('\n')
                continue

            tokens = line.split()

            if prev is None:
                prev = 1
            else:
                prev += 1

            indexed_tokens = [str(prev)] + tokens

            # print tokens
            writer.write(" ".join(indexed_tokens))
            writer.write('\n')


if __name__ == '__main__':
    add_starting_index('data/conll2003/english/eng.train.bios', 'data/conll2003/english/eng.train.bios.conll')
    add_starting_index('data/conll2003/english/eng.testa.bios', 'data/conll2003/english/eng.testa.bios.conll')
    add_starting_index('data/conll2003/english/eng.testb.bios', 'data/conll2003/english/eng.testb.bios.conll')
