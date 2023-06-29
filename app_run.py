from flask import Flask, render_template,url_for,redirect
app = Flask(__name__)

@app.route('/')
def main():
   return render_template('index.html')
   #main driver function
if __name__ == '__main__':
   app.run(debug=False,port=8000)