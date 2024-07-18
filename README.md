# CustomerReviewRatingAnalysis
# Amazon Product Scraper

This project is a web scraper for extracting product information from Amazon. It uses Python, `requests`, and `BeautifulSoup` to scrape product details such as title, price, rating, number of reviews, and availability.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [License](#license)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Update the user agent:**
    - Open the `amazon_scraper.py` file.
    - Replace `'Your User-Agent'` in the `HEADERS` dictionary with your actual user-agent string.

2. **Run the script:**
    ```sh
    python amazon_scraper.py
    ```

3. **Output:**
    - The script will save the scraped data into a CSV file named `amazon_data.csv`.

## Output

The output CSV file `amazon_data.csv` will have the following columns:
- `title`: The title of the product.
- `price`: The price of the product.
- `rating`: The rating of the product.
- `reviews`: The number of user reviews.
- `availability`: The availability status of the product.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

