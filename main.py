# Made by Roshan Prashant Bara
# GitHub link: https://github.com/roshanbara
# ******CAUTION: The owner of this code is responsible for deletion of any file/folder or any damage caused due to execution of this code******
# To run the code please follow the Readme on GitHub
# DISCLAIMER: This code has just been made as a self-project, just to apply what has been learnt and the creator has no intention of illegal usage

# CODEFORCES SCRAPPER

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import os.path
from os import path
import shutil

driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')
# Enter Contest number
print("Enter contest Number: ")
con = input()
driver.get("https://codeforces.com/contest/" + con)

# If the contest directory already exists it is deleted and a new one is made
if(path.isdir(os.getcwd() + "/" +con)):
    shutil.rmtree(os.getcwd() + "/" +con)
os.mkdir(con)
os.chdir(os.getcwd() + "/" +con) 
pathcwd = os.getcwd()

rows = driver.find_elements_by_xpath("//table[@class='problems']/tbody/tr")
num = len(rows)
for i in range(2 , num+1):
    path1  = "//table[@class='problems']/tbody/tr["+str(i)+"]/td[1]/a"
    temp0 = driver.find_element_by_xpath(path1)
    name = temp0.text
    # print(name)
    #creating problem dir
    os.mkdir(name)
    #moving to problem dir
    os.chdir(os.getcwd()+"/" +name)
    # Navigating to the problem
    linktxt = driver.find_element_by_xpath(path1)
    linktxt.click()

    pstmt = driver.find_element_by_class_name("problem-statement")
    pstmt.screenshot("problem.png")
    #finding no. of input-output examples
    inpt = driver.find_elements_by_tag_name("pre")    
    num1 = len(inpt)

    # print(num1)
    #iterating over all examples
    for j in range(0, num1):
        if(j%2==0):
            f = open("input"+str((j//2)+1)+".txt", "a")
            f.write(inpt[j].text)
            f.close()
        else:
            t = open("output"+str((j//2)+1)+".txt", "a")
            t.write(inpt[j].text)
            t.close()

    #moving back in webdriver
    driver.back()
    #changing dir back to contest dir
    os.chdir(pathcwd)

# All tasks done
print("Tasks done!")