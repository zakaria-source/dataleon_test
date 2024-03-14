from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential


class LanguageServiceClient:
    """
    A client for interacting with the Azure Language Service.
    It provides methods to perform conversation analysis using Azure's AI capabilities.
    """

    def __init__(self, endpoint, key):
        """
        Initializes the LanguageServiceClient with the necessary credentials.

        :param endpoint: The Azure service endpoint URL.
        :param key: The subscription key for authentication.
        """
        self.endpoint = endpoint
        self.key = key
        self._client = None

    @property
    def client(self):
        """Lazily initializes and returns the Azure ConversationAnalysisClient."""
        if not self._client:
            self._client = ConversationAnalysisClient(self.endpoint, AzureKeyCredential(self.key))
        return self._client

    def analyze_conversation(self, user_text):
        """
        Analyzes the given text to extract intents and entities using Azure's conversation analysis service.

        param user_text: The user input text to analyze.
        :return: The analysis result from Azure Language Service.
        """
        cls_project = 'CookingIntentDetector'
        deployment_slot = 'production'
        with self.client:
            result = self.client.analyze_conversation(
                task={
                    "kind": "Conversation",
                    "analysisInput": {
                        "conversationItem": {
                            "participantId": "1",
                            "id": "1",
                            "modality": "text",
                            "language": "en",
                            "text": user_text
                        },
                        "isLoggingEnabled": False
                    },
                    "parameters": {
                        "projectName": cls_project,
                        "deploymentName": deployment_slot,
                        "verbose": True
                    }
                }
            )
        return result


class ConversationHandler:
    """
    Handles user conversations, processing input through the LanguageServiceClient
    and providing appropriate responses based on the analyzed intents and entities.
    """

    def __init__(self, language_service_client):
        """
        Initializes the ConversationHandler with a LanguageServiceClient.

        :param language_service_client: An instance of LanguageServiceClient for conversation analysis.
        """
        self.language_service_client = language_service_client

    def get_cooking_instructions(self, recipe_name):
        """
        Retrieves cooking instructions for the specified recipe name.

        :param recipe_name: The name of the recipe to get instructions for.
        :return: Cooking instructions as a string.
        """
        recipe_name = recipe_name.lower()
        if recipe_name in recipes_db:
            return recipes_db[recipe_name]
        else:
            return "Recipe not found. Please make sure you've entered the correct recipe name."

    def run(self):
        """Starts the conversation handler, processing user input until 'quit' is received."""
        user_text = ''
        while user_text.lower() != 'quit':
            user_text = input('\nEnter some text about cooking ("quit" to stop)\n')
            if user_text.lower() != 'quit':
                result = self.language_service_client.analyze_conversation(user_text)
                top_intent = result["result"]["prediction"]["topIntent"]
                entities = result["result"]["prediction"]["entities"]
                print("Top intent:")
                print("\tIntent: {}".format(top_intent))
                if top_intent == "GetRecipe":
                    recipe_name = next((entity["text"] for entity in entities if entity["category"] == "RecipeName"),
                                       None)
                    if recipe_name:
                        instructions = self.get_cooking_instructions(recipe_name)
                        print(f"\nCooking instructions for {recipe_name}:")
                        print(instructions)
                    else:
                        print("Recipe name not found in the query.")
                else:
                    print("No cooking-related intent found.")


if __name__ == "__main__":
    # These could be loaded from environment variables or configuration files
    endpoint = "https://intentrecipient.cognitiveservices.azure.com/"
    key = "cb2cf2da045d44edb4118e4ec2c4c9ba"
    language_service_client = LanguageServiceClient(endpoint, key)
    conversation_handler = ConversationHandler(language_service_client)
    conversation_handler.run()
