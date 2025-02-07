import requests
import logging

"""
Utility class For fetching api data from Numbers API
"""

logger = logging.getLogger(__name__)

class ExternalAPIError(Exception):
  """
  Custom Exception Handler
  """
  pass


def FetchNumberAPI(number, timeout = 10):
  """
  Fetch Numbers API and raise ExternalAPIError
  """
  url = f"http://numbersapi.com/{number}/math?json"
  try:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()

    return response.json()
  
  except requests.RequestException as e:
    logger.error(f"Error fetching API: {e}")
    raise ExternalAPIError("Failed to fetch Data!")