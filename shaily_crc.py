



import keras
from keras.layers import BatchNormalization
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.optimizers import SGD
import numpy as np
np.random.seed(132)





import numpy as np
def xor(a,b):
    result=[]
    for i in range(1,len(b)):
        if a[i]==b[i]:
            result.append('0')
        else :
            result.append('1')

    return(''.join(result)) 
    
     
    ### Performs modulo-2 division function
def mod2div(divident,divisor):
    pick = len(divisor)
    tmp=divident[0:pick]
    while pick < len(divident):
        
        if tmp[0]=="1":
            tmp=str(xor(divisor,tmp)) + str(divident[pick])
          
        else:
             tmp=str(xor("0"*pick,tmp)) + str(divident[pick])
            

        pick +=1
    
    if tmp[0]=="1":
        tmp=xor(divisor,tmp)
                       
    else:
                            
        tmp=xor("0"*pick,tmp)
                                
    checkword = tmp

    return checkword

def encodeData(data,key):
    l_key=len(key)
                            
                    
   # appends n-1 zeroes at end of Data
    appended_data = data + "0"*(l_key-1)
    remainder = mod2div(appended_data,key)
    rem.append((remainder))
    # append remainder in the Original data
    codeword=data+remainder
    return codeword

encoded_data=[]
data=[]
rem=[]


n = 16 
for i in range(10000):
    b = bin(i)[2:]
   
    l = len(b)
    b = str(0) * (n - l) + b
    key="111010101"
    data.append(list(b))
  
   
    
    ans=encodeData(b,key)
    encoded_data.append(ans)
    B=np.array(data)

s=[]
for i in range(10000):
    s.append(list(rem[i]))
   
print(s)
print(data)

X=np.array(data)
Y=np.array(s)
print(X)
print(Y)

model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(16,)))
model.add(Dropout(0.25))
model.add(Dense(64, activation='relu'))
model.add(Dense(8))
model.summary()


model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])
model.fit(X,Y,epochs=200,verbose=1,batch_size=50,validation_split=0.2,shuffle=True)

