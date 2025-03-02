![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-3.x-orange?logo=gradio&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-1.9%2B-red?logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-orange?logo=huggingface&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)

# Finance AI Assistant 🤖💰

Welcome to the **Finance AI Assistant** project! This is a conversational AI assistant that helps you with finance-related queries, such as investments, stock market insights, banking, taxes, loans, and much more. The model has been fine-tuned to deliver accurate and informative responses to your financial questions.

## 🚀 Features
- **Finance-Specific AI**: Trained to answer all kinds of finance-related questions 📊💸
- **Real-time Interaction**: Chat with the assistant and get instant responses on finance topics 🕒
- **Multi-turn Conversations**: Can handle continuous conversations for more interactive chats 🗣️
- **Customizable**: The model can be fine-tuned further for specific needs 🎯
  
---

## 🧑‍💻 Technology Stack
- **Gradio**: For building a user-friendly web interface 🌐
- **PEFT**: Fine-tuned causal language model to generate answers 🤖
- **Transformers**: For loading and managing the language model 🔄
- **PyTorch**: Used for efficient model computation on GPU 🖥️
- **LLM (Large Language Model)**: Used for processing and generating human-like text responses 🤖🧠
- **Gen AI (Generative AI)**: Powers the AI assistant to provide informative and context-aware responses 🌱
  
---

## 🔧 Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Finance-AI-Assistant.git
   cd Finance-AI-Assistant
   
2. **Install Dependencies**: Install the required libraries by running:
   ```bash
      pip install -r requirements.txt

3. **Download the Pre-trained Model**: To download the fine-tuned Mistral Alpaca model, you can use the following code:
   ```bash
   from transformers import AutoTokenizer, AutoModelForCausalLM

   # Define model path
   model_name = "tiiuae/mistral-finetuned-alpaca"

   # Download and load the model and tokenizer
   tokenizer = AutoTokenizer.from_pretrained(model_name)
   model = AutoModelForCausalLM.from_pretrained(model_name)

   # Save the model and tokenizer locally
   model.save_pretrained("./mistral_finetuned_alpaca")
   tokenizer.save_pretrained("./mistral_finetuned_alpaca")

   print("Model and tokenizer saved successfully!")

This will automatically download the model to your local machine. You can also use the from_pretrained() method to load the model directly from Hugging Face if you have internet access 🌐.

4. **Run the App:** Launch the Gradio app using the following command:

   ```bash
   python app.py
---

## 🧑‍🎓 How to Use
1. Type any finance-related question in the input box 💬
2. Get accurate, and helpful answers to your queries 🎯
3. Explore different financial topics like investments, loans, stocks, banking, and more 💳📉

---

### 📸 Output Preview
![Screenshot 2024-12-25 105345](https://github.com/user-attachments/assets/a8944000-d4b4-4bf6-8414-b88df190c79b)
---
### 📜 License
This project is open-source and available under the MIT License. See the LICENSE file for more details.







