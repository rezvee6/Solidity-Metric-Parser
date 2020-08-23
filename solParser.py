# Solidity Parser
# File contains helper functions to parse and calculate understandability metrics
# Author: Reezvee Sikder
# Date: 04/08/2020

import inflection
import re

def removeComments(code):
    """ Remove comments from code"""
    code = str(code)
    # # remove // comments
    code = re.sub(r'(?m)^ *//.*\n?', '', code)
    code = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,code)
    return code


def removeEmptyLine(code):
    """ Removes empty whitelines in code string"""
    return re.sub(r'^$\n', '', code, flags=re.MULTILINE)


def insideFunction(code):
    """ Return code contents from inside a function"""
    return code[code.find("{")+1:code.find("}")]


def codeToArray(code):
    """Splits code string into array separated by newline character"""
    convList = []
    code = code.split("\n")
    for element in code:
        convList.append(element.strip())
    return convList


def load_words():
    """ Helper function which loads english word dictionary"""
    #http://www.mieliestronk.com/wordlist.html
    with open('words_alpha2.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


def splitLine(line):
    """Splits a line of words into an array, and returns array"""
    line =  re.split(' ',line)
    return list(filter(None, line))


def wordsFromLine(line):
    """ Returns a line with only str words"""
    return line.replace('_',' ').replace('[',' ').replace(']',' ').replace(',',' ').replace('=',' ').replace('.',' ').replace('(',' ').replace(')',' ').replace('{',' ').replace('}',' ').replace(';',' ').replace(':',' ')


def solKeywordFilter(List):
    """ Filters out unwanted keywords in a comment word array"""
    removeAr = ["uint","uint256","uint8",">","<","ERC677Token","ERC20","ERC677Receiver","*/","*","/*","/**","||","/","@param","//","@dev","%","+","-","&&","@return","ERC20Basic","ERC677","!","return","18","mul","a","b","c","0"]
    for word in list(List):
        if word in removeAr:
            List.remove(word)
    
    return list(dict.fromkeys(List))


def similarityScore(arrayOne, arraytwo):
    """returns similarity score of two word arrays, similarity being matching english words"""
    return set(arrayOne) & set(arraytwo)


def pragmaRemover(code):
    """ function which removes pragma from solidity file"""
    return re.sub(r'^pragma.*\n?', '', code, flags=re.MULTILINE)

def libraryRemover(code):
    """ function which removes pragma"""
    return re.sub(r'^library.*\n?', '', code, flags=re.MULTILINE)


def extractComments(code):
    """ Function which returns a list of commented lines from a list of code lines"""
    commentBank = []
    itemsList = ["//", "#", "/*", "*/", "*"]
    for item in itemsList:
        for line in code:
            if item in line:
                commentBank.append(line)
    return commentBank

def camelCase(List):
    """Returns list containing camelcase words"""
    camelCaseList = []
    nonCamelCaseList = []
    for s in List:
        if s != s.lower() and s != s.upper() and "_" not in s:
            camelCaseList.append(s)
        else:
            nonCamelCaseList.append(s)

    return camelCaseList, nonCamelCaseList 

# def camlCase(List):
#     newList = []
#     for s in List:
#         if inflection.camelize(s, uppercase_first_letter=True) == s:
#             newList.append(s)
#     return newList