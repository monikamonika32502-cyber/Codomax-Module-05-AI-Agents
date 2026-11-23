
print("=== DAY 24: AI AGENT WITH TOOLS ===")

class AIAgent:

    def calculator(self, a, b):
        return a + b

    def greeting_tool(self, name):
        return "Hello " + name + "! Welcome to AI Agents."

    def run(self, task):

        if task == "calculate":
            result = self.calculator(10, 20)
            print("Calculator Tool Result:", result)

        elif task == "greet":
            result = self.greeting_tool("Student")
            print("Greeting Tool Result:", result)

        else:
            print("No suitable tool found.")


agent = AIAgent()

print("\n1. Testing Calculator Tool")
agent.run("calculate")

print("\n2. Testing Greeting Tool")
agent.run("greet")

print("\nDay 24 Learning Completed!")
