'''Server to detect emotions '''
from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    '''Detect emotion from input string'''
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    formatted_output = (
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}."
    )
    response = (
        f"For the given statement, the system response is"
        f" {formatted_output}. The dominant emotion {emotions['dominant_emotion']}.")

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
