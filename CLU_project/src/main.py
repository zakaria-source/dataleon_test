from clients.azure_language_service_client import AzureLanguageServiceClient
from config.config import Config
from handlers.conversation_handler import ConversationHandler


def create_service_client(config):
    """
    Create a service client based on the provided configuration.

    Args:
        config (Config): The configuration object.

    Returns:
        ServiceClient: An instance of the appropriate service client.

    Raises:
        ValueError: If the provided service type is unsupported.
    """
    if config.service_type == "azure":
        return AzureLanguageServiceClient(config)
    else:
        raise ValueError("Unsupported service type")


if __name__ == "__main__":
    """
    Main function to initialize and run the conversation handler.
    """
    config = Config()
    service_client = create_service_client(config)
    conversation_handler = ConversationHandler(service_client)
    conversation_handler.run()
