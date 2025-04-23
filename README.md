
# VoiceClone-GPT-Agent

A real-time voice cloning system integrated with GPT-based smart replies. This project lets you interact using your own cloned voice, powered by advanced AI models for both speech synthesis and text generation.


## About the Project

**VoiceClone-GPT-Agent** enables users to:

- Input speech via microphone in real time
- Generate intelligent replies using GPT (or LLaMA via Ollama)
- Hear AI-generated responses in their own cloned voice
- Seamlessly integrate with external voice models and pre-trained data

---


## Requirements

Before getting started, ensure you have the following installed:

- **Python 3.10+** (Recommended)
- **Git**
- **CUDA Toolkit** (Optional but recommended for GPU acceleration)
- **git-lfs** (For handling large files such as model weights)


## Instructions to Download

1. **Clone the repository:**

   ```bash
   git clone https://github.com/akshat8415/voiceclone-gpt-agent.git
   cd voiceclone-gpt-agent```


2. **Set up a virtual environment (recommended):**

    ```python -m venv venv```
    ```source venv/bin/activate```  # On Windows, use venv\Scripts\activate

    - After that
        ```python3.10 -m venv venv```
    - For activate the environment
        ```.\venv_py310\Scripts\activate ```
 


3. **Install project dependencies:**

    ```pip install -r requirements.txt```


4. **Downloading and Placing the Models**
This project requires three large pre-trained models (Encoder, Synthesizer, Vocoder) that are not stored directly in the repository due to size limits.Steps:

    1. Download the models from the following Google Drive folder:Download Models from Google Drive     

    2. Download the following files:
- [Drive Link](https://drive.google.com/drive/folders/1Gwf02JQkOkzyxWJDbbpJWKAE3HjzhpVO?usp=drive_link)

        1. encoder.pt
        2. synthesizer.pt
        3. vocoder.pt

4. **Place the downloaded files in the corresponding directories inside your project folder as shown below:**

    ```voiceclone-gpt-agent/
            ├── encoder/
            │   └── saved_models/
            │       └── encoder.pt
            ├── synthesizer/
            │   └── saved_models/
            │       └── synthesizer.pt
            └── vocoder/
                └── saved_models/
                    └── vocoder.pt```

5. **Setup & Running**
    ``python voice_cloner.py``

6. **Interact**
- Speak into your microphone.
- The system will generate a text reply using ollam and respond in your cloned voice

## Acknowledgements

- [Real-Time Voice Cloning Repository](https://github.com/CorentinJ/Real-Time-Voice-Cloning)
- [GPT / LLaMA (Ollama)](https://ollama.com)

