class ConversationHandler:
    """
    Handles user conversations using the LanguageServiceClient.
    """

    def __init__(self, language_service_client):
        """
        Initializes the ConversationHandler with a LanguageServiceClient.

        Args:
            language_service_client (ServiceClient): The service client used for conversation analysis.
        """
        self.language_service_client = language_service_client

    @staticmethod
    def display_analysis_results(result):
        """
        Displays analysis results in a structured and more readable format.

        Args:
            result (dict): The analysis result containing the top intent,
                           entities, and query.
        """
        prediction = result.get("result", {}).get("prediction", {})
        top_intent = prediction.get("topIntent", "No intent detected")
        entities = prediction.get("entities", [])
        intents = prediction.get("intents", [])

        # Simplify finding the intent details
        intent_details = next((intent for intent in intents if intent.get("category") == top_intent), None)

        print(f"\nAnalysis Result:\n- Top Intent: {top_intent}")

        if intent_details:
            print(f"- Intent Category: {intent_details.get('category')}")
            print(f"- Intent Confidence Score: {intent_details.get('confidenceScore')}")
        else:
            print("- Intent details not available.")

        if entities:
            print("\nEntities:")
            for entity in entities:
                category = entity.get('category', 'Unknown category')
                text = entity.get('text', 'No text')
                confidence = entity.get('confidenceScore', 0)
                print(f"  - Category: {category}, Text: {text}, Confidence Score: {confidence}")
        else:
            print("\nNo entities detected.")

        print(f"\nQuery: {result.get('result', {}).get('query', 'No query provided')}")

    def run(self, language="en"):
        """
        Starts processing user input until 'quit' is received.

        Args:
            language (str, optional): The language of the input text. Defaults to "en".
        """
        print("Enter some text to analyze ('quit' to stop):")
        while True:
            user_text = input()

            while not user_text.strip():
                print("The input is empty. Please enter some text to analyze:")
                user_text = input()

            if user_text.lower() == 'quit':
                break
            result = self.language_service_client.analyze_conversation(user_text, language)
            self.display_analysis_results(result)
