def count_words(file_name, output_amount):
        filename = open(file_name, "r", encoding="utf-8-sig")
        infile = filename.read()
        words = infile.split()
        count = {}

        for word in words:
            word = word.strip('!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~').lower()
            count[word] = count.get(word, 0) + 1

        items = list(count.items())
        items.sort(key=lambda x: x[1], reverse=True)

        for i in range(output_amount):
            word, count = items[i]
            print("{0:<15}{1:>5}".format(word, count))
