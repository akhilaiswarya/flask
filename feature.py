from flask import Flask
FAI=Flask(__name__)

@FAI.route('/stringresponse')
def stringresponse():
    return 'This is our first flask project'

@FAI.route('/Secondstringresponse')
def Secondstringresponse():
    return 'This is our Second string response flask project'

if __name__=='__main__':
    FAI.run(debug=True)
