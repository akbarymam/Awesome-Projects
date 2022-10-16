# Car Desirability Analysis

### Python based Miniproject implementing KNN and Apriori Algorithm on "Car Evaluation Dataset"

## Languages Used
1. Python (Backend)
2. HTML (Frontend)
3. CSS3 (Frontend)
4. JavaScript (Frontend)

## Frameworks & Libraries Used:
1. Flask
2. Pandas
3. Numpy
4. Arules
5. Scikit-learn
6. Selenium

## How to Setup:
1. Clone this repo
2. Open repo folder in Terminal/PS
3. Create virtual-env (Assuming Python3 installed) `python -m venv venv`
4. Activate virtual-env (Windows) `.\venv\Scripts\activate` or (Linux) `. venv/bin/activate`
5. Run `pip install -r requirements.txt`
6. Download: [Arules](https://drive.google.com/file/d/1QMkk7B7hfaWkuecpCc0TQIKP7vtfVPtD/view?usp=sharing) and extract into `venv\lib\site-packages\` (replace existing files).
7. Run `python car_evaluation.py`
8. The project will be available at `localhost:5000`

## Selenium Testing:
1. For Selenium testing, you'll need Selenium Firefox driver: [Geckodriver](https://github.com/mozilla/geckodriver/releases/) installed, and on `PATH`.
2. Alternately, you can use Selenium Chrome driver: [ChromeDriver](https://chromedriver.storage.googleapis.com/index.html) installed, and on `PATH` as well. In this case, you'll have to change code from [webdriver.Firefox()](https://github.com/Athi223/car_evaluation_knn_apriori/blob/main/selenium_testing.py#L8) to `webdriver.Chrome()`.

# [Dataset](https://archive.ics.uci.edu/ml/datasets/car+evaluation)

This project implements KKN to predict the Acceptability of a Car having input features based on model trained using the above dataset. It also briefs the factors leading to each of the decisions ( Unacceptable, Acceptable Good `Preferred` & VGood `Optimal` ) using Apriori Algorithm.
