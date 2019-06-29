from flask import Flask,render_template,request
import requests
import json
import time




app = Flask(__name__)

@app.route('/test1')
def web1():
	return render_template("index1.html")

 
@app.route('/test2')
def web2():
	
	return render_template("index2.html")
	

@app.route('/test3',methods = ["POST"])
def web3():
	latitude = request.form['Latitude']
	longitude = request.form['Longitude']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat='+latitude+'&lon='+longitude+'&appid=f99ff9bee2ebf69b87d81068bb64b639')


	obj = r.text
	print(obj) 
	print(type(obj))
	obj1 = json.loads(obj) 
	res = float(obj1['main']['temp_min']),float(obj1['main']['temp_max']),float(obj1['main']['humidity']),float(obj1['main']['pressure']),float(obj1['wind']['speed']),float(obj1['clouds']['all']),float(obj1['sys']['sunrise']),float(obj1['sys']['sunset']),(obj1['weather'][0]['icon']),float(obj1['main']['temp']),(obj1['weather'][0]['description'])
	

	a = res[0]-273
	b = res[1]-273
	c = res[2]
	d = res[3]
	e = res[4]
	f = res[5]
	
	ts = int(float(obj1['sys']['sunrise']))
	g = time.ctime(ts)
	print(g)

	ts = int(float(obj1['sys']['sunset']))
	h = time.ctime(ts)
	print(h)

	i = res[8]
	j = res[9]-273
	k = res[10]
	

	return render_template("index4.html",a = round(a,2),b = round(b,2),c= c,d = d,e = e,f = f,g = g,h = h,i = i,j=round(j,2),k = k)



@app.route('/test4')
def web4():
	return render_template("index3.html")



@app.route('/test5',methods=['POST'])
def web5():
	pincode = request.form['Pincode']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+pincode+',IN&appid=f99ff9bee2ebf69b87d81068bb64b639')
	

	obj = r.text
	print(obj) 
	print(type(obj))
	obj1 = json.loads(obj) 
	res = float(obj1['main']['temp_min']),float(obj1['main']['temp_max']),float(obj1['main']['humidity']),float(obj1['main']['pressure']),float(obj1['wind']['speed']),float(obj1['clouds']['all']),float(obj1['sys']['sunrise']),float(obj1['sys']['sunset']),(obj1['weather'][0]['icon']),float(obj1['main']['temp']),(obj1['weather'][0]['description'])
	

	a = res[0]-273
	b = res[1]-273
	c = res[2]
	d = res[3]
	e = res[4]
	f = res[5]
	
	ts = int(float(obj1['sys']['sunrise']))
	g = time.ctime(ts)
	print(g)

	ts = int(float(obj1['sys']['sunset']))
	h = time.ctime(ts)
	print(h)

	i = res[8]
	j = res[9]-273
	k = res[10]
	

	return render_template("index4.html",a = round(a,2),b = round(b,2),c= c,d = d,e = e,f = f,g = g,h = h,i = i,j=round(j,2),k = k)

@app.route('/test6',methods=['POST'])
def web6():
	state = request.form['stateslist']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+state+',IN&appid=f99ff9bee2ebf69b87d81068bb64b639')
	obj = r.text
	obj1 = json.loads(obj)
	print(obj1)
	r1 = float(obj1['main']['temp'])

	
	return str(r1)


if __name__ == '__main__':
	app.run(debug = True)