# STM32CubeMX C to C++ exporter

STM32Cube IDE is able to make a C++ project. However, even with these settings, the CubeMX tool generates a main.c every time there is a change in peripheral configurations.
Copying user code from the old main.cpp to the newly generated main.c can become annoying after a while.
So I wrote a simple python script to overcome this problem.  

## How it works

The script copies user code from the old main.cpp to the newly generated main.c.
It then deletes main.cpp and renames main.c to main.cpp. 
After these steps, .cpp will be the main file, when compiling the project. Hooray, problem solved! 🥳

## Usage

1. Copy the python file to the base folder of STM32Cube C++ project.

2. After making a change in MX graphical interface, that generates new code, run the python script.

3. Enjoy the result of your work!