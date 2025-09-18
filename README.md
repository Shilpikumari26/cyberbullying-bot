README.md -- ## 📂 Project Structure


cyberbullying-bot/
│── data/
│    └── cyberbullying_tweets.csv      # Dataset (from Kaggle)
│── models/
│    ├── model.pkl                     # Trained ML model
│    └── vectorizer.pkl                # TF-IDF vectorizer
│── src/
│    ├── preprocess.py                 # Text cleaning functions
│    ├── train.py                      # Training script
│    ├── service.py                    # Prediction service
│    └── bot.py                        # Telegram bot code
│── requirements.txt                   # Python dependencies
│── README.md                          # Project documentation


---

## ✨ Features

* 🧹 Text Preprocessing: Cleans raw tweets (removes links, mentions, special chars).
* 🤖 Machine Learning Model: Logistic Regression trained with **TF-IDF features.
* 🔍 Binary Classification: Detects messages as **bullying or safe.
* 💬 Telegram Bot Integration: Users can interact with the model directly in Telegram.
* 📊 Evaluation Report: Prints precision, recall, F1-score on test data.

---

## 📊 Dataset

* Source: [Cyberbullying Tweets Dataset](https://www.kaggle.com/datasets/noyeemhossain135/cyberbullying-tweets)
* Contains tweets labeled as different types of cyberbullying (e.g., age, **gender, **religion) and non-bullying tweets.
* For this project, all bullying types are merged into a single bullying class, and others are labeled safe.

---

## ⚙ Installation & Setup

### 1. Clone this repo

bash
git clone https://github.com/your-username/cyberbullying-bot.git
cd cyberbullying-bot


### 2. Create virtual environment (optional but recommended)

bash
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows


### 3. Install dependencies

bash
pip install -r requirements.txt


---

## 🏋‍♂ Training the Model

1. Place the Kaggle dataset file (cyberbullying_tweets.csv) in the data/ folder.
2. Run training:

bash
cd src
python train.py


3. This will:

   * Clean and preprocess the tweets.
   * Train a Logistic Regression model.
   * Save model.pkl and vectorizer.pkl into models/.

---

## 🤖 Running the Telegram Bot

1. Create a bot using [BotFather](https://t.me/botfather) on Telegram and copy the API token.
2. Open src/bot.py and replace:

python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"


with your actual token.

3. Start the bot:

bash
python bot.py


4. Open Telegram, search your bot, and send a message. Example:


👤 User: You're such a loser!
🤖 Bot: ⚠ Bullying detected! (confidence: 0.83)


---

## 📑 Example Output

After training, the console will show a classification report like:


              precision    recall  f1-score   support
     bullying       0.90      0.88      0.89      1200
         safe       0.87      0.89      0.88      1100
    accuracy                           0.89      2300
   macro avg       0.89      0.89      0.89      2300
weighted avg       0.89      0.89      0.89      2300


---

## 📌 Tech Stack

* Python 3.8+
* scikit-learn (ML model)
* pandas (data handling)
* python-telegram-bot (bot framework)

---

## 🚀 Future Improvements

* Add deep learning models (LSTMs, Transformers).
* Multi-class classification (predict which type of bullying).
* Deploy bot on cloud platforms (Heroku, AWS, etc.) for 24/7 availability.

---

## 👨‍💻 Contributors
* Shilpi Kumari
* Poorva Jaiswal
* Swara Mishra
* Dashkrat Srivastava
* Prayush Patel
