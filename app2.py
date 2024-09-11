# Import necessary libraries
from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

# Function to load the LLaMA-compatible model and generate a response
def get_llama_response(question):
    # Load tokenizer and model (replace 'model_name' with the LLaMA variant)
    model_name = "meta-llama/Llama-2-7b-chat-hf"  # Example: LLaMA-2 model variant
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Encode the input question
    inputs = tokenizer(question, return_tensors="pt")

    # Generate the response using the model
    outputs = model.generate(inputs["input_ids"], max_length=512, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Chatbot with LLaMA")

st.header("LLaMA Q&A Application")

# Get user input
input_question = st.text_input("Enter your question:", key="input")

# Submit button to ask the question
submit = st.button("Ask the question")

# If the submit button is clicked, get and display the response
if submit and input_question.strip():  # Check if input is not empty
    response = get_llama_response(input_question)
    st.subheader("The Response is:")
    st.write(response)
