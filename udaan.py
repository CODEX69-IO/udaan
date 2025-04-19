import os
os.environ["LITELLM_CONFIG_PATH"] = "litellm.config.json"
from crewai import Crew, LLM
from crewai import Agent, Task, Crew
from dotenv import load_dotenv



OPENAI_API_KEY=""

llm = LLM(
    model="ollama/llama3:latest",
    base_url="http://localhost:11434"
)

load_dotenv()
OLLAMA_BASE_URL = "http://localhost:11434"
LLAMA_MODEL = "llama3"

print("done")
def create_agents():
    placeholder_backstory = "This will be updated based on the case description."
    return {
        "defendant": Agent(
            role="Defendant",
            goal="Defend yourself against the charges.",
            backstory=placeholder_backstory,
            verbose=True,
             model="llama3",
             llm=llm
        ),
        "defense_lawyer": Agent(
            role="Defense Lawyer",
            goal="Defend the defendant and raise reasonable doubt.",
            backstory=placeholder_backstory,
            verbose=True,
             model="llama3",
             llm=llm
        ),
        "plaintiff": Agent(
            role="Plaintiff",
            goal="Accuse the defendant of wrongdoing.",
            backstory=placeholder_backstory,
            verbose=True,
             model="llama3",
             llm=llm
        ),
        "prosecution_lawyer": Agent(
            role="Prosecution Lawyer",
            goal="Prove that the defendant is guilty.",
            backstory=placeholder_backstory,
            verbose=True,
             model="llama3",
             llm=llm
            
        ),
        "witness_defense": Agent(
            role="Witness for Defense",
            goal="Support the defendant's alibi.",
            backstory=placeholder_backstory,
            verbose=True,
             model="llama3",
             llm=llm
        ),
        "witness_prosecution": Agent(
            role="Witness for Prosecution",
            goal="Testify against the defendant's actions.",
            backstory=placeholder_backstory,
            verbose=True,
             model="llama3",
             llm=llm
        ),
        "judge": Agent(
            role="Judge",
            goal="Ensure fair trial and give final ruling.",
            backstory=placeholder_backstory,
            verbose=True,
             model="llama3",
             llm=llm
        ),
        "jury": Agent(
            role="Jury",
            goal="Evaluate all arguments and give a verdict.",
            backstory=placeholder_backstory,
            verbose=True,
             model="llama3",
             llm=llm
        )
    }
def update_backstories(agents, case_description):
    agents["defendant"].backstory = "You are accused in this case. Case details: " + case_description
    agents["defense_lawyer"].backstory = "You are representing the defendant in this case. Case: " + case_description
    agents["plaintiff"].backstory = "You are bringing the case forward. Case: " + case_description
    agents["prosecution_lawyer"].backstory = "You are the prosecution attorney in this case. Case: " + case_description
    agents["witness_defense"].backstory = "You are a witness supporting the defendant. Case: " + case_description
    agents["witness_prosecution"].backstory = "You are a witness against the defendant. Case: " + case_description
    agents["judge"].backstory = "You are overseeing the trial. Case: " + case_description
    agents["jury"].backstory = "You are the jury member deciding the outcome. Case: " + case_description


print("done")
# def create_tasks(agents):
#     return [
#         # Opening
#         Task(description="Give an opening statement for the prosecution.",
#              expected_output="Compelling case summary.",
#              agent=agents["prosecution_lawyer"]),

#         Task(description="Give an opening statement for the defense.",
#              expected_output="Defense of the accused.",
#              agent=agents["defense_lawyer"]),

#         # Interrogation of Witnesses
#         Task(description="Interrogate the witness for the defense.",
#              expected_output="Testimony supporting the defendant.",
#              agent=agents["prosecution_lawyer"]),

#         Task(description="Interrogate the witness for the prosecution.",
#              expected_output="Cross-examination of hostile testimony.",
#              agent=agents["defense_lawyer"]),

#         # Witnesses speak
#         Task(description="Give testimony as the witness for the defense.",
#              expected_output="Describe your version of the events.",
#              agent=agents["witness_defense"]),

#         Task(description="Give testimony as the witness for the prosecution.",
#              expected_output="Describe suspicious behavior of defendant.",
#              agent=agents["witness_prosecution"]),

#         # Closing
#         Task(description="Give your closing statement.",
#              expected_output="Summarize your argument.",
#              agent=agents["defense_lawyer"]),

#         Task(description="Give your closing statement.",
#              expected_output="Summarize your prosecution argument.",
#              agent=agents["prosecution_lawyer"]),
#     ]
print("done")
# === MAIN RUNNER ===
# === MAIN RUNNER ===
def run_trial():
    agents = create_agents()

    # 📝 CASE SETUP
    case_description = input("Enter a description of the case: ")

    update_backstories(agents, case_description)
    # 👥 WITNESS TESTIMONIES (USER INPUT)
    witness_defense_testimony = input("Witness for Defense, enter your testimony: ")
    witness_prosecution_testimony = input("Witness for Prosecution, enter your testimony: ")

    # 📌 TASKS FOR CReWAI
    tasks = [
        Task(description=f"Case: {case_description}\nGive an opening statement for the prosecution.",
             expected_output="Compelling case summary.",
             agent=agents["prosecution_lawyer"],
             model=LLAMA_MODEL,
             base_url=OLLAMA_BASE_URL),

        Task(description=f"Case: {case_description}\nGive an opening statement for the defense.",
             expected_output="Defense of the accused.",
             agent=agents["defense_lawyer"],
             model=LLAMA_MODEL,
             base_url=OLLAMA_BASE_URL),

        Task(description=f"Interrogate the witness for the defense. Witness said: '{witness_defense_testimony}'",
             expected_output="Cross-examine the credibility of their testimony.",
             agent=agents["prosecution_lawyer"],
             model=LLAMA_MODEL,
             base_url=OLLAMA_BASE_URL),

        Task(description=f"Interrogate the witness for the prosecution. Witness said: '{witness_prosecution_testimony}'",
             expected_output="Try to weaken their testimony.",
             agent=agents["defense_lawyer"],
             model=LLAMA_MODEL,
             base_url=OLLAMA_BASE_URL),

        Task(description="Give your closing statement.",
             expected_output="Summarize your defense.",
             agent=agents["defense_lawyer"],
             model=LLAMA_MODEL,
             base_url=OLLAMA_BASE_URL),

        Task(description="Give your closing statement.",
             expected_output="Summarize your case against the defendant.",
             agent=agents["prosecution_lawyer"],
             model=LLAMA_MODEL,
             base_url=OLLAMA_BASE_URL),
    ]

    # 🧠 RUN THE TRIAL
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    print("\n👩‍⚖ Running the Courtroom Simulation...\n")
    result = crew.kickoff()

    print("\n✅ Simulation Complete.\n")

    # 👨‍⚖ FINAL VERDICTS
    jury_verdict = input("🗳 Jury, enter your verdict (Guilty / Not Guilty): ")
    judge_final_statement = input("👨‍⚖ Judge, write your final ruling statement: ")

    print("\n🎓 Final Courtroom Summary:")
    print("📄 Case:", case_description)
    print("🧑‍⚖ Judge's Final Ruling:", judge_final_statement)
    print("🧑‍⚖ Jury's Verdict:", jury_verdict)
    print("📜 Trial Completed ✅")
if __name__ == "__main__":
    run_trial()
