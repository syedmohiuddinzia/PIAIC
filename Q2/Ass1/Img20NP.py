def LibImport():
    import matplotlib.pyplot as plt 
    import matplotlib.image as mpimg
    from PIL import Image
    import numpy as np
    import os, os.path

def main():
    dir = "photos" #20 Images of different sizes stored here
    ReqArr = np.zeros([l,200,200,3]) #Required 4-D Array
    size_200 = (200,200) #200 width by 200 height
    print(ReqArr.shape)
    
    LibImport()
    LengthFiles()
    NameFiles()
    ResizeFiles()    
    
def LengthFiles():
    onlyfiles = next(os.walk(dir))[2] #Finds all files in directory "photos"
    l = len(onlyfiles) #Length of all files found
    print(l)
    
def NameFiles():
    for dirName, subdirList, fileList in os.walk(dir): #Finds names in directory "photos"
        print('Found directory:' , dirName)
        print('Found fileList:' , fileList)

def ResizeFiles():
    D4Arr = [] #Empty 4-D List
    for fname in fileList: #For particular file name
        #print('Found fname:' , fname)
        
        if fname.endswith(".jpeg"): #Files that ends with .jpeg
            i = Image.open(fname) #Opens that files data in variable
            fn, fext = os.path.splitext(fname) #Separates name and extension

            npArrOld = np.array(i) #Coverts data into array    
            i = i.resize(size_200) #Resizes the file data and saves in variable
            i.save("cars/{}{}".format(fn, fext))  #Saves the new data in 'cars'
            npArrNew = np.array(i) #Coverts new data into array

            #plt.imshow(i) #Plots image
            #plt.show(i) #Plots image
            
        D4Arr.append(npArrNew) #Appends 4-D List
    ndArr = np.array(D4Arr) #Converts 4-D List into 4-D array
    print(ndArr.shape) #Shape of 4-D Array
    
if __name__ == '__main__':
    main()
