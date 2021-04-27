import os
import requests
import re
urlsgot = []
#grepper
def geturls(a, grep):

    global urlsgot

    linkreplace = "https://google.com/search?q=REPLACE&client=firefox-b-1-e"
    stoppingpoint = 'did not match any documents.'
    linkreplace = linkreplace.replace('REPLACE', a)
    if len(urlsgot) > 0:
        linkreplace = linkreplace + '&start=' + str(len(urlsgot))

    req = requests.get(linkreplace)
    if req.status_code != 200:
        print('Error retrieving...\n')


    ##begin parsing for links
    returndat = req.text
    urlfinder = '/url?q='
    if returndat.find(urlfinder) > -1:
        urlparse = returndat.split(urlfinder)
        for x in urlparse:
            if x.split('&amp')[0].find('google.com') <= 0 and x.split('&amp')[0].find('function(') <= 0:
                urlsgot.append(x.split('&amp')[0])


    if returndat.find(stoppingpoint) <= 0:
        ##spit out urls.
        intstat = 0
        for x in urlsgot:
            intstat += 1
            if intstat > len(urlsgot) - 10:
                #print(x + '\n')
                ##grepperize
                page = requests.get(x)
                if req.ok:
                    source = page.text
                    itemsfound = re.findall(grep + '..............................................................................................................................', source)
                    if len(itemsfound) > 0:
                        for grepfound in itemsfound:
                            print(x + '\n\n' + grepfound)


        geturls(a, grep)

    elif returndat.find(stoppingpoint) > -1:
        for x in urlsgot:
            print(x + '\n')
        quit()

if __name__ == '__main__':
    print('G0ogol link finder. Enter a search term...\n')
    a = input('')
    print('\n')
    b = input('grep for: \n')

    geturls(a, b)
