
print("=== DAY 23: BUILDING A SIMPLE AI AGENT ===")

# Define the agent
class SimpleAgent:

    def __init__(self):
        self.memory = []

    # Understand user input
    def understand(self, task):
        print("\nUnderstanding task:", task)
        self.memory.append(task)

    # Decide an action
    def decide(self, task):
        if "weather" in task.lower():
            return "Check weather information"
        elif "time" in task.lower():
            return "Provide current time information"
        elif "study" in task.lower():
            return "Suggest a study plan"
        else:
            return "Provide general assistance"

    # Perform action
    def act(self, action):
        print("Selected Action:", action)
        print("Action completed!")

    # Run agent
    def run(self, task):
        self.understand(task)
        action = self.decide(task)
        self.act(action)


# Create agent
agent = SimpleAgent()

# Test agent
agent.run("I want a study plan")

print("\nAgent Memory:", agent.memory)
print("\nDay 23 Learning Completed!")
