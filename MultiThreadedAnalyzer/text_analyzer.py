import time

# importing the threading module 
import threading 

# Returns number of words in string 
def countWords(string): 
    print('Starting count words thread...')
    state = OUT 
    wc = 0
  
    # Scan all characters one by one 
    for i in range(len(string)): 
  
        # If next character is a separator,  
        # set the state as OUT 
        if (string[i] == '\n' or string[i] == '\t' or string[i] == ' ' or string[i] == '?' or string[i] == '!' or string[i] == '.' or string[i] == ',' or string[i] == ';' ): 
            state = OUT 
  
        # If next character is not a word  
        # separator and state is OUT, then  
        # set the state as IN and increment  
        # word count 
        elif state == OUT: 
            state = IN 
            wc += 1
  
    # Return the number of words 
    print("No. of words : " + str(wc)) 
    return




# Returns number of sentences in string
def countSentences(string): 
    print('Starting count sentences thread...')
    state = OUT
    sc = 0
  
    # Scan all characters one by one 
    for i in range(len(string)): 
  
        # If next character is a sentence ender,  
        # set the state as IN 
        # also considers two sentence enders in a row
        if (string[i] == '?' or string[i] == '!' or string[i] == '.'):
            state = IN

        # Option to add extra logic for Mr. /Mrs. 
  
        # If next character is not a sentence ender
        # then
        # set the state as OUT and increment  
        # sentence count 
        elif (state == IN):
            state = OUT 
            sc += 1
  
    # Return the number of sentences 
    print("No. of sentences : " + str(sc)) 
    return 


# Returns number of characters in string(excluding spaces)
def countCharacters(string): 
    print('Starting count characters thread...')
    cc = 0
    sc = 0
  
    # Scan all characters one by one 
    for i in range(len(string)): 
  
        # If next character is a separator,  
        # count separately
        if (string[i] == '\n' or string[i] == '\t' or string[i] == ' '): 
            sc += 0

        # If next character is not a seperator 
        # increment count
        else:
            cc += 1
  
    # Return the number of character
    print("No. of characters : " + str(cc))
    return


 
# Driver Code 
start = time.perf_counter()
fileObject = open("piney.txt", "r")
data = fileObject.read()

OUT = 0
IN = 1

# creating threads
t1 = threading.Thread(target=countWords, args=(data,)) 
t2 = threading.Thread(target=countSentences, args=(data,))
t3 = threading.Thread(target=countCharacters, args=(data,))

# starting thread 1 
t1.start() 
# starting thread 2 
t2.start() 
# starting thread 3
t3.start() 

# wait until thread 1 is completely executed 
t1.join() 
# wait until thread 2 is completely executed 
t2.join() 
# wait until thread 3 is completely executed 
t3.join() 
finish = time.perf_counter()

# all threads completely executed 
print(f'Finished in {round(finish-start,10)} seconds(s)')




