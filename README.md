# Carousell Web Scraper

<img width="705" alt="Screenshot 2024-10-07 at 1 49 56 AM" src="https://github.com/user-attachments/assets/f25bc628-43b7-4770-b03a-cdf1c3de8385">

<img width="1393" alt="Screenshot 2024-10-07 at 1 49 16 AM" src="https://github.com/user-attachments/assets/d80336ec-d0f3-487f-87f7-1312e711f914">

## Overview

This Carousell Web Scraper is a tool designed to automate the process of gathering product listings from the Carousell marketplace. The scraper generates a CSV file containing essential information about each listing, including seller details, listing date, product title, price, condition, and a link to buy the item.

## Features

- Input parameters prompted by the script:
  - Product name
  - Minimum price
  - Number of listings to retrieve
- Output: 
  - A CSV file containing:
    - Seller Name
    - Listing Date
    - Title
    - Price
    - Condition
    - Link to Buy

## Requirements

Before running the scraper, ensure you have the following installed:

- Python 3.x
- Required Python packages (specified in `requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open your terminal or command prompt.
2. Navigate to the directory where the scraper is located.
3. Run the scraper with the following command:

   ```bash
   python scraper.py
   ```

4. The script will prompt you to enter:
   - Product Name
   - Minimum Price
   - Number of Listings

5. The scraper will generate a CSV file named `listings.csv` containing the retrieved listings.

## Output

The output CSV file (`listings.csv`) will include the following columns:

- **Seller Name**: The name of the seller.
- **Listing Date**: The date the listing was created.
- **Title**: The title of the listing.
- **Price**: The price of the product.
- **Condition**: The condition of the item (e.g., new, used).
- **Link to Buy**: The direct link to the listing for purchase.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Carousell community for providing a platform for buying and selling items.
- Special thanks to the libraries and tools that made this project possible.
