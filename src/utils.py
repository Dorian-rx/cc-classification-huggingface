###############################################
## Sentiment Analysis - Hugging Face | Utils ##
###############################################

################
# - PACKAGES - #
################

# -- General -- #
import requests


################
# - FUNCTION - #
################

# -- Query the Sentiment Analysis API -- #
def querySentimentAnalysis(payload: dict, headers: dict, API_URL: str):
    """Query the Sentiment Analysis API
    Args:
        payload (dict): the payload.
        headers (dict): the headers.
        API_URL (str): the API URL.
    """    
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json(), True
    return {}, False


# -- Main Runner for the Sentiment Analysis Module -- #
def runSentimentAnalysis(text: str, API_URL, API_TOKEN):
    """Main Runner for the Sentiment Analysis Module
    Args:
        text (str): the text to be analyzed.
        API_URL (str): the API URL.
        API_TOKEN (str): the API TOKEN.
    """    
    # -- Setup the Payload -- #
    payload = {"inputs": text}
    
    # -- Setup the Headers -- #
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    # -- Query the API -- #
    attempts = 0
    while attempts < 3:
        response, success = querySentimentAnalysis(payload, headers, API_URL)
        if response:
            break
        attempts += 1
        
    # -- Return the Response -- #
    return response, success