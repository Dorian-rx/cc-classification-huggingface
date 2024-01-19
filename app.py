###############################################
##  Sentiment Analysis - Hugging Face | Main ##
###############################################

################
# - PACKAGES - #
################

# -- General -- #
import streamlit as st

# -- Scripts based Import -- #
from src.config import API_URL, API_TOKEN 
from src.utils import runSentimentAnalysis


################
# - FUNCTION - #
################

def main(API_URL, API_TOKEN):
    """Main Function for the Sentiment Analysis Module"""   
    
    # --- Setup STREAMLIT Page --- 
    config_page_title, config_layout = 'Sentimental Analysis', "centered"
    st.set_page_config(page_title=config_page_title, layout=config_layout)  # Set Page Configuration
    st.markdown("<h1 style='text-align: center; color: black;'>Sentimental Analysis - Hugging Face</h1>", unsafe_allow_html=True)
    
    # -- State -- #
    if 'Launch' not in st.session_state:
        st.session_state['Launch'] = False
        st.session_state['Text'] = ""
        st.session_state['Warning_Input'] = False
    
    if not st.session_state['Launch']:
        # -- Text Input -- #
        with st.form(key='sentimental-form'):
            st.session_state['Text'] = st.text_input("Enter your Text", placeholder="I like it, I love it")  # Text Input #
            if st.session_state['Warning_Input']:
                st.warning("You need to enter a text for it to be analyzed")
            submit_button = st.form_submit_button(label='Submit') # Submit Button #

        # -- Run the Sentiment Analysis -- #
        if submit_button:
            if not st.session_state['Text']:
                st.session_state['Warning_Input'] = True
                st.rerun()
            st.session_state['Launch'] = True 
            st.session_state['Warning_Input'] = False
            st.rerun()
    
    
    # -- Launch the Sentiment Analysis -- #
    if st.session_state['Launch']:
        # --- Query the API --- #
        response, success = runSentimentAnalysis(st.session_state['Text'], API_URL, API_TOKEN)
        
        # --- Display the Error Message --- #
        if not success:
            st.error("The API is currently unavailable, please try again later.")            
        
        # --- Display the Results --- #
        else:           
            st.subheader('A reminder of the Written Text')            
            st.markdown(f"<h4 style='text-align: center; color: black;'>\" {st.session_state['Text']} \"</h4>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            lsBG = {"Positive": "rgb(187 247 208)", "Neutral": "rgb(254 240 138)", "Negative": "rgb(254 202 202)"}            
            st.markdown(f"""
                        <div style="text-align: center; border: 1px solid #000; border-radius:5px; padding:5px;">
                            <h4>Positive, Neutral and Negative Classification</h4>
                            <div style="display: flex; flex-direction: row;">
                                <div style="flex: 33.33%; padding: 5px;">
                                    <div style="border: 1px solid #000; padding: 5px; border-radius:5px; background-color:{lsBG[response[0][0]['label'].capitalize()]}">
                                        <h2 style='text-align: center; color: black;'>{response[0][0]['label'].capitalize()}</h2>
                                        <h3 style='text-align: center; color: black;'>{round(response[0][0]['score']*100,3)}%</h3>
                                    </div>
                                </div>                     
                                <div style="flex: 33.33%; padding: 5px;">
                                    <div style="border: 1px solid #000; padding: 5px; border-radius:5px; background-color:{lsBG[response[0][1]['label'].capitalize()]}">
                                        <h2 style='text-align: center; color: black;'>{response[0][1]['label'].capitalize()}</h2>
                                        <h3 style='text-align: center; color: black;'>{round(response[0][1]['score']*100,3)}%</h3>
                                    </div>
                                </div>
                                <div style="flex: 33.33%; padding: 5px;">
                                    <div style="border: 1px solid #000; padding: 5px; border-radius:5px; background-color:{lsBG[response[0][2]['label'].capitalize()]}">
                                        <h2 style='text-align: center; color: black;'>{response[0][2]['label'].capitalize()}</h2>
                                        <h3 style='text-align: center; color: black;'>{round(response[0][2]['score']*100,3)}%</h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
        # --- Retry --- #
        if st.button("Retry with another Text"):
            st.session_state['Launch'] = False
            st.session_state['Text'] = ""
            st.rerun()



############
# - CORE - #
############

if __name__ == "__main__":
    main(API_URL=API_URL, API_TOKEN=API_TOKEN)