
print("=== DAY 25: PERSONAL ASSISTANT AI AGENT ===")

class PersonalAssistant:

    def __init__(self):
        self.memory = []

    def calculator(self, a, b):
        return a + b

    def greeting(self, name):
        return f"Hello {name}! How can I help you?"

    def study_advice(self):
        return "Create a timetable and study for 2 hours daily."

    def run(self, task):

        self.memory.append(task)

        print("\nUser Task:", task)

        if task == "greet":
            print(self.greeting("Student"))

        elif task == "calculate":
            print("Calculation Result:", self.calculator(25, 15))

        elif task == "study":
            print("Study Advice:", self.study_advice())

        else:
            print("Sorry, I cannot perform this task.")

    def show_memory(self):
        print("\nAgent Memory:", self.memory)


# Create assistant
assistant = PersonalAssistant()

# Test different tasks
assistant.run("greet")
assistant.run("calculate")
assistant.run("study")

# Display memory
assistant.show_memory()

print("\nDay 25 Project Completed!")
print("AI Agent Module Completed!")
