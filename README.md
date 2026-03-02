# Zootopia-With-API:

This project generates a simple animals website using data from the API Ninjas Animals API.

The program uses a multi-file architecture:
- `data_fetcher.py` fetches animal data from the API.
- `animals_web_generator.py` generates an HTML website based on that data.

## Installation

Install dependencies:

pip install -r requirements.txt

Create a `.env` file in the root folder and add your API key:

API_KEY=your_api_key_here

## Usage

Run the program:

python3 animals_web_generator.py

Enter an animal name when prompted.  
The program will generate an `animals.html` file with the results.  
If the animal does not exist, a message will be displayed in the generated page.