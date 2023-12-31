# myPythonLessonStory
A repository documenting my Python learning journey during college.  
一个记录我大学期间Python学习历程的仓库.

## Summarize 学习总结
1. When you encounter a problem you don’t understand, you can first ask ChatGPT to try to solve it; after it gives the code, you can ask it to comment on the code and ask what a certain line of code means. This will greatly improve your independent learning efficiency. For details, please refer to [this article](https://gloridust.xyz/%E6%8A%80%E6%9C%AF/2023/08/24/studywithgpt.html) in my blog.  
遇到不懂的问题时，可以先询问ChatGPT来尝试解决；它给出代码后，你可以要求它注释代码，并且询问某一行代码什么意思。这样会使你的自主学习效率大大提升。具体可以参考我博客里的[这篇文章](https://gloridust.xyz/%E6%8A%80%E6%9C%AF/2023/08/24/studywithgpt.html)。  


## Log 日志

### 2023-10-04
#### [getInt.py](/getInt.py)
This simple Python program allows the user to enter an integer up to three digits and then extract and print out the hundredth digit of that integer. If the user input does not meet the requirements, the program will give corresponding prompts.  
这个简单的 Python 程序允许用户输入一个三位以上的整数，然后提取并打印出该整数的百位以上的数字。如果用户输入不符合要求，程序将给出相应的提示。


### 2023-09-25
Today, I created this repository and compiled the Python code from the past few days.  
今天，我创建了这个仓库，将前几天的Python代码整理了进来。  
#### [tkGUI-guessNum.py：](/tkGUI-guessNum.py)  
This is a code from my classmate, and he asked me to help him modify the code. It was both his and my first time trying to write a GUI in Python. His problem is that the GUI window is created, but the command line is still used to input & print content.  
这是一个来自我同学的代码，他让我帮他修改代码。我和他都是第一次尝试用Python写GUI。他的问题在于创建了GUI窗口，但是仍在使用命令行来Input&Print内容。  

    # suggestion:
    # 1. If you plan to implement this game in a GUI interface, consider replacing the user input part with GUI elements instead of using text input and printing messages.
    # 2. For Tkinter GUI, you can create an input box and a text label to handle user input and display messages instead of using command line input and print.
    # 3. If the user enters a non-integer, the code will throw an exception. Exception handling can be added to handle this situation to ensure that the program does not crash.
<!--  -->
    # 建议：
    # 1. 如果你打算在GUI界面中实现这个游戏，可以考虑将用户输入的部分替换为GUI元素，而不是使用文本输入和打印消息。
    # 2. 对于Tkinter GUI，你可以创建一个输入框和一个文本标签来处理用户输入和显示消息，而不是使用命令行的input和print。
    # 3. 如果用户输入非整数，代码会引发异常。可以添加异常处理来处理这种情况，以确保程序不会崩溃。


#### [guessName.py：](/guessName.py)
A simple exercise, mainly practicing some basic equality tests.  
一个简单的练习，主要练习一些基础的相等性检验。  

    # NOTE: Use the double equal sign (==) to compare for equality
<!--  -->
    # 注意：使用双等号（==）来比较相等性

#### [print(0).py：](/print(0).py)
Simple exercises on the logic of the inequality sign (!=).  
简单的关于不等号(!=)逻辑的练习。