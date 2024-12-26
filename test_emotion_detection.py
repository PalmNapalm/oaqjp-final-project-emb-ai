import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detection(self):
        # Define test cases as a list of tuples (statement, expected_emotion)
        test_cases = [
            ("I am glad this happened", 'joy'),
            ("I am really mad about this", 'anger'),
            ("I feel disgusted just hearing about this", 'disgust'),
            ("I am so sad about this", 'sadness'),
            ("I am really afraid that this will happen", 'fear')
        ]

        for text, expected_emotion in test_cases:
            with self.subTest(text=text):
                emotions = emotion_detector(text)

                # Check if the dominant emotion matches the expected emotion
                self.assertEqual(emotions['dominant_emotion'], expected_emotion)

if __name__ == '__main__':
    unittest.main()
