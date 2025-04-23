from openai_autogen import Agent, Controller, openai

# 1. Configure your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# 2. Define two simple agents
class UserAgent(Agent):
    async def respond(self, message: str) -> str:
        # In a real use you might have custom logic here.
        # For demo, just append a question mark.
        return message + "?"

class AssistantAgent(Agent):
    async def respond(self, message: str) -> str:
        # Here the assistant simply echoes back with a prefix.
        return "Assistant heard: " + message

# 3. Create instances
user = UserAgent(name="user")
assistant = AssistantAgent(name="assistant")

# 4. Build a controller that alternates between them
controller = Controller(agents=[user, assistant], max_turns=4)

# 5. Seed the conversation
controller.seed("Hello, how are you")

# 6. Run the dialogue
async def run_dialogue():
    conversation = await controller.run()
    for turn in conversation:
        print(f"{turn.agent_name}: {turn.content}")

import asyncio
asyncio.run(run_dialogue())
