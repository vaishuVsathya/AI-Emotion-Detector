import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document":{"text": text_to_analyze}}

    response = requests.post(url, headers = header, json = input_json)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        emotions = {'anger': 'None', 'disgust': 'None', 'fear': 'None', 'joy': 'None', 'sadness': 'None', 'dominant_emotion': 'None'}
    return emotions
