def main():
   
    infile = open('clients.txt','r')
    count = 0

    for line in infile: 
        count += 1
        print(str(count),'. ', line,sep='')
      
        
main()