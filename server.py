''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask('EmotionDetector')

@app.route('/')
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotion names and its confidence 
        score for the provided text and also the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] == 'None':
        response_text = "<b>Invalid text! Please try again!</b>"
    else:
        items = [f"'{key}': {value}" for key, value in response.items()]
        response_text = ("For the given statement, the system response is "
                        + ", ".join(items[0:-2])
                        + f" and {items[-2]}."
                        + f" The dominant emotion is <b>{response['dominant_emotion']}.</b>")
    return response_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
