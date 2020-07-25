from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def student():
    return render_template('student_ex4.html')

@app.route('/result1',methods=['POST','GET'])
def output():
    if request.method=='POST':
        result=request.form
        return render_template("result.html",something=result)

if __name__=='__main__':
    app.run(debug=True)