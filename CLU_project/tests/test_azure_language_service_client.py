import pytest

from clients.azure_language_service_client import AzureLanguageServiceClient
from config.config import Config


@pytest.fixture
def azure_client():
    """
    Fixture to initialize the Azure Language Service Client.
    """
    config = Config()  # This loads the ENDPOINT and KEY from environment variables
    return AzureLanguageServiceClient(config)


def test_azure_language_service_client(azure_client):
    """
    Test the Azure Language Service Client setup and request sending.
    """
    user_text = "Hello, how are you?"
    result = azure_client.analyze_conversation(user_text)

    assert "result" in result
    assert "prediction" in result["result"]
    assert "topIntent" in result["result"]["prediction"]


def test_get_recipe(azure_client):
    """
    Test getting a specific recipe.
    """
    user_text = "How do I make lasagna?"
    result = azure_client.analyze_conversation(user_text)
    assert result.get("result").get("prediction").get("topIntent") == "GetRecipe"


def test_get_nutritional_info(azure_client):
    """
    Test getting nutritional information.
    """
    user_text = "What are the calories in spaghetti carbonara?"
    result = azure_client.analyze_conversation(user_text)
    assert result.get("result").get("prediction").get("topIntent") == "GetNutritionalInfo"


def test_get_recipe_by_ingredients(azure_client):
    """
    Test getting recipe suggestions based on specific ingredients.
    """
    user_text = "What can I cook with eggs and flour?"
    result = azure_client.analyze_conversation(user_text)
    assert result.get("result").get("prediction").get("topIntent") == "GetRecipeByIngredients"


def test_cooking_advice(azure_client):
    """
    Test asking for cooking advice.
    """
    user_text = "How do I keep food from sticking to the pan?"
    result = azure_client.analyze_conversation(user_text)
    assert "CookingAdvice" in result.get("result").get("prediction").get("topIntent")


def test_ingredient_substitution(azure_client):
    """
    Test asking for ingredient substitution.
    """
    user_text = "What can I use instead of milk in this recipe?"
    result = azure_client.analyze_conversation(user_text)
    assert "GetRecipeByIngredients" in result.get("result").get("prediction").get("topIntent")


def test_specific_cooking_technique(azure_client):
    """
    Test asking about specific cooking techniques.
    """
    user_text = "What does it mean to blanch vegetables?"
    result = azure_client.analyze_conversation(user_text)
    assert "CookingTechnique" in result.get("result").get("prediction").get("topIntent")


def test_recipes_for_dietary_restrictions(azure_client):
    """
    Test asking for recipes adapted to dietary restrictions.
    """
    user_text = "Can you give me a vegetarian pasta recipe?"
    result = azure_client.analyze_conversation(user_text)
    assert "GetRecipe" in result.get("result").get("prediction").get("topIntent")
