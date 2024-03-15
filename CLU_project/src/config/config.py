import os

from dotenv import load_dotenv


class Config:
    def __init__(self):
        # Load environment variables from a .env file
        load_dotenv()  # This looks for a .env file and loads its variables

        self.endpoint = os.getenv("ENDPOINT")
        self.key = os.getenv("KEY")
        self.service_type = os.getenv("SERVICE_TYPE", "azure")
        self.project_name = os.getenv("PROJECT_NAME")
        self.deployment_slot = os.getenv("DEPLOYMENT_SLOT", "production")
