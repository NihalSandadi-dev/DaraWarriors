import fetch from "node-fetch";

const runtime = {
    handler: async (params) => {
        try {
            const ticker = params.ticker || "SPY"; // Default symbol
            const apiKey = "demo"; // Replace with your actual API key if needed
            const url = `https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=${ticker}&interval=5min&outputsize=compact&apikey=${apiKey}`;
            
            const response = await fetch(url);
            if (!response.ok) {
                return `Error fetching data: ${response.status} ${response.statusText}`;
            }

            const data = await response.json();

            if (!data["Time Series (5min)"]) {
                return "Error: Time Series data not available.";
            }

            // Get the most recent timestamp
            const latestTimestamp = Object.keys(data["Time Series (5min)"])[0];
            const latestClose = data["Time Series (5min)"][latestTimestamp]["4. close"];

            return `The latest closing price for ${ticker} is $${latestClose} (as of ${latestTimestamp}).`;
        } catch (error) {
            return `Error processing stock data: ${error.message}`;
        }
    }
};

export default runtime;
