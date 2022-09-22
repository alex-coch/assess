import os
from flask import Flask, request
from werkzeug.utils import secure_filename
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/static/upload'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    ret = '''
    <!doctype html>
    Enter t, c, k parameters<br>
    <form method=post enctype=multipart/form-data>
    x-array:
    <input type="text"  name="x1"><br>
    y-array:
    <input type="text"  name="y1"><br>
    k:
    <input type="text"  name="k"><br>
    <input type=file name=file><br>
    <input type=submit value=Upload>
    </form>
    '''
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        img = plt.imread(path)
        x1 = request.form["x1"].split(",")
        y1 = request.form["y1"].split(",")
        x = np.array(list(map(float, x1)))
        y = np.array(list(map(float, y1)))
        k1 = int(request.form["k"])
        spl = splrep(x, y, k=k1)
        x2 = np.linspace(-4, 4, 16)
        y2 = splev(x2, spl)
        plt.plot(x2, y2)
        plt.imshow(img, zorder=0, extent=[-4, 4, -4, 4])
        plt.savefig(path)

        ret = f'<img src=static/upload/{filename}>'
    return ret

if __name__ == "__main__":
    app.run(debug=True)
