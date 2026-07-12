from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    
    database_host : str
    database_name : str
    database_user : str
    database_pwd : str
    database_port : str
    client_provider : str
    client_api : str
    client_model : str

    model_config = {"env_file": str(BASE_DIR / ".env")}


settings = Settings()