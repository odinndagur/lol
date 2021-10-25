from flask import Flask, render_template, request

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './'
@app.route('/')
def first_page():
    return render_template('upload.html')

@app.route('/response_page', methods = ['POST'])
def response_page():
    name = request.form['name']    
    return render_template('response_page.html', name=name)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_filel():
   if request.method == 'POST':
        f = request.files['fil
        print(f)
        filename = f.filename
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],'input.pdf'))
        file = os.path.join(app.config['UPLOAD_FOLDER'],'input.pdf')
        files = {'file':file}
        #resp = requests.get('http://127.0.0.1:8001/uploader')
        return 'loll'
if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
        #app.run()