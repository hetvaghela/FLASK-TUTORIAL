from flask import Flask
app=Flask(__name__)
def about():
    return "this is about page"

app.add_url_rule("/","about",about)

if __name__=="__main__":
    app.run(debug=True)