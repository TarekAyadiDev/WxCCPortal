from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/',methods=["GET", "POST"])
def main():
    headers=['Customer Branch',"Closing the Branch", "Send all to Voicemail", "Type closing annoucement"]
    if request.method == "GET":        
        return render_template('home.html', headers=headers)

    else:
        params_list=[]

        global branch
        branch=request.form.get('branch')
        p={
            "name":"Customer Branch:",
            "value":branch
        }
        params_list.append(p)

        global param1
        param1=request.form.get('param_1_select')
        if param1:
            param1="yes"
            p={
            "name":"Closing the Branch:",
            "value":"yes"
        }
            params_list.append(p)
            
        else:
            param1="no"
            p={
            "name":"Closing the Branch:",
            "value":"no"
        }
            params_list.append(p)
            
        global param2
        param2 = request.form.get('param_2_select')
        if param2:
            param2="yes"
            p={
            "name":"Send all to Voicemail:",
            "value":"yes"
        }
            params_list.append(p)
        else:
            param2="no"
            p={
            "name":"Send all to Voicemail:",
            "value":"no"
        }
            params_list.append(p)

        global param3
        param3 = request.form.get('param_3_select')
        p={
            "name":"Type closing annoucement:",
            "value":param3
        }
        print(param3)
        params_list.append(p)
        
        
        return render_template('home.html', headers=headers, success=True, params_list=params_list)

@app.route('/branch',methods=["GET"])
def branch():
    return branch

@app.route('/param_1',methods=["GET"])
def param_1():
    return param1

@app.route('/param_2',methods=["GET"])
def param_2():
    return param2

@app.route('/param_3',methods=["GET"])
def param_3():
    return param3


if __name__ == "__main__":
    app.run(port=5020,debug=True)