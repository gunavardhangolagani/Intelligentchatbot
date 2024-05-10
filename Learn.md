# Building a Custom Chatbot from Your Website Data
## Setup Instructions
Follow these steps to set up the project on your local machine:

1. **Clone the Repository:**
   ```
   git clone https://github.com/gunavardhangolagani/Intelligentchatbot
   ```
2. **Create a Virtual Environment:**
   ```
   python3 -m venv venv
   ```
3. **Activate the Virtual Environment:** **(Gitpod)**
   ```
   source myenv/bin/activate\
   ```
4. **Deactivate the Virtual Environment:** **(Gitpod)**
   ```
   deactivate
   ```
5. **Install Requirements:**
   ```
   pip install -r requirements.txt
   ```
6. **Configure Environment Variables:**
   - Add your OpenAI API key to `env.sh`:
     ```
     export OPENAI_API_KEY="your_openai_api_key_here"
     ```
## Usage
  Once the project is set up, you can proceed to run the demo code provided in `demo.ipynb` to see the chatbot in action.
## Further Work
To enhance the capabilities of the chatbot and improve its usability, the following tasks can be implemented:
### 2. Automate the Web Crawling Process

Implement automation for the web crawling process to streamline data collection and update procedures. This automation can include scheduling regular crawls to ensure that the chatbot's knowledge base remains up-to-date with the latest content from the target website(s).

These enhancements will improve the chatbot's efficiency, accuracy, and ability to provide relevant information to users based on the data available on the website(s).
