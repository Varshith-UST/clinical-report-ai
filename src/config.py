"""
Configuration Management
Central place for all system settings
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Central configuration for the entire system"""
    
    # Project Paths
    BASE_DIR = Path(__file__).parent.parent
    SRC_DIR = BASE_DIR / "src"
    DATA_DIR = BASE_DIR / "data"
    TESTS_DIR = BASE_DIR / "tests"
    DOCS_DIR = BASE_DIR / "docs"
    LOGS_DIR = BASE_DIR / "logs"
    
    # Data Paths
    REPORTS_PATH = DATA_DIR / "reports"
    GUIDELINES_PATH = DATA_DIR / "guidelines"
    CHROMADB_PATH = DATA_DIR / "chromadb"
    
    # Create directories if they don't exist
    for path in [DATA_DIR, REPORTS_PATH, GUIDELINES_PATH, CHROMADB_PATH, LOGS_DIR]:
        path.mkdir(parents=True, exist_ok=True)
    
    # Environment
    ENV = os.getenv("ENV", "development")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    VERBOSE = os.getenv("VERBOSE", "True").lower() == "true"
    
    # API Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY and ENV == "production":
        raise ValueError("GEMINI_API_KEY not found in .env")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"
    LOG_FILE = LOGS_DIR / f"clinical_report_{os.getenv('LOG_DATE', 'app')}.log"
    
    # RAG Configuration
    CHUNK_SIZE = 300
    CHUNK_OVERLAP = 50
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"
    EMBEDDING_DIMS = 384
    TOP_K_RETRIEVAL = 3
    
    # API Configuration
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", 30))
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
    CACHE_RESULTS = os.getenv("CACHE_RESULTS", "True").lower() == "true"
    
    # CrewAI Configuration
    PROCESS_TYPE = "sequential"
    MEMORY_ENABLED = True

# Export config for easy import
config = Config()

if __name__ == "__main__":
    print("Configuration loaded successfully")
    print(f"   Base directory: {Config.BASE_DIR}")
    print(f"   Data directory: {Config.DATA_DIR}")
    print(f"   Logs directory: {Config.LOGS_DIR}")
