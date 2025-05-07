from agents.base_agent import run_agent

if __name__ == "__main__":
    query = input("Ask your agent: ")
    result = run_agent(query)
    print("🧠 Agent response:", result)

