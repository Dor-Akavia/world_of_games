from flask import Flask, request
import xml.dom.minidom
from utils import BAD_RETURN_CODE, SCORES_FILE_NAME

app = Flask("WORLD-OF-GAMES")


@app.route('/mainScore', methods=['GET'])
def getScore():
    my_file = open(SCORES_FILE_NAME, "r")
    lines = my_file.readlines()
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'div', None)
    table = dom.createElement('table')
    header = dom.createElement('h1')
    tableText = dom.createTextNode('Main Score')
    header.appendChild(tableText)
    table.appendChild(header)
    header.setAttribute('style', 'font-family: arial; text-align: center;')
    main_tr = dom.createElement('tr')
    name = dom.createElement('th')
    score = dom.createElement('th')
    name.appendChild(dom.createTextNode('Name'))
    score.appendChild(dom.createTextNode('Score'))
    main_tr.appendChild(name)
    main_tr.appendChild(score)
    table.appendChild(main_tr)

    for line in lines:
        value = line
        numbers = []
        name = []
        chars = "[,',',],"
        for word in value.split():
            if word.isdigit():
                numbers.append(int(word))
                numbersSTR = str(numbers)
            else:
                name.append(word)
                print(name)
                nameSTR = str(name)
        for x in chars:
            nameSTR = nameSTR.replace(x, '')
            numbersSTR = numbersSTR.replace(x, '')

        tr = dom.createElement('tr')
        recordName = dom.createElement('td')
        recordScore = dom.createElement('td')
        recordName.appendChild(dom.createTextNode(nameSTR))
        recordScore.appendChild(dom.createTextNode(numbersSTR))
        tr.appendChild(recordName)
        tr.appendChild(recordScore)
        table.appendChild(tr)
        recordName.setAttribute('style', 'border: 1px solid #dddddd; text-align: center; padding: 8px;')
        recordScore.setAttribute('style', 'border: 1px solid #dddddd; text-align: center; padding: 8px;')
        tr.setAttribute('style', 'background-color: #dddddd;')
    else:
        table.setAttribute('style', 'font-family: arial, sans-serif; border-collapse: collapse; width: 100%;')
        return table.toxml()


app.run(host="0.0.0.0", port=5001, debug=True)
