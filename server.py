from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask('EmotionDetector')

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    items = [f"'{key}': {value}" for key, value in response.items()]
    response_text = "For the given statement, the system response is " 
                    + ", ".join(items[0:-2]) 
                    + f" and {items[-2]}. The dominant emotion is <b>{response['dominant_emotion']}.</b>"
    return response_text
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)