from flask import Flask, request, render_template, jsonify
import xml_to_csv as xtoc
import test
import test2
import tp5
import os


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/pretrpage')
def pretrpage():
    return render_template('tr.html')

@app.route('/trpage')
def trpage():
    res=xtoc.main()
    if res!=1:
        return 'Es gibt eine Fehler. Bite schauen Sie es in console'
    os.system("python3 generate_tfrecord_tr.py")
    os.system("python3 generate_tfrecord_te.py")
    os.system("python3 train.py")
    return 'Ok! <a href="/" onClick=”javascript :history.go(-1);”>back</a>'

@app.route('/output')
def output():
    os.system("python3 export_inference_graph.py")
    return 'Ok! <a href="/" onClick=”javascript :history.go(-1);”>back</a>'

@app.route('/uppage')
def uppage():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        option = request.form['option']
        f = request.files['picture']
        f.save('test_image/1.jpg')
#        ou=jsonify(test.check())
#        return option
#        ou = test.check()
        if option=='xml':
            ou = test2.check()
            ou = tp5.text_xml(ou)
#            os.system("python3 tp5.py")
        else:
            ou = test.check()
            os.system("python3 tp4.py")
        return ou+'<br/><br/>Ok! <a href="/uppage" onClick=”javascript :history.go(-1);”>back</a>'
    return 'Ok! <a href="/uppage" onClick=”javascript :history.go(-1);”>back</a>'

if __name__ == '__main__':
    app.debug = True
    app.run(port=80)
