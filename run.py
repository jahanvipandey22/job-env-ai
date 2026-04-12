from environment import JobEnv
import sys

def run_simulation(role):
    output = ""

    output += f"Selected Role: {role}\n\n"

    env = JobEnv()
    state = env.reset()

    total_reward = 0

    for step in range(10):

        # SMART DECISION LOGIC
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

        output += f"\nStep {step+1} → Action: {action}\n"

        state, reward, done = env.step(action)

        total_reward += reward

        output += f"State: {state}\n"
        output += f"Reward: {reward}\n"

        if done:
            output += "🎉 SUCCESS: You got the job!\n"
            break

    output += f"\nFinal Reward: {total_reward}\n"

    return output


# This part keeps CLI working (for your local testing)
if __name__ == "__main__":
    role = sys.argv[1] if len(sys.argv) > 1 else "backend"
    print(run_simulation(role))s