# Intro to Selenium Testing

## Installation

1. ### linux
  1. Installing python pip (this requires superuser access)
      ```
      sudo apt install python-pip
      ```
  2. Installing selenium
      * open the terminal then install selenium in pip
      ```
      pip install selenium
      ```
      * using requirements.txt
      ```
      pip install -r requirements.txt
      ```

2. ### windows (under construction)

## How to run the program
our base file is the base.py file. you can just do
```
python {file|base.py}
```
to run/execute our codes or
```
python -m unittest {filename|base}
```

#### Drivers (browser engines)
to add/user custom browser engines you need to make it accessible and executable by making sure its in the PATH directory, or you can modify you PATH
* [Firefox (gecko driver)](https://github.com/mozilla/geckodriver/releases)
* [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)


#### Resources
* [Google chrome webdriver documentation](https://sites.google.com/a/chromium.org/chromedriver/getting-started)
* [Python selenium](http://selenium-python.readthedocs.io/)
* [How to install PhantomJS](https://www.vultr.com/docs/how-to-install-phantomjs-on-ubuntu-16-04)
