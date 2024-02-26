Here are the step-by-step instructions to run your Carousell scraping program:

1. **Git Clone:**
   ```
   git clone https://github.com/jiakai2002/Carousell-scraper
   cd Carousell-scraper
   ```
     
2. **Install packages:**
awd
   ```
   pip3 install selenium
   pip3 install beautifulsoup4
   ```
     
3. **Install Chrome:**
   - Either: Install the full-blown google-chrome browser
   OR
   ```
   brew tap homebrew/cask && brew cask install chromedriver
   ```
5. **Run the Program:**
   - Execute the program using Python:
   ```
   python main.py
   ```
   Input the product name, minimum price, and the desired number of listings.

6. **Open the CSV:**
   - If you want to open the CSV file with Excel, run the following command in the terminal or command prompt:
   ```
   start excel filename.csv
   ```
