
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    
    def test_joy_detection(self):
        result = emotion_detector("I'm glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_anger_detection(self):
        result = emotion_detector("I'm really angry about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_disgust_detection(self):
        result = emotion_detector("I feel disgusted when I hear this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_sadness_detection(self):
        result = emotion_detector("I feel very sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_fear_detection(self):
        result = emotion_detector("I'm really afraid this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()