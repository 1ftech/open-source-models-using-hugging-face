# 🤗 Open Source Models with Hugging Face 
This repository contains code and resources from the [Open Source Models with Hugging Face](https://www.deeplearning.ai/short-courses/open-source-models-hugging-face/). The project demonstrates how to use publicly available models and their pretrained weights from the Hugging Face Hub to develop powerful AI applications across NLP, audio, vision, and multimodal tasks.

## 🚀 Project Highlights

This project empowers you to:

- ✅ Use the `transformers` library for NLP, audio, vision, and multimodal tasks.
- ✅ Build a chatbot using a small language model with multi-turn conversation handling.
- ✅ Translate between languages, summarize documents, and compare text for semantic similarity.
- ✅ Convert audio to text (ASR) and text to speech (TTS).
- ✅ Perform zero-shot audio classification.
- ✅ Generate audio narration for images using object detection + TTS.
- ✅ Perform zero-shot image segmentation using visual prompting.
- ✅ Combine text and image models for tasks like visual QA, image search, and captioning.
- ✅ Package your code into a Gradio app and deploy it to Hugging Face Spaces.

## 🎯 Learning Outcomes

By the end of this project and repository, you will:

- ✅ Select, apply, and run open-source models from the Hugging Face Hub.
- ✅ Design end-to-end AI applications using transformers and other libraries.
- ✅ Combine multiple models into pipelines to solve multimodal challenges.
- ✅ Build AI apps with user-friendly UIs using **Gradio**.
- ✅ Deploy and share applications publicly using **Hugging Face Spaces**.
- ✅ Understand the practical use cases of **LLMs**, **ASR**, **TTS**, **object detection**, and **zero-shot learning**.


## 🛠 Technologies Used

- 🤗 `transformers`
- 🤖 `datasets`
- 🖼️ `PIL`, `opencv-python`
- 🔊 `torchaudio`
- 🌐 `gradio`
- 🧠 `sentence-transformers`, `diffusers`

## 🌐 Deployment

You can deploy your AI application using:

- **Gradio** for interactive UI
- **Hugging Face Spaces** for free cloud deployment

Example:

```python
import gradio as gr

def predict(input_text):
    return model(input_text)

gr.Interface(fn=predict, inputs="text", outputs="text").launch()


