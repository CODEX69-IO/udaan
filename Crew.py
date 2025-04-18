from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os

load_dotenv()

# === AGENTS ===
def create_agents():
    return {
        "defendant": Agent(
            role="Defendant",
            goal="Defend yourself against the charges.",
            backstory="Accused of insider trading. You maintain your innocence.",
            verbose=True,
        ),
        "defense_lawyer": Agent(
            role="Defense Lawyer",
            goal="Defend the defendant and raise reasonable doubt.",
            backstory="Skilled lawyer with a passion for justice.",
            verbose=True,
        ),
        "plaintiff": Agent(
            role="Plaintiff",
            goal="Accuse the defendant of wrongdoing.",
            backstory="Former colleague of the defendant who reported the crime.",
            verbose=True,
        ),
        "prosecution_lawyer": Agent(
            role="Prosecution Lawyer",
            goal="Prove that the defendant is guilty.",
            backstory="State attorney building a strong case based on evidence.",
            verbose=True,
        ),
        "witness_defense": Agent(
            role="Witness for Defense",
            goal="Support the defendant's alibi.",
            backstory="You were with the defendant at the time of the alleged crime.",
            verbose=True,
        ),
        "witness_prosecution": Agent(
            role="Witness for Prosecution",
            goal="Testify against the defendant's actions.",
            backstory="Saw suspicious activity related to the crime.",
            verbose=True,
        ),
        "judge": Agent(
            role="Judge",
            goal="Ensure fair trial and give final ruling.",
            backstory="Experienced judge known for fairness and integrity.",
            verbose=True,
        ),
        "jury": Agent(
            role="Jury",
            goal="Evaluate all arguments and give a verdict.",
            backstory="Neutral jury member attending the full trial.",
            verbose=True,
        )
    }

# === TASKS ===
def create_tasks(agents):
    return [
        # Opening
        Task(description="Give an opening statement for the prosecution.",
             expected_output="Compelling case summary.",
             agent=agents["prosecution_lawyer"]),

        Task(description="Give an opening statement for the defense.",
             expected_output="Defense of the accused.",
             agent=agents["defense_lawyer"]),

        # Interrogation of Witnesses
        Task(description="Interrogate the witness for the defense.",
             expected_output="Testimony supporting the defendant.",
             agent=agents["prosecution_lawyer"]),

        Task(description="Interrogate the witness for the prosecution.",
             expected_output="Cross-examination of hostile testimony.",
             agent=agents["defense_lawyer"]),

        # Witnesses speak
        Task(description="Give testimony as the witness for the defense.",
             expected_output="Describe your version of the events.",
             agent=agents["witness_defense"]),

        Task(description="Give testimony as the witness for the prosecution.",
             expected_output="Describe suspicious behavior of defendant.",
             agent=agents["witness_prosecution"]),

        # Closing
        Task(description="Give your closing statement.",
             expected_output="Summarize your argument.",
             agent=agents["defense_lawyer"]),

        Task(description="Give your closing statement.",
             expected_output="Summarize your prosecution argument.",
             agent=agents["prosecution_lawyer"]),
    ]

# === MAIN RUNNER ===
def run_trial():
    agents = create_agents()
    tasks = create_tasks(agents)
    
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    print("\n👩‍⚖️ Running the Courtroom Simulation...\n")
    result = crew.kickoff()

    print("\n✅ Simulation Complete.\n")

    # User input verdicts from Jury and Judge
    jury_verdict = input("🗣️ Jury, enter your verdict (Guilty / Not Guilty): ")
    judge_verdict = input("👨‍⚖️ Judge, enter your final ruling based on the trial: ")

    print("\n🎓 Final Courtroom Summary:")
    print("🧑‍⚖️ Judge's Final Ruling:", judge_verdict)
    print("🧑‍⚖️ Jury's Verdict:", jury_verdict)
    print("📜 Trial Completed ✅")

if __name__ == "__main__":
    run_trial()
