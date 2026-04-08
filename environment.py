import random

class JobEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.candidate = {
            "skills": ["python"],
            "experience": 1,
            "projects": 2,
            "resume_score": 0.5
        }

        self.jobs = [
            {"role": "backend", "required_skills": ["python", "django"], "difficulty": "easy"},
            {"role": "data_analyst", "required_skills": ["sql", "python"], "difficulty": "medium"},
            {"role": "ml_engineer", "required_skills": ["python", "ml"], "difficulty": "hard"}
        ]

        # 🧠 Memory of failed jobs
        self.failed_jobs = []

        return self.state()

    # 🔹 Skill + Experience Matching
    def calculate_match_score(self, job):
        match = 0
        for skill in job["required_skills"]:
            if skill in self.candidate["skills"]:
                match += 1

        skill_score = match / len(job["required_skills"])
        exp_score = min(self.candidate["experience"] / 3, 1)
        project_score = min(self.candidate["projects"] / 5, 1)

        return (0.5 * skill_score +
                0.3 * exp_score +
                0.2 * project_score)

    # 🔹 ATS Filtering
    def ats_filter(self, job):
        score = self.calculate_match_score(job)
        return score > 0.4

    # 🔹 Success Probability
    def get_success_probability(self, job):
        base_score = self.calculate_match_score(job)

        difficulty_factor = {
            "easy": 0.9,
            "medium": 0.6,
            "hard": 0.3
        }

        return base_score * difficulty_factor[job["difficulty"]]

    # 🔹 Main Step Function
    def step(self, action):
        reward = 0
        done = False

        if action == "learn_skill":
            new_skill = random.choice(["django", "sql", "ml"])
            if new_skill not in self.candidate["skills"]:
                self.candidate["skills"].append(new_skill)
                reward = 0.1

        elif action == "improve_resume":
            self.candidate["resume_score"] += 0.1
            reward = 0.05

        elif action == "apply":
            job = random.choice(self.jobs)

            # ⚠️ Avoid repeating failed jobs
            if job["role"] in self.failed_jobs:
                print(f"⚠️ Avoiding previously failed job: {job['role']}")
                return self.state(), -0.05, False

            # 🚫 ATS FILTER
            if not self.ats_filter(job):
                print(f"🚫 Rejected by ATS for {job['role']}")
                self.failed_jobs.append(job["role"])
                return self.state(), -0.2, False

            # 🎯 Interview Stage
            prob = self.get_success_probability(job)

            if random.random() < prob:
                reward = 1.0
                done = True
                print(f"✅ Selected for {job['role']}")
            else:
                reward = -0.1
                self.failed_jobs.append(job["role"])
                print(f"❌ Rejected from {job['role']}")

        return self.state(), reward, done

    # 🔹 State Representation
    def state(self):
        self.candidate["resume_score"] = round(self.candidate["resume_score"], 2)
        return self.candidate