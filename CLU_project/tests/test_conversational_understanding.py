from unittest.mock import patch

import pytest

from src.conversational_understanding import LanguageServiceClient

# Données de test
endpoint = "https://test.cognitiveservices.azure.com/"
key = "testkey"


@pytest.fixture
def language_service_client():
    with patch('azure.ai.language.conversations.ConversationAnalysisClient') as MockClient, \
            patch('azure.core.credentials.AzureKeyCredential'):
        client = LanguageServiceClient(endpoint, key)
        client._client = MockClient()  # Utilisation d'un mock pour le client Azure
        yield client


def test_analyze_conversation(language_service_client):
    # Préparer le mock pour retourner une réponse simulée
    expected_intent = "GetRecipe"
    language_service_client._client.analyze_conversation.return_value = {
        "result": {
            "prediction": {
                "topIntent": expected_intent,
                "entities": [{"category": "RecipeName", "text": "chocolate cake"}]
            }
        }
    }

    result = language_service_client.analyze_conversation("How do I make a chocolate cake?")
    assert result["result"]["prediction"]["topIntent"] == expected_intent, "The intent should be GetRecipe"
    assert "chocolate cake" in result["result"]["prediction"]["entities"][0][
        "text"], "Entity text should contain 'chocolate cake'"
