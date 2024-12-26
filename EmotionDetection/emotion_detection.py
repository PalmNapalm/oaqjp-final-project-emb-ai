# Example usage:
# > python3.11
# > from emotion_detection import emotion_detector
# > print(emotion_detector("I hate working long hours"))

import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code == 200:
        result = response.json()
        emotions = result['emotionPredictions'][0]['emotion']
        
        # Find the emotion with the highest score
        dominant_emotion = max(emotions, key=emotions.get)
        dominant_score = emotions[dominant_emotion]

        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }
    else:
        return f"Error: {response.status_code}"
