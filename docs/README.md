# Azure Language Service Client

The Azure Language Service Client is a Python client for utilizing Azure's powerful Conversation Analysis service.
It enables you to analyze text for intents and entities, leveraging Azure's advanced language processing capabilities.

## Prerequisites

Before you begin, ensure you have the following:

- **Azure Subscription**: An active Azure subscription is required to access the Conversation Analysis service.
- **Azure Language Service Resource**: Access to the Azure Language Service, with the necessary credentials (endpoint
  and key).
- **Python Environment**: Python 3.x installed on your machine.

## Installation

1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/zakaria-source/dataleon_CLU_test.git
   cd dataleon_CLU_test
   ```

2. **Set up a Virtual Environment** (recommended):
    - For macOS/Linux:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```
    - For Windows:
      ```cmd
      python -m venv .venv
      .\.venv\Scripts\activate
      ```

3. **Install Dependencies**:
   Ensure `requirements.txt` includes `azure-language-service-client` and other necessary packages.
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Configure the client with your Azure Language Service credentials by creating a `.env` file in your project's root
directory:

```plaintext
AZURE_LANGUAGE_SERVICE_ENDPOINT=<your_endpoint_here>
AZURE_LANGUAGE_SERVICE_KEY=<your_key_here>
SERVICE_TYPE=<your_service_type_here>
PROJECT_NAME=<your_project_name_here>
DEPLOYMENT_SLOT=<your_deployment_slot_here>
```

By abstracting the service client, the SERVICE_TYPE in this case should be set to "azure".

## Usage

Example of analyzing text:

```python
from azure_language_service_client import AzureLanguageClient

client = AzureLanguageClient()
text = "Hello, how can I help you today?"
result = client.analyze_text(text)
print(result)
```

## Running Tests

Ensure `pytest` is listed in `requirements.txt`. To run tests, execute:

```bash
pytest
```

Note: Since the tests in my case pertain to cooking recipes, they heavily rely on my model. Therefore, tests may fail if
you use your own model, which could differ from mine based on how you've defined your intents, entities, and utterances.
If you aim to pass all the tests, you should use my endpoint, my API key, my project name, and my deployment slot.

## Support

For assistance or to report issues, please open an issue on the project's GitHub page.

