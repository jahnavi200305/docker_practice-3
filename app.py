from flask import Flask, request,jsonify


app=Flask(__name__)


@app.route('/calculate',methods=['POST]'])
def calculate():
    data=request.get_json()
    num1=data.get('num1')
    num2=data.get('num2')
    operation=data.get('operation')
    
    if not all([num1,num2,operation]):
        return jsonify({'error':'Missing input'}),400
    if operation=='add':
        result = num1+num2
    elif operation=='subtract':
        result = num1-num2
    elif operation=='multiply':
        result=num1*num2
    elif operation=='divide':
        if(num2!=0):
            result =num1/num2
        else:
            'undefined'
    else:
        return jsonify({'error': 'Invalid operation'})
    return jsonify({'result':result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    
    