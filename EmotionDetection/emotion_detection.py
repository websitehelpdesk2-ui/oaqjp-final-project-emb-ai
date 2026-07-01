import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers)
    
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the required set of emotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Write the code logic to find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the output in the requested format
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }