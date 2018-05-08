import csv
with open('spam.csv', newline= '' ) as f:
    data = csv.reader(f)
    data_n = list(data)
spam_train = {}
ham_train = {}
hamcount=0
spamcount=0
ham_sum = 0
spam_sum = 0
ham_prob = {}
spam_prob = {}

spam_test = {}
ham_test = {}
test_prob_spam = 1
test_prob_ham = 1

    #l = list(map(tuple, reader))
for i in range(1,len(data_n)):
    for word in data_n[i][0].split():
        if word == "ham":
            hamcount=hamcount+1
        else:
            spamcount+=1

for i in range(1,len(data_n)):
    for word in data_n[i][0].split():
        if word=="ham":
            
            for word in data_n[i][1].split():
                if word in ham_train:
                    ham_train[word] +=1
                    ham_sum = ham_sum+ham_train[word]
                    ham_prob[word] = ham_train[word]/ham_sum
                else:
                    ham_train[word] = 1
                    ham_sum = ham_sum+ham_train[word]
                    ham_prob[word] = ham_train[word]/ham_sum
                    
                    
                    
        else:
            for word in data_n[i][1].split():
                if word in spam_train:
                    spam_train[word] +=1
                    spam_sum = spam_sum+spam_train[word]
                    spam_prob[word] = spam_train[word]/spam_sum
                else:
                    spam_train[word] = 1
                    spam_sum = spam_sum+spam_train[word]
                    spam_prob[word] = spam_train[word]/spam_sum
                    


wish = "Watching telugu movie..wat abt u?"

for word in wish.split():
    if word in ham_train:
        continue
    else:
        ham_train[word] = 1
        ham_sum = ham_sum+ham_train[word]
        ham_prob[word] = ham_train[word]/ham_sum
        hamcount = hamcount+1
for word in wish.split():
    if word in spam_train:
        continue
    else:
        spam_train[word] = 1
        spam_sum = spam_sum+spam_train[word]
        spam_prob[word] = spam_train[word]/spam_sum
        spamcount+=1


spam_prob_new = spamcount/(spamcount+hamcount)
ham_prob_new = 1-spam_prob_new
            
for word in wish.split():
        test_prob_spam = test_prob_spam*spam_prob[word]
    
        test_prob_ham = test_prob_ham*ham_prob[word]

        
        
test_prob_spam = test_prob_spam*spam_prob_new
test_prob_ham = test_prob_ham*ham_prob_new
            
if test_prob_spam>test_prob_ham:
    print("mail is spam")
else:
    print("mail is ham")
                
                
                
                
            
        
        
    
    

#print(data_n)





