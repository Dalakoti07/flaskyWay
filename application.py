from flask import Flask, session,redirect,url_for,render_template,request,jsonify
import requests
app = Flask(__name__)
from PIL import Image
from flask import send_file

# to post on the web
# url = 'http://file.api.wechat.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE'
# files = {'media': open('test.jpg', 'rb')}
# requests.post(url, files=files)

@app.route('/result',methods=['GET','POST'])
def results():
	if(request.method=='POST'):
		pass


@app.route('/post',methods=['POST','GET'])
def post():
	print('we are at line 20 ',request.files)
	f = request.files['file']
	print("line 15")
	f.save("image.png")
	img = Image.open('image.png').convert('LA')
	img.save('greyscale.png')
	return send_file("greyscale.png", mimetype='image/png')


@app.route('/')
def sendToServer():
	return render_template('home.html')

if __name__ == '__main__':
	app.debug=True
	app.run()