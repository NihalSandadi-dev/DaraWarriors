# DaraWarriors
repo for the AI hackathon

## Stock Impact Analysis API Client

### Overview

This script interacts with a local API endpoint to analyze news articles and determine the stocks most impacted by the article's content. The script extracts the top three stock tickers along with their projected price changes based on the given article.

### Requirements

- Python 3.x
- requests library
- A locally hosted AI model running at `http://localhost:1234/v1/chat/completions`

### Installation

Ensure you have Python installed and install the required package by running:

```
pip install requests
```

### Usage

Modify the url variable to match your API endpoint if needed:

`url = "http://localhost:1234/v1/chat/completions"`

The script sends a JSON request containing:

1. The AI model to use (gemma-3-12b-it)

2. A system prompt defining the response format

3. A news article for analysis

4. The API processes the request and returns a response containing stock tickers and their predicted price changes.

### Example Output

The script will return a comma-separated list of stock tickers and their projected price changes in the format:

`AAPL:+3.5,TSLA:-2.1,AMD:+4.2`

If no stock information is available, the response will be:

`0`

### Code Structure
- Sends an initial request with the article and extracts the most impacted stock tickers.
- Uses the extracted information to generate a refined response, providing further context based on economic and historical data.
- Prints the final response.

### Error Handling
- If the API call fails, ensure the server is running at the specified url.
- Handle missing JSON keys in the response to avoid runtime errors.

### Future Enhancements
- Implement exception handling for network failures.
- Allow dynamic API endpoints via command-line arguments.
- Support additional AI models and parameter tuning.

