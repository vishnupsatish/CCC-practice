#imports
import os
from io import StringIO
import sys
from datetime import datetime
rootdir ='.'  #set root directory
old_stdout = sys.stdout  #set the current print() function to variable to go back later
old_stdin = sys.stdin  #set the current input() function to variable to go back later
probs = ["J1", "J2", "J3", "J4", "J5"]  #create list with problem names
whatInput = input().split()  #get input for what years to run
whatInput = sorted(list(set(whatInput)))  #remove all duplicate elements and sorts
counter = 0  #counter of how many items are a valid year
listOfYears = []
if whatInput == "all":  #if user wants to test all years
    listOfYears = sorted(os.listdir(rootdir)) #get all of the years in the CCC folder sorted
else:  #if user has specific list of years to check
    for item in whatInput:  #iterate over all items in input
        if not item in os.listdir(rootdir):  #if one item is not a valid year, continue
            listOfYears = sorted(os.listdir(rootdir))  #set the list of years to check to all
            break  #no need to continue loop
        else:  #if the item is a valid year, continue
            counter += 1  #set counter of valid years + 1
            listOfYears.append(item)  #if the element exists, add to the list of years to iterate
    if len(listOfYears) == 0:  #if no element exists in list of years, continue
        listOfYears = sorted(os.listdir(rootdir))  #make the list of years all of the years (default)
open(rootdir + "/checker.txt", 'w').close()  #delete all of the contents of the checker file
record = open(rootdir + "/checker.txt", "w+")  #open the checker file
record.write("checker.py test on " + datetime.today().strftime('%Y-%m-%d') + "\n" + "\n")  #add the current date of the checker file
howManyFailed = []  #contains the names of the ifles where the test failed
for subdir in listOfYears:  #go through all of the years
    if os.path.isdir(subdir) and subdir[0] != ".":  #continue only if the item is directory and not a .git directory
        record.write(subdir + "\n" + "\n")  #add the current year to the checker file
        for prob in probs:  #go through the problem names (J1, J2, etc.)
            currentPath = rootdir + "/" + subdir + "/" + prob  #set current working path (ex: ./2019/J5)
            problemPath = currentPath + "/" + prob + ".py"  #set current Python file path (ex: ./2019/J5/J5.py)
            if os.path.isfile(problemPath):  #continue if the current Python file exists
                record.write(problemPath + "\n" + "\n")  #add the current Python file's path to checker file
                for user in sorted(os.listdir(currentPath + "/" + "Inputs")):  #iterate over all of the input files
                    if user != "." and user[0] != ".":  #continue if the input files are not OS files
                        result = StringIO()
                        sys.stdout = result  #redirect the output to the variable "result"
                        userInput = open(currentPath + "/" + "Inputs" + "/" + user)  #open the current input file (ex: ./2019/J5/Inputs/j5.01.in)
                        record.write("Input file: " + user + " at path " + currentPath + "/" + "Inputs" + "/" + user + "\n" + "\n")  #add the current input file to the checker file
                        sys.stdin = userInput  #redirect the user input to the contents of the current input file opened
                        run = open(problemPath, "r")  #open the current Python file to be run
                        try:
                            exec(run.read())  #try running the Python file with the current Input file as given input
                        except:
                            record.write("The program crashed" + "\n" + "\n")  #if error in Python program, add this to the checker file
                        userInput.close()  #close the current input file
                        expectedOutput = open(currentPath + "/" + "Outputs" + "/" + user[:-2] + "out")  #open the expected output file that matches to the input file
                        sys.stdout = old_stdout  #redirect the output to console to be shown (not used)
                        wantedOutput = str(expectedOutput.read())  #set variable to contents of the expected output file
                        givenResult = str(result.getvalue())  #set variable to the given output after running the Python program
                        if wantedOutput == givenResult:  #continue if the expected output and given output match
                            record.write("Given output matches wanted result, test PASSED" + "\n" + "\n")  #add that the outputs match and test passed to the checker file
                        else:  #continue if the expected output and given output do not match
                            record.write("Given output does NOT match, test FAILED" + "\n" + "\n")  #add that the outputs do not match and test failed to the checker file
                            howManyFailed.append(user[:-2] + "out")  #add the test that failed to the failed list
                        expectedOutput.close()  #close the output file
                        run.close()  #close the Python file
                if len(howManyFailed) == 0:  #continue if no tests failed
                    record.write("All Tests Passed" + "\n" + "\n")  #add that to the checker file
                else:  #if at least one test failed, continue
                    record.write("Failed:" + "\n")  #add the list of the expected output files where the given output did not match
                    for elem in howManyFailed:
                        record.write(elem + "\n")
                    record.write("\n")
                record.write("-----------------------------------------" + "\n\n")
                howManyFailed = []  #reset the list of tests that failed to nothing
            else:  #if there is no Python file, continue
                record.write(prob + " with path of " + problemPath + " Not found or does not exist." + "\n" + "\n")  #add to the file that there is no problem file
                record.write("-----------------------------------------" + "\n\n")
record.close()  #close the checker file