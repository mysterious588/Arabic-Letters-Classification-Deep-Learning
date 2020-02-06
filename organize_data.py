import os
import shutil
import time

string = 'ain alef beh dad dal feh ghain hah heh jeem kaf khah lam meem noon qaf reh sad seen sheen tah teh thal theh waw yeh zah zain'.split()
root_folder = os.getcwd()
print('you must place this program in a directory with your train and test folders unzipped in the same place')
print('you are currently in: ' + root_folder)
print()
print('finding test & data....')

if('test' and 'train' in os.listdir()):
    print('Success, folders found!')
else:
    print('failed, place the file in the same folder with the test/train folders and try again')
    time.sleep(5)
    exit()


try:
    print (os.chdir(root_folder + '/train'))
except:
    print('can not go to that folder')
# make directories
for directory in string:
    try:
    # Create target Directory
        os.mkdir(directory)
        print("Directory " , directory ,  " Created ") 
    except FileExistsError:
        print("Directory " , directory ,  " already exists")

images = os.listdir(os.getcwd())
for image in images:
    for i in range(len(string)):
        if (image[:3] == string[i][:3]):
            try:
                shutil.move(image, string[i])
            except:
                print('error occured with ' + image)
else:
    print('traning data completed')

# make directories
for directory in string:
    try:
    # Create target Directory
        os.mkdir(directory)
        print("Directory " , directory ,  " Created ") 
    except FileExistsError:
        print("Directory " , directory ,  " already exists")

try:
    print (os.chdir(root_folder + '/test'))
except:
    print('can not go to that folder')
    
for directory in string:
    try:
    # Create target Directory
        os.mkdir(directory)
        print("Directory " , directory ,  " Created ") 
    except FileExistsError:
        print("Directory " , directory ,  " already exists")

images = os.listdir(os.getcwd())
for image in images:
    for i in range(len(string)):
        if (image[:3] == string[i][:3]):
            try:
                shutil.move(image, string[i])
            except:
                print('error occured with ' + image)
else:
    print('testing data completed')


