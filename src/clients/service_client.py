from abc import ABC, abstractmethod


class ServiceClient(ABC):
    """
    Abstract base class for service clients.
    """

    @abstractmethod
    def analyze_conversation(self, user_text, language):
        """
        Analyzes text for intents and entities.

        Args:
            user_text (str): The text to analyze.
            language (str): The language of the text.
        """
        pass
