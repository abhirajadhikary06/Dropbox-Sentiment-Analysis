This repository contains a README file sample for Daytona Samples and the MIT License.

It can be used as a template to create sample repositories that can be added into [Daytona](https://github.com/daytonaio/daytona).

Once you finish your sample and it gets merged, you can open a PR in the Daytona repo and submit the sample into the [index file](https://github.com/daytonaio/daytona/blob/main/hack/samples/index.json).

# Python

## Spotify User Review Sentiment Analysis
This project performs sentiment analysis on Spotify user reviews. It utilizes natural language processing techniques to classify reviews as positive, negative, or neutral and provides an interactive visualization interface.

---

## 🚀 Getting Started  

### Open Using Daytona  

1. **Install Daytona**: Follow the [Daytona installation guide](https://www.daytona.io/docs/installation/installation/).  
2. **Create the Workspace**:  
   ```bash  
   daytona create <SAMPLE_REPO_URL>  
   ```  
3. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  
4. **Start the Application**:  
   ```bash  
   streamlit run src/app.py  
   ```  

---

## ✨ Features  

- 🧠 Sentiment analysis of Spotify reviews using natural language processing.  
- 📊 Interactive and user-friendly visualization dashboard powered by Streamlit.  
- 🛠️ Standardized development environment using Daytona.  
- 🔄 Comprehensive data pipeline for preprocessing, analysis, and visualization.  
- 📈 Extracts insights into user feedback trends from Spotify reviews.  
- 🦆 Efficient query handling and data storage powered by DuckDB through MotherDuck integration for seamless performance.