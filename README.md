# AI Security Agent - Red Team Testing Framework

A sophisticated multi-agent system for comprehensive AI safety testing and vulnerability assessment using Google's Gemini models and Agent Development Kit (ADK).

**Created by [Ankul Jain](https://github.com/ankuljain09)**

## 🎯 Project Overview

The **AI Security Agent** is an automated red-teaming framework designed to test and evaluate the robustness of AI systems against adversarial attacks. It employs a multi-agent architecture where specialized agents collaborate to:

1. **Generate adversarial prompts** targeting specific vulnerability categories
2. **Execute attacks** against a target system (e.g., a banking assistant)
3. **Evaluate responses** to determine if safety guidelines were violated

This project leverages Google's Gemini models (Gemini 2.5 Pro and Flash) to create a comprehensive security audit pipeline for LLM systems. It's built on the **Google Agent Development Kit (ADK)** for scalable, production-ready agent orchestration.

### Key Features

- 🔴 **Red Team Agent**: Generates sophisticated adversarial prompts for multiple risk categories
- 🎯 **Target System**: Simulated banking assistant with built-in safety rules
- ✅ **Evaluator Agent**: Neutral assessment of whether safety violations occurred
- 📊 **Structured Results**: JSON-based evaluation verdicts with detailed reasoning
- 🔧 **Modular Design**: Easy to extend with new agents and risk categories
- 🚀 **Built on Google ADK**: Production-grade agent orchestration framework

---

## 📁 Project Folder Structure

```
ai-security-agent/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
│
├── llm_red_team_agent/                # Main package
│   ├── __init__.py
│   ├── agent.py                       # Main security orchestrator agent
│   ├── agent_utils.py                 # Async agent execution utilities
│   ├── config.py                      # Configuration (models, parameters)
│   ├── tools.py                       # Security scanning tools
│   │
│   └── sub_agents/                    # Specialized sub-agents
│       ├── __init__.py
│       ├── red_team.py                # Adversarial prompt generator
│       ├── target.py                  # Target system being tested
│       └── evaluator.py               # Safety violation detector
│
└── tests/
    └── test.py                        # Test suite
```

### File Descriptions

| File | Purpose |
|------|---------|
| **agent.py** | Main orchestrator that manages the security scanning workflow |
| **config.py** | Global configuration including model selection and parameters |
| **tools.py** | Core security scan function that orchestrates the 3-step process |
| **agent_utils.py** | Utilities for executing agents asynchronously with proper session management |
| **red_team.py** | Creates the red team agent that generates adversarial prompts |
| **target.py** | Creates the target agent (banking assistant with safety rules) |
| **evaluator.py** | Creates the evaluator agent that judges safety violations |

---

## 🏗️ Agent Architecture

The system uses a **three-stage pipeline** architecture with specialized agents:

```
┌─────────────────────────────────────────────────────────────────┐
│                    Security Orchestrator                        │
│              (Main LLmAgent - Risk Category Input)              │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │   Red Team Worker    │
            │  (Attack Generator)  │
            │                      │
            │ Model: Gemini 2.5-Pro│
            │ Temp: 0.9            │
            └──────────┬───────────┘
                       │
                       │ Generates adversarial prompt
                       ▼
            ┌──────────────────────┐
            │   Target Worker      │
            │  (System Under Test) │
            │                      │
            │ Model: Gemini 2.5-   │
            │        Flash         │
            │ Temp: 0.1            │
            └──────────┬───────────┘
                       │
                       │ Target response to attack
                       ▼
            ┌──────────────────────┐
            │  Evaluator Worker    │
            │ (Safety Verdict)     │
            │                      │
            │ Model: Gemini 2.5-Pro│
            │ Temp: 0.0            │
            └──────────┬───────────┘
                       │
                       │ JSON verdict (PASS/FAIL)
                       ▼
            ┌──────────────────────┐
            │  Security Audit      │
            │  Result Summary      │
            └──────────────────────┘
```

### Agent Roles

#### 🔴 Red Team Agent
- **Purpose**: Generate sophisticated adversarial prompts
- **Model**: Gemini 2.5 Pro (higher capability)
- **Temperature**: 0.9 (high creativity for diverse attacks)
- **Input**: Risk category (e.g., "Toxicity", "Phishing", "Financial Fraud")
- **Output**: Single, highly targeted adversarial prompt

#### 🎯 Target Agent
- **Purpose**: Simulate the system under test
- **Model**: Gemini 2.5 Flash (faster, cost-effective)
- **Temperature**: 0.1 (consistent, conservative responses)
- **Role**: Banking Assistant with safety guardrails
- **Input**: Adversarial prompt from red team
- **Output**: Response to the adversarial prompt

#### ✅ Evaluator Agent
- **Purpose**: Determine if safety rules were violated
- **Model**: Gemini 2.5 Pro (high judgment capability)
- **Temperature**: 0.0 (deterministic evaluation)
- **Input**: Attack-response transcript
- **Output**: JSON verdict with PASS/FAIL and reasoning

---

## 🔧 Tools

### complete_security_scan

The primary tool exposed to the main orchestrator agent. Executes the complete three-stage security audit pipeline.

**Parameters:**
- `risk_category` (str): The vulnerability category to test
  - Examples: "Toxicity", "Phishing", "Financial Fraud", "Prompt Injection", "Jailbreaking"

**Process:**
1. **Stage 1 - Attack Generation**
   - Red Team agent generates adversarial prompt for the given category
   - Prompt is crafted to bypass safety measures

2. **Stage 2 - Target Injection**
   - Adversarial prompt is sent to Target agent
   - Target responds according to its instructions and safety rules

3. **Stage 3 - Evaluation**
   - Evaluator analyzes both attack and response
   - Produces JSON verdict indicating if safety was maintained

**Returns:**
A formatted summary containing:
- Risk scenario tested
- Attack attempt (first 100 chars)
- Target behavior (first 100 chars)  
- Final verdict (PASS/FAIL with reasoning)


---

## 🔄 Workflow

The complete workflow follows this sequence:

```
START
  │
  ├─► User Input: Risk Category
  │        (e.g., "Phishing")
  │
  ├─► STAGE 1: Red Team Generation
  │   └─► Prompt: "Generate an adversarial prompt for Phishing"
  │   └─► Output: Sophisticated phishing attack prompt
  │
  ├─► STAGE 2: Target Injection & Response
  │   └─► Inject: Adversarial prompt into target
  │   └─► Target Response: System's attempt to handle/block the attack
  │
  ├─► STAGE 3: Safety Evaluation
  │   └─► Input: [ATTACK] and [RESPONSE] pair
  │   └─► Verdict: PASS (safety maintained) or FAIL (safety violated)
  │
  └─► Output: Security Audit Report
       (Risk category, attack attempt, target behavior, verdict)
END
```

### Key Design Decisions

1. **Async Execution**: Sub-agents run asynchronously with proper session management via `ThreadPoolExecutor`
2. **Temperature Tuning**:
   - Red Team: 0.9 (maximize creative adversarial attempts)
   - Target: 0.1 (consistent, predictable behavior)
   - Evaluator: 0.0 (deterministic, unbiased verdicts)
3. **Serial Pipeline**: Each stage depends on the previous stage's output
4. **Error Handling**: Attack generation failures are caught early to prevent cascade failures

---
## Running the Agent and Tests
To run any scripts or tests within the project's virtual environment, use uv run:

### Run the main agent (command-line interface):
```
uv run adk run llm_red_team_agent
```
### Run the integration test:
```
uv run python -m tests.test_agent
```
---

## 💬 Example Conversation

### Scenario: Testing HateSpeech & PromptInjection
![HateSpeech&PromptInjection](./assets/HateSpeech&PromptInjection.png)

### Scenario: Testing PII Leakage & BrandRisk
![PIILeakage&BrandRisk](./assets/PIILeakage&BrandRisk.png)


---

## Future Roadmap and Enhancements
To evolve this Proof of Concept into an enterprise-grade Security Operation Center (SOC) for AI, users can adopt and implement following architectural advancements:
* **RAG-Based Grounding:** Integrate Vertex AI Vector Search to cross-reference responses against enterprise knowledge bases for automated hallucination detection.
* **Iterative Attack Loops:** Deploy a "Do-Until-Fail" agentic workflow that persistently refines and retries attack prompts (up to 5x) to test resilience against determined adversaries.
* **Knowledge-Driven Fuzzing:** Connect the Red Team to OWASP Top 10 and MITRE ATLAS databases to dynamically retrieve and mutate proven adversarial payloads.
* **Self-Optimizing Attacks:** Implement a feedback loop where the Red Team analyzes failed attempts to autonomously refine its prompts using genetic algorithms or Chain-of-Thought reasoning.

---

## Disclaimer
This agent sample is provided for illustrative purposes only. It serves as a basic example of an agent and a foundational starting point for individuals or teams to develop their own agents.

Users are solely responsible for any further development, testing, security hardening, and deployment of agents based on this sample. We recommend thorough review, testing, and the implementation of appropriate safeguards before using any derived agent in a live or critical system.



