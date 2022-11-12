'''

'''
import os

if __name__ == '__main':
    path = './Core/Src'  # here is where main.c is generated and the last main.cpp is
    filename_c = 'main.c'
    filename_cpp = 'main.cpp'

    # read in lines of files
    c_lines = []
    cpp_lines = []
    with open(path+filename_c, 'r') as f:
        c_lines = f.readlines()
    with open(path+filename_cpp, 'r') as f:
        cpp_lines = f.readlines()

    should_copy=False
    no_copy_user_code=False
    same_lines=False
    
    with open(path+filename_c, 'w') as fc:
        # write all generated code into main.c
        for c_line in c_lines:
            # copy cpp lines after every USER CODE BEGIN statement
            if 'USER CODE BEGIN' in c_line:
                fc.write(c_line) # write this line into file
                no_copy_user_code=True # do not copy lines from c after USER CODE BEGIN
                cpp_line2copy = []
                for cpp_line in cpp_lines:
                    if c_line == cpp_line:
                        should_copy = True
                        continue
                    if should_copy == True and 'USER CODE END' in cpp_line:
                        should_copy = False
                        break
                    if should_copy == True:
                        cpp_line2copy.append(cpp_line)
                [fc.write(cpp_line2add) for cpp_line2add in cpp_line2copy]
            # can copy lines after USER CODE END
            if 'USER CODE END' in c_line:
                no_copy_user_code=False
            if not no_copy_user_code:
                fc.write(c_line)

    # delete main.cpp then rename main.c to main.cpp
    os.remove(path+filename_cpp)
    os.rename(path+filename_c, path+filename_cpp)
