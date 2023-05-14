# MILENKO WAS HERE

## This is a fork of https://github.com/GrilledLambda/NeweggAutoPurchaseBot
## I stopped working on this at some point, have a look at the Selenium documentation if you're interested in continuing development
* https://selenium-python.readthedocs.io/navigating.html?highlight=value#filling-in-forms

## Linux version w/ targeting for a specific aftermarket 4090.
* You need to install `chromium` for your Linux distribution and replace the `chromedriver` binary in `ChromeWebDriver/` with the corresponding version from [here](https://sites.google.com/chromium.org/driver/downloads).

# Newegg Auto Purchase Bot

This is a auto-purchase bot that uses selenium and HTTP requests to check for available products on NewEgg. All the settings you need to configure will be in BotSettings.py Check the requirements folder for dependencies.  

Once you are done configuring the settings in BotSettings.py, open an elevated CMD, navigate to the Requirements folder directory, and run the following command to automatically install dependencies:  
```
 pip3 install -r requirements.txt
```
After that you are good to go. 
Just run `ScanPages.py`
#
Please report any bugs you find.  

**WARNING:** Run this at your own risk. I am unsure whether or not this violates Newegg's terms.

