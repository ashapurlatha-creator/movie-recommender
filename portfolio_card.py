# Import the subprocess module to fetch our real GitHub data
import subprocess


def generate_portfolio_snippet():
    # Fetch the remote URL from Git settings
    repo_url_raw = subprocess.getoutput("git remote get-url origin")
    # Clean the URL to make it a web link
    repo_url = repo_url_raw.replace(".git", "")

    # Define your project 'Pitch'
    project_title = "Movie Recommendation Engine"
    tech_used = "Python, Pandas, Scikit-Learn, Cosine Similarity"
    key_achievement = "Built a content-based filtering engine for 5,000+ movies."

    # Print the formatted 'Portfolio Card'
    print("\n" + "=" * 50)
    print("🚀 YOUR PROFESSIONAL PORTFOLIO SNIPPET 🚀")
    print("=" * 50)
    print(f"Project: {project_title}")
    print(f"URL:     {repo_url}")
    print(f"Stack:   {tech_used}")
    print(f"Impact:  {key_achievement}")
    print("=" * 50)
    print(
        "\n💡 ACTION: Copy the URL above and add it to your LinkedIn 'Featured' section!"
    )


# Run the snippet generator
if __name__ == "__main__":
    generate_portfolio_snippet()
