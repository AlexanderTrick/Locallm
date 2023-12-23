# Locallm
An assistant powered by an LLM that works completely offline.

This project emerged as an experiment to explore the potential of creating Language Model (LLM) assistants akin to those such as Google Assistant or Alexa, with the distinctive feature of operating entirely locally to ensure enhanced privacy.

Throughout its development, i aim to experiment with a variety of technologies and incorporate increasingly specialized functions to achieve optimal results.

## Key Project Objectives

1. **Lightweight Design:**
   - The system should be sufficiently lightweight to run smoothly on computers with moderate performance.
   - Models will be tailored for CPU usage rather than GPU, and preliminary tests with 8GB of RAM have demonstrated a satisfactory user experience.

2. **Comprehensive Functionality:**
   - The assistant is not limited to text generation; it will also feature voice recognition and speech synthesis capabilities, providing a better user experience.

3. **Easy to set up and run:**
   - The end goal is to make as easy to install as possible, without errors that even the greatest of the developers/GPT's in the out there knows how to fix.
  
4. **Good at doing it's primary goal**
   - While traditional assistants such as ChatGPT have been prevalent for a considerable period, the true breakthrough for this assistant will be achieved when it seamlessly executes specific tasks, at the end of the day, it's an assistant, isn't it?
# Getting Started
### Prerequisites
Ensure that the code functions seamlessly with **Python 3.11.5**; other versions have not been tested. Utilize your preferred development environment or virtual environment (for testing, PyCharm Community Edition was employed for its user-friendly management, but any preferred solution is acceptable).

### Installation Steps
1. Clone the repository using the following command:
   ```bash
   git clone https://github.com/AlexanderTrick/Locallm.git
    ```
Navigate to the folder containing the files and download the necessary pip dependencies:
```bash
  pip install -r requirements.txt
```
### Speech Recognition Model Setup

1. Download a speech recognition model of your choice from the official site:

   [Vosk Models](https://alphacephei.com/vosk/models)

   It is recommended to download the `vosk-model-small-en-us-XXXX` version for models with 7 and 13 billion parameters. Models in languages other than English may introduce translation errors and hallucinations, posing a higher risk of inaccuracies.

2. Add the downloaded model to the `models` folder.

### LLM Installation

1. Install the LLM and ensure compatibility with the `pyllamacpp` library (refer to the [pyllamacpp compatibility list](https://pypi.org/project/pyllamacpp/)).

2. Add the LLM model to the `models` folder, specifying the name or path by modifying the code accordingly.

### Final Steps

Now the setup is complete, and you are ready to run the Assistant! You can do that by running
```bash
  python main.py
```
in the terminal or using your IDE of choice.
### Usage
The current use of the assistant simply involves speaking and asking questions, following a similar approach to what one would do with a tool like ChatGPT. However, there are plans for the future to make the interaction more flexible and versatile.

### Contributing
Fell free to help me out by submitting **pull requests** or **issues**!

### License
This project is under the GNU Affero General Public License v3.0.
