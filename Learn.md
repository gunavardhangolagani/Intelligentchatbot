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
<<<<<<< HEAD
      source myenv/bin/activate

=======
   source venv/bin/activate
>>>>>>> refs/remotes/origin/main
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
7. **When you encounter similar type issues**
   -  To https://github.com/gunavardhangolagani/Intelligentchatbot.git
      ! [rejected]        main -> main (non-fast-forward)
      error: failed to push some refs to 'https://github.com/gunavardhangolagani/Intelligentchatbot.git'
      hint: Updates were rejected because the tip of your current branch is behind
      hint: its remote counterpart. If you want to integrate the remote changes,
      hint: use 'git pull' before pushing again.
      hint: See the 'Note about fast-forwards' in 'git push --help' for details.
   - When you ran git merge, you effectively brought the changes from the remote main branch into your local main branch. This action synced your local branch with      the changes on the remote repository.
   - git merge helped you incorporate the changes from the remote repository into your local branch, resolving the conflict between the local and remote versions of the branch, and allowing you to push your changes successfully.

## Usage
  Once the project is set up, you can proceed to run the demo code provided in `demo.ipynb` to see the chatbot in action.
## Further Work
To enhance the capabilities of the chatbot and improve its usability, the following tasks can be implemented:
### 2. Automate the Web Crawling Process

Implement automation for the web crawling process to streamline data collection and update procedures. This automation can include scheduling regular crawls to ensure that the chatbot's knowledge base remains up-to-date with the latest content from the target website(s).

These enhancements will improve the chatbot's efficiency, accuracy, and ability to provide relevant information to users based on the data available on the website(s).
