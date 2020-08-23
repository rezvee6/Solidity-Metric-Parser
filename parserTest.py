from solParser import *

import glob, os, csv, time      

def getSolFileList():
    solFiles = []
    os.chdir("./contracts/")
    for file in glob.glob("*.sol"):
        solFiles.append(file)
    return solFiles

def metricOne(contents):
    """ Returns % of full identifiers in code, excluding comments"""
    
    countBank = []
    wordBank = []
    contents = removeComments(contents)
    contents = removeEmptyLine(contents)
    contents = pragmaRemover(contents)
    contents = libraryRemover(contents)
    
    contents = codeToArray(contents)
    for line in contents:
        parseLine = wordsFromLine(line)
        processLine = splitLine(parseLine)
        for word in processLine:
            wordBank.append(word)

    wordBank = solKeywordFilter(wordBank)

    for word in wordBank:
        countBank.append(word in english_words)
        
    totalLen = len(countBank)
    totalTrue = sum(countBank)
    return(totalTrue/totalLen)

def metricTwo(contents):
    """Comment similarity index"""
    # extract comments
    # get all the words in an array

    # extract all the words including comments
    # get fraction of comments/ total words 
    
    contentsEmptyLinesRemoved = removeEmptyLine(contents)
    contentsEmptyLinesRemovedPragma = pragmaRemover(contentsEmptyLinesRemoved)
    contentsInArray = codeToArray(contentsEmptyLinesRemovedPragma)
    commentsArray = extractComments(contentsInArray)
    
    # Have our comment words
    commentWordBank =[]
    for line in commentsArray:
        parseLine = wordsFromLine(line)
        processLine = splitLine(parseLine)
        for word in processLine:
            commentWordBank.append(word)
   
    commentWordBankFiltered = solKeywordFilter(commentWordBank)

     # get rest of the identifiers from code
    wordBank = []
    for line in contentsInArray:
        parseLine = wordsFromLine(line)
        processLine = splitLine(parseLine)
        for word in processLine:
            wordBank.append(word)

    wordBankFiltered = solKeywordFilter(wordBank)
    
    totalWordCount = len(commentWordBankFiltered) + len(wordBankFiltered)
    similarity = len(similarityScore(commentWordBankFiltered,wordBankFiltered))
    CIC = similarity/totalWordCount
    
    return CIC

def metricThree(contents):
    """Percentage of camelcase identifiers in code"""
    contents = removeComments(contents)
    contents = removeEmptyLine(contents)
    contents = pragmaRemover(contents)
    contents = libraryRemover(contents)
    
    contents = codeToArray(contents)
    wordBank = []
    for line in contents:
        parseLine = wordsFromLine(line)
        #print(parseLine)
        processLine = splitLine(parseLine)
        for word in processLine:
            wordBank.append(word)
    
    wordBankFiltered = solKeywordFilter(wordBank)

    camelCaseBank, nonCamelCaseBank = camelCase(wordBankFiltered)
    totalWordCount = len(wordBankFiltered)
    camelCount = len(camelCaseBank)
    percentageCamel = camelCount/totalWordCount
    return percentageCamel


def parseFiles(solFileArray):
    # english_words = load_words()
    decimalPlace = 5
    outputArray = [["Filename","Metric One","Metric Two","Metric Three"]]
    for file in solFileArray:
        fileToParse = open(file, "rt",encoding="utf8")
        contents = fileToParse.read()
        #append file name
        tempArray = []
        tempArray.append(file)
        # calc metrics
        tempArray.append(round(metricOne(contents),decimalPlace))
        tempArray.append(round(metricTwo(contents),decimalPlace))
        tempArray.append(round(metricThree(contents),decimalPlace))
        outputArray.append(tempArray)
        # 
        
    return outputArray

def writeCSV(metricsArray):
    timestr = time.strftime("%d%m%Y_%H%M%S")
    csvFileName = "metricExport" + timestr + ".csv"
    with open(csvFileName,"w", newline="") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(metricsArray)
    pass

if __name__ == '__main__':
    english_words = load_words()

    # Key parse functions
    solFiles = getSolFileList()
    # print(solFiles)
    metricsArray = parseFiles(solFiles)

    # print(metricsArray)
    writeCSV(metricsArray)

    #################### development  ###################
    # fileToParse = open("40WAX.sol", "rt",encoding="utf8")
    # contents = fileToParse.read()
    # contents = removeComments(contents)
    # contents = removeEmptyLine(contents)
    # contents = pragmaRemover(contents)
    # contents = libraryRemover(contents)
    
    # contents = codeToArray(contents)
    # wordBank = []
    # for line in contents:
    #     parseLine = wordsFromLine(line)
    #     #print(parseLine)
    #     processLine = splitLine(parseLine)
    #     for word in processLine:
    #         wordBank.append(word)
    
    # wordBankFiltered = solKeywordFilter(wordBank)

    # camelCaseBank, nonCamelCaseBank = camelCase(wordBankFiltered)
    # totalWordCount = len(wordBankFiltered)
    # camelCount = len(camelCaseBank)
    # percentageCamel = camelCount/totalWordCount
    # print(percentageCamel)
    #################### development  ###################
