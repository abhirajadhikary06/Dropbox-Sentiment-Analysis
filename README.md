# Dropbox Reviews Sentiment Analysis

This project provides a comprehensive dashboard for analyzing the sentiment of Dropbox app reviews. It leverages **Streamlit** for the web interface, **Plotly** for interactive visualizations, and **TextBlob** for sentiment analysis.It is a part of Airbyte + Motherduck Hackthon so it leverages **Airbyte** for data connection between Google Sheet and **Motherduck** and Motherduck for database.

## Features

- **Sentiment Analysis**: Analyze the polarity and subjectivity of Dropbox app reviews.
- **Interactive Visualizations**: View sentiment distribution and sentiment by review score.
- **Sample Reviews**: Explore sample reviews categorized by sentiment.
- **Customizable Filters**: Filter reviews based on sentiment type.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/abhirajadhikary06/Dropbox-Sentiment-Analysis.git
    cd dropbox-reviews-analytics
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run src/app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to view the dashboard.

## Deployment

To deploy this app on Streamlit Cloud:

1. Push your code to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io) and sign in with your GitHub account.
3. Click "New app" and select your repository.
4. Set the main file path to [app.py](http://_vscodecontentref_/0).
5. Add any necessary environment variables (e.g., `MOTHERDUCK_TOKEN`).
6. Click "Deploy".

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. See the LICENSE file for details.

You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.
