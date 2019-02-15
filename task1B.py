def most_common(file1,file2,file3):
	
        with open(file1 'r') as fout1:
             return unique_words(fout1)

        with open(file1 'r') as fout2:
             return unique_words(fout2)

        with open(file1 'r') as fout3:
             return unique_words(fout3)

 

       for line in w:
                res = line.lower().strip(string.punctuation + string.whitespace).split()
                n_res += res

        count = {}
        for word in n_res:
                count[word] = count.get(word, 0) + 1

        s_count = sorted([(v, k) for k, v in count.items()], reverse=True)
        mostfreq_20 = s_count[:20]

        for count, word in mostfreq_20:
                print(word + " : " + str(count))

counter()

most_common('Book1.txt','Book2.txt','Book3.txt')
