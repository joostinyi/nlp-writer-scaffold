# Run by typing python3 main.py

## **IMPORTANT:** only collaborators on the project where you run
## this can access this web server!

"""
    Bonus points if you want to have internship at AI Camp
    1. How can we save what user built? And if we can save them, like allow them to publish, can we load the saved results back on the home page? 
    2. Can you add a button for each generated item at the frontend to just allow that item to be added to the story that the user is building? 
    3. What other features you'd like to develop to help AI write better with a user? 
    4. How to speed up the model run? Quantize the model? Using a GPU to run the model? 
"""

# import basics
import os

# import stuff for our web server
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from flask import jsonify
from utils import get_base_url, allowed_file, and_syntax

# import stuff for our models
import torch
from aitextgen import aitextgen

'''
Coding center code - comment out the following 4 lines of code when ready for production
'''
# load up the model into memory
# you will need to have all your trained model in the app/ directory.

'''
##JACKSON##
Need to change absolute path to download from gdrive and make model instances for each of the 2 saved models
'''
model_path = '/projects/ffb3608a-abf1-4dd2-af5c-8e98ccab67df/Batch_A/trained_models/'
ai_pos = aitextgen(to_gpu=False, model_folder=model_path+'positive_output_directory')
ai_neg = aitextgen(to_gpu=False, model_folder=model_path+'negative_output_directory')

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 12340
base_url = get_base_url(port)
# app = Flask(__name__, static_url_path=base_url+'static')

'''
Deployment code - uncomment the following line of code when ready for production
'''
app = Flask(__name__)


@app.route('/', methods = ['GET'])
# @app.route(base_url, methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
# @app.route(base_url+'/result', methods = ['POST'])
def result():
    prompt = request.form['prompt']
    sentiment = str(request.form['sentiment'])
    model = ai_pos if sentiment == 'positive' else ai_neg
    generated = model.generate(
        n=1,
        batch_size=3,
        prompt=str(prompt),
        max_length=50,
        temperature=0.9,
        return_as_list=True
    )
    return render_template('index.html', generated=generated[0])


if __name__ == "__main__":
    '''
    coding center code
    '''
    # IMPORTANT: change the cocalcx.ai-camp.org to the site where you are editing this file.
    website_url = 'cocalc3.ai-camp.org'
    print(f"Try to open\n\n    https://{website_url}" + base_url + '\n\n')

    app.run(host = '0.0.0.0', port=port, debug=True)
    import sys; sys.exit(0)

    '''
    scaffold code
    '''
    # Only for debugging while developing
    # app.run(port=80, debug=True)

