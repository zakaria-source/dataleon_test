from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential

from clients.service_client import ServiceClient


class AzureLanguageServiceClient(ServiceClient):
    """
    Client for interacting with Azure's Language Service for conversation analysis.
    """

    def __init__(self, config):
        """
        Initializes the AzureLanguageServiceClient.

        Args:
            config (Config): Configuration object containing endpoint, key, project_name, and deployment_slot.
        """
        self.endpoint = config.endpoint
        self.key = config.key
        self.project_name = config.project_name
        self.deployment_slot = config.deployment_slot
        self._client = None

    @property
    def client(self):
        """
        Lazily initializes and returns the Azure ConversationAnalysisClient.
        """
        if not self._client:
            self._client = ConversationAnalysisClient(self.endpoint, AzureKeyCredential(self.key))
        return self._client

    def analyze_conversation(self, user_text, language="en"):
        """
        Analyzes text for intents and entities using Azure's conversation analysis service.

        Args:
            user_text (str): The text to analyze.
            language (str, optional): The language of the text. Defaults to "en".

        Returns:
            dict: The analysis result.
        """
        result = self.client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": language,
                        "text": user_text
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": self.project_name,
                    "deploymentName": self.deployment_slot,
                    "verbose": True
                }
            }
        )
        return result
