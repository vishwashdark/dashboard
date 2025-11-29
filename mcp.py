from google import genai
from google.genai import types

def search_with_gemini():
    # PASTE YOUR API KEY HERE
    api_key = "AIzaSyCPrzH2NkSoOCmq6zONph0wYBBeAwM03Uk"

    client = genai.Client(api_key=api_key)

    # Create the tool configuration for Google Search
    google_search_tool = types.Tool(
        google_search=types.GoogleSearch()
    )

    prompt = "You are a helpful assistant. Use the Google Search and figure out if the information provided is actually a fake news or what, Trump has signed a memorandum with india to kill osama bin laden"
    print(f"Asking: {prompt}...\n")

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[google_search_tool],
                response_modalities=["TEXT"]
            )
        )

        # Print the text response
        if response.text:
            print("Response:\n" + response.text)

        # Access and print the grounding metadata (sources)
        if response.candidates and response.candidates[0].grounding_metadata:
            metadata = response.candidates[0].grounding_metadata
            if metadata.grounding_chunks:
                print("\nSources used:")
                for chunk in metadata.grounding_chunks:
                    if chunk.web:
                        print(f"- {chunk.web.title}: {chunk.web.uri}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_with_gemini()