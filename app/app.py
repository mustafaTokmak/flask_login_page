"""
    Created by nguyenvanhieu.vn at 9/16/2018
"""
from flask import Flask, render_template, redirect, url_for, request
import time
import json
app = Flask(__name__)


@app.route('/')
def welcome():  
    return redirect('/login')


@app.route('/home')
def home():
    return 'Login success!'


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form['username'])
        if request.form['username'] == 'mustafa' and request.form['password'] == 'admin':
            return redirect('/redirect_mustafa', code=302)
            
            #return redirect("http://srv.biyosecure.com:4747", code=302)
        elif request.form['username'] == 'kemal' and request.form['password'] == 'admin':
            #return redirect("http://srv.biyosecure.com:4748", code=302)
             return redirect('/redirect_kemal', code=302)

        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)


@app.route('/kemal', methods=['GET', 'POST'])
def kemal():
    error = None
    if request.method == 'POST':
        otp = request.form['username']
        import requests
        import json
        url = "http://31.207.83.251:3999/api/check_totp"

        payload = {}
        payload["userid"] = "kemalulker"
        payload["tenantid"] = "6"
        payload["totp"] = str(otp)
        headers = {
            'Content-Type': "application/json"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        result = response.json()['result']
        if(result == 'True'):
            return render_template('resultsuccess.html', error=error)
        else:
            return render_template('resultfail.html', error=error)
    return render_template('kemal_otp.html', error=error)


@app.route('/mustafa', methods=['GET', 'POST'])
def mustafa():
    error = None
    if request.method == 'POST':
        otp = request.form['username']
        import requests
        import json
        url = "http://31.207.83.251:3999/api/check_totp"

        payload = {}
        payload["userid"] = "mtokmak"
        payload["tenantid"] = "6"
        payload["totp"] = str(otp)
        headers = {
            'Content-Type': "application/json"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        result = response.json()['result']
        if(result == 'True'):
            with open("log.txt","a") as f:
                f.write("cikis,"+"mustafa,"+"otp,"+"True,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return render_template('resultsuccess.html', error=error)
        else:
            with open("log.txt","a") as f:
                f.write("cikis,"+"mustafa,"+"otp,"+"False,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return render_template('resultfail.html', error=error)
        return otp
    return render_template('mustafa_otp.html', error=error)

@app.route('/kemal_long', methods=['GET', 'POST'])
def kemal_long():
    error = None
    if request.method == 'POST':
        otp = request.form['username']
        import requests
        import json
        url = "http://31.207.83.251:3999/api/check_hashchain"

        payload = {}
        payload["userid"] = "kemalulker"
        payload["tenantid"] = "6"
        payload["sessionid"] = "1323232"
        payload["p_init"] = str(otp)
        headers = {
            'Content-Type': "application/json"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        result = response.json()['result']
        if(result == 'True'):
            with open("log.txt","a") as f:
                f.write("cikis,"+"kemal,"+"otp_long,"+"True,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return render_template('resultsuccess.html', error=error)
        else:
            with open("log.txt","a") as f:
                f.write("cikis,"+"kemal,"+"otp_long,"+"True,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return render_template('resultfail.html', error=error)
        return otp
    return render_template('kemal_otp_long.html', error=error)



@app.route('/mustafa_long', methods=['GET', 'POST'])
def mustafa_long():
    error = None
    if request.method == 'POST':
        otp = request.form['username']
        import requests
        import json
        url = "http://31.207.83.251:3999/api/check_hashchain"

        payload = {}
        payload["userid"] = "mtokmak"
        payload["tenantid"] = "6"
        payload["sessionid"] = "1323232"
        payload["p_init"] = str(otp)
        headers = {
            'Content-Type': "application/json"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        result = response.json()['result']
        
        if(result == 'True'):
            with open("log.txt","a") as f:
                f.write("cikis,"+"mustafa,"+"otp_long,"+"True,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return render_template('resultsuccess.html', error=error)
        else:
            with open("log.txt","a") as f:
                f.write("cikis,"+"mustafa,"+"otp_long,"+"False,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return render_template('resultfail.html', error=error)
    return render_template('mustafa_otp_long.html', error=error)


@app.route('/redirect_mustafa', methods=['GET', 'POST'])
def redirect_mustafa():
    error = None
    if request.method == 'POST':
        if request.form['submit_button'] == 'Qr_Reader':
            with open("log.txt","a") as f:
                f.write("giris,"+"mustafa,"+"qr_reader,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return redirect("http://srv.biyosecure.com:4747",302)
            print("srv")
        elif request.form['submit_button'] == 'Otp':
            with open("log.txt","a") as f:
                f.write("giris,"+"mustafa,"+"otp,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return redirect('/mustafa')
        elif request.form['submit_button'] == 'Otp_Long' :
            with open("log.txt","a") as f:
                f.write("giris,"+"mustafa,"+"otp_long,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return redirect('/mustafa_long')
    return render_template('redirect_mustafa.html', error=error)

@app.route('/redirect_kemal', methods=['GET', 'POST'])
def redirect_kemal():
    error = None
    if request.method == 'POST':
        if request.form['submit_button'] == 'Qr_Reader':
            with open("log.txt","a") as f:
                f.write("giris,"+"kemal,"+"qr_reader,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return redirect("http://srv.biyosecure.com:4748",302)
        elif request.form['submit_button'] == 'Otp':
            with open("log.txt","a") as f:
                f.write("giris,"+"kemal,"+"otp,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return redirect('/kemal')
        elif request.form['submit_button'] == 'Otp_Long' :
            with open("log.txt","a") as f:
                f.write("giris,"+"kemal,"+"otp_long,"+str(time.ctime())+", "+str(time.time())+str("\n"))
            return redirect('/kemal_long')

    
    return render_template('redirect_kemal.html', error=error)


@app.route('/redirect_mustafa_success', methods=['GET', 'POST'])
def redirect_mustafa_success():
    error = None
    with open("log.txt","a") as f:
        f.write("cikis,"+"mustafa,"+"qr_reader,"+"True,"+str(time.ctime())+", "+str(time.time())+str("\n"))
    return render_template('resultsuccess.html', error=error)


@app.route('/redirect_kemal_success', methods=['GET', 'POST'])
def redirect_kemal_success():
    error = None
    with open("log.txt","a") as f:
        f.write("cikis,"+"kemal,"+"qr_reader,"+"True,"+str(time.ctime())+", "+str(time.time())+str("\n"))
    return render_template('resultsuccess.html', error=error)


@app.route('/redirect_mustafa_fail', methods=['GET', 'POST'])
def redirect_mustafa_fail():
    error = None
    with open("log.txt","a") as f:
        f.write("cikis,"+"mustafa,"+"qr_reader,"+"False,"+str(time.ctime())+", "+str(time.time())+str("\n"))
    return render_template('resultfail.html', error=error)

@app.route('/redirect_kemal_fail', methods=['GET', 'POST'])
def redirect_kemal_fail():
    error = None
    with open("log.txt","a") as f:
        f.write("cikis,"+"kemal,"+"qr_reader,"+"False,"+str(time.ctime())+", "+str(time.time())+str("\n"))
    return render_template('resultfail.html', error=error)


@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        content = request.get_json()
        with open('log.txt',"a") as f:
            f.write("cikis,"+"mustafa,"+"qr_reader,"+str(time.ctime())+", "+str(time.time())+str("\n"))
        return "True"
    if request.method == 'GET':
        with open('log.txt',"r") as f:
            data = f.readlines()
        return json.dumps(data,indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4545,debug=True)

