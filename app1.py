from flask import Flask, request, jsonify
import werkzeug
from main import main
app = Flask(__name__)

@app.route('/post_image',methods=["POST"])
def upload():
    if request.method=="POST":
        imagefile = request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save("files_upload\check.jpg")

        path = 'files_upload/check.jpg'
        ret = main(path)

        return jsonify({
            "message":ret
        })

if __name__ == "__main__":
    app.run(debug=False,port=8080,host='0.0.0.0')