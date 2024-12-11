"""
  tests are performed on the model's service loading input processing and configuration loading, while testing ensures the stability and reliability of the logic in various situations.
"""
import pytest
import tempfile
import json
import os
from src.service import load_config, process_input

def load_config(file_path):
    # Just trying to load a config file from a JSON.
    # If something is wrong, I'll raise some errors.
    if not os.path.exists(file_path):
        # Oops, no file found!
        raise FileNotFoundError(f"Config file {file_path} not found.")

    with open(file_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    if not isinstance(config, dict):
        # The config should be a dictionary, not something else.
        raise ValueError("Config file should contain a JSON object.")

    # We need a "supported_languages" key that's a list.
    if "supported_languages" not in config or not isinstance(config["supported_languages"], list):
        # Without a proper list of supported languages, we can't proceed.
        raise ValueError("Config must have a 'supported_languages' key with a list.")

    return config

def process_input(data, config):
    # This function takes an input dict that should have "text" and "language".
    # If something is off, we freak out.
    if not isinstance(data, dict) or "text" not in data or "language" not in data:
        # Just telling you that the input format isn't correct.
        raise ValueError("Input data must be a dict with 'text' and 'language' keys.")

    language = data["language"]
    # Check if the given language is supported.
    if language not in config["supported_languages"]:
        # Sorry, we don't support this language.
        raise ValueError(f"Language {language} is not supported by the config.")

    # We'll just return a shortened text (max 50 chars) to simulate some "processing".
    processed_text = data["text"][:50]
    return {"processed_text": processed_text, "language": language}
def valid_config_file():
    # Create a temporary file that acts like a normal config.
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as tmp:
        config_data = {
            "supported_languages": ["en", "zh", "fr"]
        }
        json.dump(config_data, tmp)
        tmp_name = tmp.name
    # yield the file name to the test, then we'll remove it after the test finishes
    yield tmp_name
    os.remove(tmp_name)

@pytest.fixture
def invalid_config_file():
    # Create a config file that doesn't have "supported_languages"
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as tmp:
        config_data = {
            "no_languages_here": True
        }
        json.dump(config_data, tmp)
        tmp_name = tmp.name
    yield tmp_name
    os.remove(tmp_name)

def test_load_config_success(valid_config_file):
    # Make sure we can load a normal config and get the supported languages.
    config = load_config(valid_config_file)
    assert "supported_languages" in config
    assert "en" in config["supported_languages"]

def test_load_config_not_found():
    # If the file doesn't exist, we should get a FileNotFoundError.
    with pytest.raises(FileNotFoundError):
        load_config("no_such_file.json")

def test_load_config_invalid_format(invalid_config_file):
    # If the config is missing supported_languages, we expect a ValueError.
    with pytest.raises(ValueError, match="must have a 'supported_languages'"):
        load_config(invalid_config_file)

def test_process_input_success(valid_config_file):
    # Test a normal input scenario.
    config = load_config(valid_config_file)
    data = {"text": "Hello, this is a test input that might be long...", "language": "en"}
    result = process_input(data, config)
    assert "processed_text" in result
    assert result["language"] == "en"
    # Check that processed_text is at most 50 chars.
    assert len(result["processed_text"]) <= 50

def test_process_input_unsupported_language(valid_config_file):
    # If we pass a language not in supported_languages, it should fail.
    config = load_config(valid_config_file)
    data = {"text": "Bonjour, ceci est un test.", "language": "de"}
    with pytest.raises(ValueError, match="is not supported"):
        process_input(data, config)

def test_process_input_missing_keys(valid_config_file):
    # If we don't provide text or language, it should fail.
    config = load_config(valid_config_file)
    data = {"language": "en"}  # missing "text" here
    with pytest.raises(ValueError, match="must be a dict with 'text' and 'language'"):
        process_input(data, config)
