from flask import Flask, session,redirect,url_for,render_template,request,jsonify
import requests
app = Flask(__name__)
from PIL import Image
from flask import send_file

# to post on the web
# url = 'http://file.api.wechat.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE'
# files = {'media': open('test.jpg', 'rb')}
# requests.post(url, files=files)

@app.route('/about',methods=['GET'])
def results():
	return jsonify("U are in home page, there is nothing here, go for /post and upload image")


@app.route('/post',methods=['GET'])
def post():
	# print('we are at line 20 ',request.files)
	f = request.files['file']
	# print(f)
	f.save("image.png")
	img = Image.open('image.png').convert('LA')
	img.save('greyscale.png')
	# return jsonify("Success")
	return send_file("greyscale.png", mimetype='image/png')


@app.route('/')
def sendToServer():
	return render_template('home.html')

if __name__ == '__main__':
	app.debug=True
	app.run()