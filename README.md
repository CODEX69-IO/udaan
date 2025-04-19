**Uddan Courtroom Simulation**

**Description** :

Uddan is a Python-based interactive courtroom simulation tool that leverages LLMs (Large Language Models) to mimic a trial process. Users can input a case description and witness testimonies, and the system simulates the roles of defendant, lawyers, witnesses, judge, and jury, generating realistic courtroom interactions using the CrewAI framework and an Ollama-hosted Llama 3 model.

**Features**:

Simulates a full courtroom trial with roles: Defendant, Defense Lawyer, Plaintiff, Prosecution Lawyer, Witnesses, Judge, and Jury.

Interactive: prompts user input for case description and witness testimonies.

Automated generation of opening statements, cross-examinations, and closing arguments using LLMs.

Final verdict and judge's ruling are entered by the user.

Modular agent creation and backstory updates for each role.



**Installation**:


1.Clone the repository and navigate to the project directory.

2.Install dependencies:

     Python 3.8+
  
     crewai
  
     dotenv

     An Ollama server running the llama3 model.

3.Set up environment variables:

     Create a .env file if needed.

     Set your OpenAI API key (if required for other LLMs).

4.Configure LLM:

    Ensure litellm.config.json is present and correctly maps the llama3 model to your Ollama server.
