import gradio as gr
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer

# Load the tokenizer and model
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("Your_mistral_model_path")
    model = AutoPeftModelForCausalLM.from_pretrained("Your_mistral_model_path").to("cuda")
    return tokenizer, model

tokenizer, model = load_model()

# Finance-specific instruction
finance_instructions = "You are an AI assistant trained to answer finance-related questions. Please respond with accurate and informative answers on topics such as investments, stock market, banking, taxes, loans, inflation, and more."

# Conversation handling
conversation_history = ""
MAX_HISTORY_TURNS = 5  # Limit history to last 5 turns

def chat_with_assistant(input):
    global conversation_history

    # Append the user's input to the conversation history
    conversation_history += f"###Human: {input}\n###Assistant: "

    # Tokenize the conversation history with the finance-specific instruction
    inputs = tokenizer(f"{finance_instructions}\n\n{conversation_history}", return_tensors="pt").to("cuda")

    # Generate the assistant's response with parameters for better completeness
    output = model.generate(
        inputs["input_ids"],
        max_length=500,  # Increase max_length for a longer response
        pad_token_id=tokenizer.eos_token_id,
        num_beams=5,  # Beam search for better output quality
        temperature=0.7,  # Control randomness in the responses
        no_repeat_ngram_size=2,  # Avoid repeating phrases
        early_stopping=True,  # Stop when the answer is complete
        do_sample=True,  # Enable sampling for diversity
        top_p=0.9,  # Control diversity through nucleus sampling
        top_k=50  # Limit sampling to the top 50 tokens
    )

    # Decode the generated output and extract the assistant's response
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    assistant_response = answer.split("###Assistant: ")[-1].strip()

    # Append the assistant's response to the conversation history
    conversation_history += assistant_response + "\n"

    # Limit the conversation history to the last N turns to avoid long inputs
    history_lines = conversation_history.split("\n")
    if len(history_lines) > MAX_HISTORY_TURNS * 2:  # Each turn has two lines (question and answer)
        conversation_history = "\n".join(history_lines[-MAX_HISTORY_TURNS * 2:])

    # Return only the assistant's response
    return assistant_response

# Gradio Interface with a cool, colorful neotheme
iface = gr.Interface(
    fn=chat_with_assistant,
    inputs="text",
    outputs="text",  # Single output box for the assistant's response
    title="Finance AI Assistant",
    examples=[
        ["What are the benefits of investing in mutual funds?"],
        ["How do I calculate my EMI for a loan?"],
        ["What are the Post office saving schemes in India?"],
    ],
    theme="grass",
    allow_flagging="never",
    live=True
)

# Launch the Gradio app
iface.launch()
