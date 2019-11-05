# python-ebay-scraper

## Description

It can scrape through Ebay to find the results of the item you need inside the given budget limit provided inside the 
CSV file named *inventory.csv*.

### Setup

1. Install virtual environment
   ```console
   pip install virtualenv
   ```
2. Create a virtual environment inside your project directory
   ```console
   virtualenv -p python3 (NameOfYourEnvironment e.g. venv)
   ```

3. Activate that virtual environment
	```console
    source (ProjectDirectory)/venv/bin/activate
	```
4. Install the packages
    ```console
    pip install bs4
    pip install requests
	```
5. Execute the code.
	```console
    python3 ebay.py
	```

### Libraries Used

1. **bs4:** Because it works with * *Python3* * and is faster and has more features.
2. __**requests:**__ Beacause the user can add content like headers, form data and parameters
using simple Python libraries.
3. **csv:** To read and write tabular data in CSV format.
4. **re:** Provides regular expression matching operations.
4. **operator:** Exports a set of functions corresponding to the intrinsic operators of Python
 