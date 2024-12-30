<img src="assets/main.png" alt="main" style="width: 100%; height: auto;"/>
<img src="assets/main-2.png" alt="main" style="width: 100%; height: auto;"/>

# 📊 Dropbox User Sentiment Analysis Dashboard

This project demonstrates how to set up a **Dropbox User Sentiment Analysis Dashboard** using **Airbyte** for data extraction, **Motherduck (DuckDB)** for storage and querying, and **Streamlit** for visualization. 🚀

## 🌟 **Overview of the Project**

The goal is to analyze user reviews of the Dropbox app using sentiment analysis techniques. Here's the workflow breakdown:

1. **Dataset Source:** A CSV dataset of Dropbox app user reviews (from Kaggle).
2. **Preprocessing:** Data uploaded to Google Sheets for formatting.
3. **Airbyte Integration:** Google Sheets (source) connected to Motherduck (destination) via Airbyte.
4. **Destination Setup:** Motherduck stores data in DuckDB.
5. **Sentiment Analysis:** Python and Streamlit dashboard for data visualization.

🔗 **Live Demo:** [Streamlit Dashboard](https://airbyte-motherduck-hackathon-sentiment-analysis.streamlit.app)

🔗 **Blog Post:** [Detailed Guide on Sentiment Analysis](https://dev.to/abhirajadhikary06/dropbox-user-sentiment-analysis-using-airbyte-and-motherduck-1ggd)

---

## 🛠️ **Tech Stack**

- **Airbyte:** Data Integration
- **Motherduck (DuckDB):** Database Management
- **Streamlit:** Data Visualization
- **Python:** Backend and Sentiment Analysis
- **TextBlob:** Sentiment Analysis Library
- **Plotly:** Data Visualization Library

---

## 📁 **Folder Structure Overview**

```plaintext
DROPBOX-REVIEWS-ANALYSIS
├── .devcontainer
│   ├── devcontainer.json
├── .streamlit
│   ├── config.toml
├── assets
│   ├── main.png
├── dropbox-reviews-analytics
│   ├── src
│   │   ├── config
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   ├── utils
│   │   │   ├── __init__.py
│   │   │   ├── database.py
│   │   ├── app.py
├── .env
├── venv
├── .gitignore
├── LICENSE.md
├── README.md
├── requirements.txt
```

### 👉 **Key Directories Explained:**

- **.streamlit/config.toml:** UI customization for Streamlit.
- **src/config/config.py:** Handles environment variables.
- **src/utils/database.py:** Database queries with Motherduck.
- **src/app.py:** Core Streamlit app logic.
- **.env:** Stores secure environment variables.

---

## 🚀 **Setup and Installation**

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/abhirajadhikary06/Dropbox-Sentiment-Analysis.git
cd Dropbox-Sentiment-Analysis
```

### 2️⃣ **Create and Activate Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4️⃣ **Setup Environment Variables**

Create a `.env` file in the root directory and add:

```plaintext
MOTHERDUCK_TOKEN=your_motherduck_api_key
```

### 5️⃣ **Run the Streamlit App**

```bash
streamlit run src/app.py
```

The app will be available at **http://localhost:8501**.

---

## 🧠 **Core Components**

### 📊 **Sentiment Analysis Logic**

Using **TextBlob**, we calculate sentiment polarity and subjectivity.

```python
from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(str(text))
    return blob.sentiment.polarity if sentiment_type == "Polarity" else blob.sentiment.subjectivity
```

### 🦆 **Motherduck Database Integration**

```python
import duckdb
from config.config import MOTHERDUCK_TOKEN

def get_connection():
    return duckdb.connect(f"md:?token={MOTHERDUCK_TOKEN}")

def get_reviews_for_sentiment():
    conn = get_connection()
    query = """
    SELECT content, score FROM dropbox_reviews WHERE content IS NOT NULL
    """
    return conn.execute(query).fetch_df()
```

### 📈 **Visualization Example**

```python
import plotly.express as px
fig = px.histogram(reviews_df, x='sentiment', title='Sentiment Distribution')
st.plotly_chart(fig)
```

---

## ⚠️ **Deployment Notes**

- Avoid specifying exact library versions in `requirements.txt`.
- Ensure `.env` is correctly configured.
- Validate database connection tokens during runtime.

**Deployment Steps:**
1. Load `.env` variables.
2. Connect securely to Motherduck.
3. Serve the dashboard via Streamlit.

---

## 🎯 **What’s Next?**

- Improve dashboard interactivity.
- Add real-time review updates.
- Expand to analyze multiple datasets.

🔗 **Complete Project on GitHub:** [GitHub Repository](https://github.com/abhirajadhikary06/Dropbox-Sentiment-Analysis)

🔗 **Live Demo:** [Streamlit Dashboard](https://airbyte-motherduck-hackathon-sentiment-analysis.streamlit.app)

🔗 **Motherduck Instance:** 
```
-- Run this snippet to attach database
ATTACH 'md:_share/abhiraj_db/275eb3cc-2d8b-4705-a787-39c8010e8b2f';
```

---

## 📜 **License**

This project is licensed under the [Creative Commons Zero v1.0 Universal](LICENSE.md).
