This document explains the structure and purpose of each part of the uddan.py file, which implements an AI-powered courtroom simulation using CrewAI and a local Llama 3 model.

## 1\. Imports and Environment Setup

* os, dotenv: Used to set environment variables and load configuration from .env files.  
* crewai: Imports core classes (Agent, Task, Crew, LLM) for multi-agent orchestration.  
* OPENAI\_API\_KEY: Placeholder for API key (not actively used in this code).  
* LLM Initialization: Sets up the LLM interface to use the Llama 3 model served locally via Ollama at http://localhost:11434.

## 2\. Agent Creation

The create\_agents() function defines all courtroom participants as AI agents:

* Roles: Defendant, Defense Lawyer, Plaintiff, Prosecution Lawyer, Witness for Defense, Witness for Prosecution, Judge, Jury.  
* Goal: Each agent has a specific goal (e.g., defend, prosecute, testify, judge).  
* Backstory: Initially a placeholder, updated later with case details.  
* Model: All agents use the Llama 3 model via the same LLM instance.

## 3\. Backstory Updating

The update\_backstories(agents, case\_description) function personalizes each agent’s backstory with the current case description, making their responses context-aware.

## 4\. Main Trial Simulation

The run\_trial() function orchestrates the entire simulation:

1. Agent Setup: Calls create\_agents() and updates backstories based on user input for the case description.  
2. Witness Testimonies: Prompts the user to input statements for both defense and prosecution witnesses.  
3. Task Creation: Defines a sequence of courtroom tasks (opening statements, witness cross-examinations, closing statements) assigned to the appropriate agents. Each task includes a description, expected output, agent, model, and base URL.  
4. Crew Execution: Initializes a Crew with all agents and tasks, then runs the simulation with crew.kickoff().  
5. Final Verdicts: After the simulation, prompts the user to enter the jury’s verdict and the judge’s final statement.  
6. Summary Output: Prints a summary of the case, final ruling, and verdict.

## 5\. Program Entry Point

The script runs the run\_trial() function if executed as the main module.

## 6\. Configuration File Reference

The code expects a litellm.config.json file mapping the llama3 model to the local Ollama server, ensuring the LLM interface works correctly2.

## 7\. User Interaction

Throughout, the script interacts with the user for:

* Case description  
* Witness testimonies  
* Final verdicts and judge’s statement

## 8\. Commented Code

There is a commented-out create\_tasks() function, which shows an alternative or earlier approach to defining courtroom tasks.

## 9\. Summary

* Purpose: Simulate a courtroom trial with realistic AI-generated statements and arguments.  
* Technology: CrewAI for agent/task orchestration, Llama 3 via Ollama for language generation.  
* User Role: Initiates the simulation, provides case/witness input, and enters final verdicts.

This explanation provides a high-level overview of each component in uddan.py and how they work together to create an interactive courtroom simulation12.  
