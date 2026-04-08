from environment import JobEnv
import sys

# Get role input
role = sys.argv[1] if len(sys.argv) > 1 else "backend"

print(f"Selected Role: {role}")

env = JobEnv()
state = env.reset()

actions = ["learn_skill", "improve_resume", "apply"]

total_reward = 0

for step in range(10):

    #  SMART DECISION LOGIC 

    if role.lower() == "backend":
        required_skill = "python"
    elif role.lower() == "frontend":
        required_skill = "javascript"
    else:
        required_skill = "python"

    # Decision making
    if required_skill not in state["skills"]:
        action = "learn_skill"
    elif state["resume_score"] < 0.7:
        action = "improve_resume"
    else:
        action = "apply"

    print(f"\nStep {step+1} → Action: {action}")

    state, reward, done = env.step(action)

    total_reward += reward

    print("State:", state)
    print("Reward:", reward)

    if done:
        print("🎉 SUCCESS: You got the job!")
        break

print("\nFinal Reward:", total_reward)