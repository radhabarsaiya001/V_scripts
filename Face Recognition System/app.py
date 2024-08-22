from flask import Flask, jsonify, request
import Register_in_FRS_Application as fr

app = Flask(__name__)
@app.route('/Register',methods=["POST"])
def fun():
    try:
        data = request.get_json()
        faceid = data['faceid']
        name = data['name']
        reg = fr.register(faceid,name)
        return str(reg)
    except Exception as e:
        return e

if __name__ =="__main__":
    app.run(debug=True)