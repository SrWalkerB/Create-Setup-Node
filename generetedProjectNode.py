import sys
import os

startJS = """const express = require('express');
const dotenv = require('dotenv');

dotenv.config();

const PORT = 4000;

const app = express();

app.use(express.json());

app.get("/", (req, res) => {
    return res.json({
        message: "Hello World"
    });
})

app.listen(PORT, () => {
    console.log(`Server in running: ${PORT}`);
});
"""

def generetedDir(name):
    os.mkdir(name)

def executeCommand(command):
    return os.system(command)

def getArgumentScript():
    return sys.argv[1]

def navegateDir(dirName):
    return os.chdir(dirName)

def generetedFile(filename):
    open(filename, 'w')

def writingFile(filename, data):
    file = open(filename, 'w')
    file.write(data)
    file.close()

def executeListCommands(listComands):
    
    for command in listComands:
        executeCommand(command)


def main():
    listCommands = [
        "npm init --y",
        "npm install express",
        "npm install dotenv",
        "npm install nodemon --save-dev"
    ]

    myPath = 'Desktop/Things/Codes/Node'

    dirNameArgument = getArgumentScript()

    navegateDir(myPath)
    generetedDir(dirNameArgument)
    navegateDir(dirNameArgument)
    executeListCommands(listCommands)
    generetedFile('.gitignore')
    generetedFile('.env')
    writingFile('.gitignore', "node_modules")
    generetedDir('src')
    navegateDir('src')
    generetedFile('main.js')
    writingFile('main.js', startJS)

main()
