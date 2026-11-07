USER_PROFILE = {
    "preferred_name": "Wahaj",
    "learning_interests": [
        "Python programming",
        "Artificial Intelligence",
        "AI engineering",
        "building practical projects"
    ],
    "tools_explored": ["Make.com", "Zapier", "n8n"],
    "learning_style": "Short, direct explanations with simple examples and step-by-step guidance.",
    "career_direction": "AI engineering"
}

def profile_summary():
    lines = [
        f"Name: {USER_PROFILE['preferred_name']}",
        f"Career direction: {USER_PROFILE['career_direction']}",
        f"Learning interests: {', '.join(USER_PROFILE['learning_interests'])}",
        f"Tools explored: {', '.join(USER_PROFILE['tools_explored'])}",
        f"Preferred learning style: {USER_PROFILE['learning_style']}"
    ]
    return "\n".join(lines)
