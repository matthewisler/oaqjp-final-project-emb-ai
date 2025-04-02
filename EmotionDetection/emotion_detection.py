import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions']

        anger_score = emotions[0]['emotion']['anger']
        disgust_score = emotions[0]['emotion']['disgust']
        fear_score = emotions[0]['emotion']['fear']
        joy_score = emotions[0]['emotion']['joy']
        sadness_score = emotions[0]['emotion']['sadness']
        
        ret_dict = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        dom_emotion = max(ret_dict, key=ret_dict.get)
        ret_dict['dominant_emotion'] = dom_emotion

    elif response.status_code == 400:
        ret_dict = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return ret_dict
