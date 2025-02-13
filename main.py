import requests
import streamlit as st
import json

BASE_API_URL = "http://127.0.0.1:7860"
FLOW_ID = "b009cd29-dc18-4745-bf8c-8e7aec87c5cb"
ENDPOINT = "customer" # The endpoint name of the flow

# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
# TWEAKS = {
#   "ChatInput-tMEFZ": {},
#   "ChatOutput-6CeuH": {},
#   "Agent-exkbp": {},
#   "Prompt-URE69": {},
#   "AstraDB-Asl7b": {},
#   "ParseData-llIwd": {},
#   "File-N7e0b": {},
#   "SplitText-Obey4": {},
#   "AstraDB-Pqrra": {},
#   "Agent-XTEYC": {},
#   "Agent-qJEec": {},
#   "AstraDBToolComponent-B5jhp": {},
#   "AstraDBToolComponent-NK9Xm": {}
# }

def run_flow(message: str,
  output_type: str = "chat",
  input_type: str = "chat") -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param endpoint: The ID or the endpoint name of the flow
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    # if tweaks:
    #     payload["tweaks"] = tweaks
    # if api_key:
    #     headers = {"x-api-key": api_key}

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Chat Interface")
    
    message = st.text_area("Message", placeholder="Ask something...")
    
    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return
    
        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

# res = run_flow("what are the shipment times?")
# print(res)

if __name__ == "__main__":
    main()
