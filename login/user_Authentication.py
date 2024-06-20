from flask import Flask,request,jsonify
from cryptography.fernet import Fernet 
from db_model import database_model

db = database_model()
db_alldata = db.user_db()
# print(db_alldata)
db_pwd = db_alldata[0]["password"]
db_name = db_alldata[0]["name"]
secret_key = db_alldata[0]["secret_key"]
# print(secret_key)

# *************Fernet Decryption*************
f = Fernet(secret_key)
decrypt_password = f.decrypt(db_pwd)
decrypt_name = f.decrypt(db_name)
# print(decrypt_name.decode())
# print(decrypt_password.decode())

app = Flask(__name__)
@app.route('/login',methods=['POST'])
def login():
    try:
        data = request.get_json()
        pwd = data.get('pwd')
        name = data.get("name")
        if name == decrypt_name.decode() and pwd == decrypt_password.decode():
            return jsonify({'msg':'successfully login!','status':200})
        elif name != decrypt_name.decode() and pwd != decrypt_password.decode():
            return jsonify({'msg':'Invalid username and password','status':500})
        elif pwd != decrypt_password.decode():
            return jsonify({'msg':'Invalid password','status':500})
        else :
            return jsonify({'msg':'Invalid username','status':500})
    except Exception as e:
        return jsonify({'error': str(e), 'status':500})
    
if __name__ =="__main__":
    app.run(debug= True)
