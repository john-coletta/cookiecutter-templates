import json
import logging
from typing import Dict, Any

from src.services.{{ cookiecutter.main_service }} import {{ cookiecutter.main_service.title().replace('_', '') }}
from src.utils.logger import setup_logger
from src.utils.decorators import error_handler, validate_input

logger = setup_logger(__name__)


@error_handler
@validate_input
def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    """
    {{ cookiecutter.description }}
    Main Lambda handler for {{ cookiecutter.project_name }}.
    """
    logger.info(f"Processing event: {event}")

    service = {{ cookiecutter.main_service.title().replace('_', '') }}()
    result = service.process(event)

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }