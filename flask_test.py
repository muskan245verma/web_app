from flask import Flask,render_template, request
import Lgame

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods=['POST'])
def run_code():
    l1=request.form['loginUser']
    l2=request.form['loginPassword']
    common=Lgame.common_member(l1,l2)
    eq=Lgame.equal(l1,l2)
    return render_template('pass.html', c=common, e=eq)


if __name__ == '__main__':
    app.run(debug=True)