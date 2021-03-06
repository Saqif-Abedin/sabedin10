# Third Huge Freckled Elephant
# Ethan Shenker, Constance Chen, Andrew Jiang, Saqif Abedin
# K14 - Form and Function
# 2020-12-10

from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    '''
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    '''
    return render_template('login.html')


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():

    
    if not request.args['username']:
        return render_template("error.html")
    
    '''
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])
    print("***DIAG: request.headers ***")
    '''
    print(request.headers)

    return render_template("response.html", user=request.args['username'], method=request.method)  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()