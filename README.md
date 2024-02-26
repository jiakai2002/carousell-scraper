Here are the step-by-step instructions to run your Carousell scraping program:

1. **Git Clone:**
     ```
     git clone https://github.com/jiakai2002/Carousell-scraper
     cd Carousell-scraper
     ```
     
2. **Install packages:**
     ```
     pip3 install selenium
     pip3 install beautifulsoup4
     ```
     
3. **Download and Prepare ChromeDriver:**
   - Visit the [ChromeDriver Download Page](https://sites.google.com/chromium.org/driver/) and download the ChromeDriver version compatible with your Chrome browser.
   - Extract the ChromeDriver file into the repository directory.

4. **Run the Program:**
   - Execute the program using Python:
     ```bash
     python main.py
     ```
   - Follow the prompts to input the product information, minimum price, and the desired number of listings.

5. **Open the CSV:**
   - If you want to open the CSV file with Excel, run the following command in the terminal or command prompt:
     ```bash
     start excel filename.csv
     ```
