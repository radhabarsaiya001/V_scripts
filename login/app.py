from flask import Flask,request,jsonify
from login_functionality import authentication

auth = authentication()
app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    try:        
        data = request.get_json()
        name = data.get('name')
        pwd = data.get('pwd')
        db_name, db_pwd =auth.g_data()        
        print("user pwd",pwd)
        print("database pwd ",db_pwd)

        if name == db_name and pwd == db_pwd:
            return jsonify({'msg':'successfully login!','status':200})
        elif name != db_name and pwd != db_pwd:
            return jsonify({'msg':'Invalid username and password','status':500})
        elif pwd != db_pwd:
            return jsonify({'msg':'Invalid password','status':500})
        else :
            return jsonify({'msg':'Invalid username','status':500})
        
    except Exception as e:
        return jsonify({'error': str(e), 'status':500})

@app.route('/reset_pwd',methods=['POST'])
def forgot():
    try:
        data = request.get_json()
        name = data.get('name')
        pwd = data.get('pwd')
        db_name, db_pwd =auth.g_data()
        if name == db_name: 
            auth.update_data(pwd)
            return jsonify({'msg':'success','status':200})
        else:
            return "User is not registered please sign in!"
    except Exception as e:
        return jsonify({'Error':str(e),'status':500})
    
if __name__ =="__main__":
    app.run(debug= True)