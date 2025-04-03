from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_result = emotion_detector("I am glad this happened")
        self.assertEqual(test_result['dominant_emotion'], "joy")
        test_result = emotion_detector("I am really mad about this")
        self.assertEqual(test_result['dominant_emotion'], "anger")
        test_result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_result['dominant_emotion'], "disgust")
        test_result = emotion_detector("I am so sad about this")
        self.assertEqual(test_result['dominant_emotion'], "sadness")
        test_result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test_result['dominant_emotion'], "fear")
unittest.main()