# ==========================================
# AI RECOMMENDATION SYSTEM
# DecodeLabs Project 3
# ==========================================

# Dataset of items with their categories

items = {
    "Python Programming": ["programming", "technology", "coding"],
    "Machine Learning": ["ai", "technology", "data science"],
    "Web Development": ["programming", "website", "coding"],
    "Graphic Design": ["design", "creativity", "art"],
    "Digital Marketing": ["marketing", "business", "social media"],
    "Cyber Security": ["security", "technology", "networking"],
    "Photography": ["art", "creativity", "camera"],
    "Business Analytics": ["business", "data science", "statistics"],
    "Mobile App Development": ["programming", "technology", "apps"],
    "Artificial Intelligence": ["ai", "technology", "machine learning"]
}

print("=" * 50)
print("      AI RECOMMENDATION SYSTEM")
print("=" * 50)

# Take user interests
user_input = input(
    "\nEnter your interests separated by commas\n"
    "(Example: ai, technology, coding): "
)

# Clean input
user_preferences = [
    interest.strip().lower()
    for interest in user_input.split(",")
]

# Calculate similarity score
recommendations = []

for item, features in items.items():

    score = len(
        set(user_preferences).intersection(
            set(feature.lower() for feature in features)
        )
    )

    recommendations.append((item, score))

# Sort by similarity score
recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nRecommended Courses:")
print("-" * 50)

found = False

for item, score in recommendations:

    if score > 0:
        found = True
        print(f"{item}  | Match Score: {score}")

if not found:
    print("No strong matches found.")
    print("Showing popular recommendations:")
    print("\n1. Artificial Intelligence")
    print("2. Python Programming")
    print("3. Machine Learning")

print("\nThank you for using the AI Recommendation System!")