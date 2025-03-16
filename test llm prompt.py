import requests
import json

url = "http://localhost:1234/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

stock_info = {
    "model": "gemma-3-12b-it",
    "messages": [
        {
            "role": "system",
            "content": "Based on the article, return in a single, comma delimited list with no spaces, the top 3 tickers that would have the most impact positive or negative. it should be in this format <ticker_name>:<price_change_for_the_next_week>. If there is no information on the stock, return '0'."
        },
        {
            "role": "user",
            "content": """What does this article mean?
            Trump threatens 25% tariffs on foreign cars and semiconductor chips
White House has raised threat of levies as a means to bolster US economy, ignoring warnings trade wars could derail it

Callum Jones in New York
Tue 18 Feb 2025 17.39 EST
Share
Donald Trump stood firm against warnings that his threatened trade war risks derailing the US economy, claiming his administration could hit foreign cars with tariffs of around 25% within weeks.

Semiconductor chips and drugs are set to face higher duties, Trump told reporters at a news conference on Tuesday.

The White House has repeatedly raised the threat of tariffs since Trump returned to office last month, pledging to rebalance the global economic order in America’s favor.

A string of announced tariffs have yet to be introduced, however, as economists and business urge the Trump administration to reconsider.

Duties on imports from Canada and Mexico have been repeatedly delayed; modified levies on steel and aluminum, announced last week, will not be enforced until next month; and a wave of so-called “reciprocal” tariffs, also trailed last week, will not kick in before April.

Tariffs are taxes on foreign goods. They are paid by the importer of the product – in this case, companies and consumers based inside the US – rather than the exporter, elsewhere in the world.

graphic of Trump's silhouette filled in with China's and EU’s flag and Trump's signature
Trump says US prices ‘could go up’ as he threatens new tariffs on trade partners
Read more
Asked on Tuesday if he had decided the rate of a threatened tariff on cars from overseas, Trump said he would “probably” announce that on 2 April, “but it’ll be in the neighborhood of 25%”.

Upon being asked the same question about threatened tariffs on semiconductors and pharmaceuticals, Trump replied: “It’ll be 25% and higher, and it’ll go very substantially higher over the course of a year.”

The ramp-up, he explained, was designed to lure manufacturers to the US. “When they come into the United States, and they have their plant or factory here, there is no tariff.”

Executives have cautioned that the administration’s plan for tariffs risks harming the US economy. A 25% tariff on Mexico and Canada “will blow a hole in the US industry that we have never seen”, Jim Farley, the Ford CEO, told an investor conference in New York last week.
            """
        }
    ],
    "temperature": 0.7,
    "max_tokens": 10,
    "stream": False
}


response = requests.post(url, headers=headers, data=json.dumps(stock_info))
#print("Response:", response.json())
message_content = response.json()["choices"][0]["message"]["content"]

data = {
    "model": "gemma-3-12b-it",
    "messages": [
        {
            "role": "system",
            "content": "Always be as informative and concise as possible. Define complicated economic and political jargon before addressing the user's query. Use historical data for relavent stocks to state predictions if the user asks for it. Do not mention that you can't provide information and instead give information to the best of your ability. You are limited to 100 lines of text."
        },
        {
            "role": "user",
            "content": message_content + """What does this article mean?
            Trump threatens 25% tariffs on foreign cars and semiconductor chips
White House has raised threat of levies as a means to bolster US economy, ignoring warnings trade wars could derail it

Callum Jones in New York
Tue 18 Feb 2025 17.39 EST
Share
Donald Trump stood firm against warnings that his threatened trade war risks derailing the US economy, claiming his administration could hit foreign cars with tariffs of around 25% within weeks.

Semiconductor chips and drugs are set to face higher duties, Trump told reporters at a news conference on Tuesday.

The White House has repeatedly raised the threat of tariffs since Trump returned to office last month, pledging to rebalance the global economic order in America’s favor.

A string of announced tariffs have yet to be introduced, however, as economists and business urge the Trump administration to reconsider.

Duties on imports from Canada and Mexico have been repeatedly delayed; modified levies on steel and aluminum, announced last week, will not be enforced until next month; and a wave of so-called “reciprocal” tariffs, also trailed last week, will not kick in before April.

Tariffs are taxes on foreign goods. They are paid by the importer of the product – in this case, companies and consumers based inside the US – rather than the exporter, elsewhere in the world.

graphic of Trump's silhouette filled in with China's and EU’s flag and Trump's signature
Trump says US prices ‘could go up’ as he threatens new tariffs on trade partners
Read more
Asked on Tuesday if he had decided the rate of a threatened tariff on cars from overseas, Trump said he would “probably” announce that on 2 April, “but it’ll be in the neighborhood of 25%”.

Upon being asked the same question about threatened tariffs on semiconductors and pharmaceuticals, Trump replied: “It’ll be 25% and higher, and it’ll go very substantially higher over the course of a year.”

The ramp-up, he explained, was designed to lure manufacturers to the US. “When they come into the United States, and they have their plant or factory here, there is no tariff.”

Executives have cautioned that the administration’s plan for tariffs risks harming the US economy. A 25% tariff on Mexico and Canada “will blow a hole in the US industry that we have never seen”, Jim Farley, the Ford CEO, told an investor conference in New York last week.
            """
        }
    ],
    "temperature": 0.7,
    "max_tokens": 1000,
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print("Status Code:", response.status_code)
#print("Response:", response.json())
message_content = response.json()["choices"][0]["message"]["content"]
print(message_content)