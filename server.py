''' The application to be executed over the Flask channel and deployed on localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package:
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app :
app=Flask("emotionDetector")
@app.route("/emotionDetector")
def emotion_detection():
    ''' This function sends a GET request to the HTML 
        and call your sentiment_analyzer application with text_to_analyze as the argument.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if not result or result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 200

    response = {
            "anger": result.get('anger', 0),
            "disgust": result.get('disgust', 0),
            "fear": result.get('fear', 0),
            "joy": result.get('joy', 0),
            "sadness": result.get('sadness', 0),
            "dominant_emotion": result.get('dominant_emotion', 'unknown')
        }
    formatted_response = (
            f"For a given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']},  "
            f"'sadness': {response['sadness']}."
            f"The dominant emotion is {response['dominant_emotion']}."
        )
    return formatted_response
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
