from flask import Flask
from flask_restful import Resource, Api, reqparse
import cv2
import pytesseract as pyt
import os


app = Flask(__name__)
api = Api(app)

# Test that tesseract is running correctly
class Test(Resource):
    def get(self):

        # Gets the image data and preprocesses it
        def gather_image_data():
            image = cv2.imread(os.getcwd() + '/media/test.JPG')
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            image_data = pyt.image_to_data(image)
            image_data = image_data.splitlines()

            processed_data = []
            for text_data_str in image_data[1:]:
                text_data = text_data_str.split()
                if len(text_data) == 12 and len(text_data[11]) > 3:
                    processed_data.append(text_data[11])
                    
            return processed_data
        processed_data = gather_image_data()

        # If Tesseract-ocr reads the data as accuratly as Tesseract v.5 would this will return 200 success
        if processed_data == ["YouTube","STACEY","ABRAMS","your","name","STAND","WITH","Sitcoms","Conan","Helps","Assistant","ANew","CONAN","Coco","Conan","Hangs","With","Interns","CONAN","Conan","Andy","Help","Freshmen","Move","Into","College","\"Late","Nig.","Conan","Says","Farewell","Late","Night","CONAN","Sona","Finishes","\"Friends\"","Marathon","CONAN","1.9M","viey","Team","Coco","#CONAN:","Joel","McHale","Full","subs","Interview","CONAN"]:
            return{
                'status': 'success',
                'message': '🚀 All systems go!'
            }, 200
        else:
            try:
                tesseract_version = pyt.get_tesseract_version()
            except:
                tesseract_version = 'Tesseract not found'
            return{
                'status': 'failure',
                'message': f'🔥Test failed.   Tesseract version: {tesseract_version}'
            }, 404

api.add_resource(Test, '/test')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)