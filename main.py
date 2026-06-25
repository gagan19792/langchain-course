from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

def main():
    print("Hello from langchain-course!")
    print("Loading environment variables from .env file...")
    if not os.getenv("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set. Please set it in your .env file.")
    else:
        print(os.getenv("OPENAI_API_KEY"))

if __name__ == "__main__":
    main()
