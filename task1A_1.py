"""Sub task1A_1 Function name: unique_words - Returns: A list containing only one copy of the words. (for example, if the word "it"
 appears 50 times in the book, there should be only one "it" in the tuple)"""

#fout1=open("Book1.txt")
#fout2=open("Book2.txt")
#fout3=open("Book3.txt")
import string

def unique_words(file1,file2,file3): #book passed as function's argument

    with open(file1 'r') as fout1:
        return unique_words(fout1)

    with open(file1 'r') as fout2:
        return unique_words(fout2)

    with open(file1 'r') as fout3:
        return unique_words(fout3)

	resp=[]

	for item in file1:
            item=item.split()
	    
            if item not in resp:
	       item.append(item)

        for item in file2:
            item=item.split()

            if item not in resp:
               item.append(item)
        for item in file3:
            item=item.split()

            if item not in resp:
               item.append(item)

	return resp

"""Sub task1A_2 Function name: count_the_article - Returns: An Integer that counts the total 
number of words that are in the list.
 => ["a", "the", "at", "run", "to","and","are","or","for","an","this"]"""

lst=["a", "the", "at", "run", "to","and","are","or","for","an","this"]

def count_the_article(lst): 
        #count = 0
	n_res = []

	for line in lst:
		res = line.lower().strip(string.punctuation + string.whitespace).split()
		n_res += res

	count = {}
	for words in n_res:
		count[words] = count.get(words, 0) + 1

	no_list = list(set(count.keys()) - set(word_list))

	return no_list
"""Sub Task1A_3 Function name: sorted_words - Returns: A list containing the 
words in the book in descending order based on character count. """

def sorted_words(file1,file2,file3):
	for line in file:
		line=line.split()
		line.sort()
		print(line)

#print(count_the_article(lst))
print(unique_words('Book1.txt','Book2.txt','Book3.txt'))
print(count_the_article(lst))
print(sorted_words('Book1.txt','Book2.txt','Book3.txt'))


