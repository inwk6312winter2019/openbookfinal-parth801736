#fout1=open("Book1.txt")
#fout2=open("Book2.txt")
#fout3=open("Book3.txt")
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


	return resp
print(unique_words('Book1.txt','Book2.txt','Book3.txt'))

