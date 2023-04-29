import openai
import time

# Set up OpenAI API credentials
openai.api_key = "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"

# Define a function to generate a response to a prompt


def generate_response(prompt):
    # Set up OpenAI API request parameters
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the response text from the API response
    message = completions.choices[0].text.strip()

    return message

# Define a function to interact with the user and generate responses


def therapist():
    # Greet the user and ask for their first prompt
    print("Hello! I'm here to listen. What's on your mind?")
    prompt = input("> ")
    prompt = "Respond like a professional therapist to the user for the the issue\"" + \
        prompt+"\" Give answer in points"

    while prompt != "quit":
        # Generate a response to the user's prompt
        response = generate_response(prompt)

        # Display the response to the user
        print(response)

        # Ask for the next prompt
        prompt = input("> ")

        # Pause briefly to avoid hitting the API rate limit
        time.sleep(0.5)

    # Say goodbye to the user
    print("Goodbye! Take care of yourself.")


# Call the therapist function to start the program
therapist()
