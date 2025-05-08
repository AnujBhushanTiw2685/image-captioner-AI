# 🖼️ AI Image Caption Generator

A lightweight GenAI project that automatically generates captions for uploaded images using the BLIP (Bootstrapped Language Image Pretraining) model from HuggingFace. This project is built with Python and Streamlit and runs locally in minutes!

---

## 🚀 Features

- Upload any image (JPEG, PNG, etc.)
- Get an automatic AI-generated caption for the image
- Simple and clean web interface powered by Streamlit
- Uses a pretrained transformer model (Salesforce/BLIP)

---

## 🧰 Tech Stack

- Python 3.9+
- Streamlit
- HuggingFace Transformers
- PyTorch
- PIL (Pillow)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-captioner.git
cd ai-captioner

```
###  2. Create a Virtual Environment
```bash
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on macOS/Linux
source venv/bin/activate

``` 
### 3. Install Dependencies
 Install PyTorch (CPU-only):

 ```bash

 pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


 ```
 Install other packages:

 ```bash
 pip install streamlit transformers pillow
 
 ```

## ▶️ Run the App:

```bash

streamlit run app.py


```


