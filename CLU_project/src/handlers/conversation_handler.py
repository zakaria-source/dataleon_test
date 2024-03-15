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
        Displays analysis results in a structured format.

        Args:
            result (dict): The analysis result.
        """
        top_intent = result["result"]["prediction"]["topIntent"]
        entities = result["result"]["prediction"]["entities"]
        print("\nAnalysis Result:\nTop Intent:", top_intent)

        intent_details = next(
            (intent for intent in result["result"]["prediction"]["intents"] if intent["category"] == top_intent), None)
        if intent_details:
            print("Intent Category:", intent_details["category"])
            print("Intent Confidence Score:", intent_details["confidenceScore"])
        else:
            print("Intent details not available.")

        print("\nEntities:")
        for entity in entities:
            print(
                f"- Category: {entity['category']}, Text: {entity['text']}, Confidence Score: {entity['confidenceScore']}")

        print("\nQuery:", result["result"]["query"])

    def run(self, language="en"):
        """
        Starts processing user input until 'quit' is received.

        Args:
            language (str, optional): The language of the input text. Defaults to "en".
        """
        print("Enter some text to analyze ('quit' to stop):")
        while True:
            user_text = input()
            if user_text.lower() == 'quit':
                break
            result = self.language_service_client.analyze_conversation(user_text, language)
            self.display_analysis_results(result)
