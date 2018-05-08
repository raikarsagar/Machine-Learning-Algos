import numpy as np
from sklearn import datasets
import math

def eucl_dist(pt_a,pt_b,l):
    distance = 0
    for i in range(1,l):
        distance = distance+math.pow((pt_a[i]-pt_b[i]),2)
    return math.sqrt(distance)
        
digits = datasets.load_digits()
images_and_labels = list(zip(digits.images, digits.target))
n_samples = len(digits.images)

def MyFn(a):
    return a[0]

K = 1
train_end = 1000
test_begin = 1200
train_data = digits.data[0:(train_end),:]
test_label = digits.target[test_begin:len(digits.target)]
test_image = digits.data[test_begin:len(digits.data),:]

euc_test = np.zeros(len(train_data))
euc_test_label = np.zeros(len(train_data))
dist_tuple = []
count_label = 0

for j in range(0,len(test_image)):
    euc_test_sorted = []
    euc_test_f = []
    dist_tuple = []
    for i in range(0,len(train_data)):
        
        euc_test[i] = eucl_dist(test_image[j],train_data[i],64)
        euc_test_label[i] = images_and_labels[i][1]
        dist_tuple.append((euc_test[i],train_data[i],euc_test_label[i]))
    
    euc_test_sorted = sorted(dist_tuple,key = MyFn)
    euc_test_f = euc_test_sorted[0:K]
    count = np.full((10,1),0,dtype=int)
    label = np.array([[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]])
    count = np.concatenate((count,label),axis = 1)
    for k in range(0,K):
        if(euc_test_f[k][2]==0):
            count[0][0] +=1
        if(euc_test_f[k][2]==1):
            count[1][0] += 1
        if(euc_test_f[k][2]==2):
            count[2][0]+=1
        if(euc_test_f[k][2]==3):
            count[3][0]+= 1        
        if(euc_test_f[k][2]==4):
            count[4][0]+=1
        if(euc_test_f[k][2]==5):
            count[5][0]+=1
        if(euc_test_f[k][2]==6):
            count[6][0]+=1
        if(euc_test_f[k][2]==7):
            count[7][0]+=1
        if(euc_test_f[k][2]==8):
            count[8][0]+=1
        if(euc_test_f[k][2]==9):
            count[9][0]+=1
    final_count =  count[:,0].argsort()
    #final_count = count[count[:,0].argsort()]
    final = count[final_count[9],1]
    expected_label = test_label[j]
    print("expected_label:",expected_label)
    print("predicted:",final)
    if(expected_label==final):
        count_label+=1
    
accuracy = count_label/len(test_image)
print("accuracy=",accuracy)