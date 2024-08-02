# Trademark Infringement Detection AI

This project leverages AI to detect potential trademark infringement by comparing company names with existing trademarks registered in India. The system uses LangChain, FAISS, Google Generative AI, and Streamlit to analyze and identify similarities in names, spelling, and pronunciation.

## Trademark Journal Website
- by Government of India (GOI)
https://search.ipindia.gov.in/IPOJournal/Journal/Trademark

## Overview
![WhatsApp Image 2024-08-02 at 23 10 46_f348ab02](https://github.com/user-attachments/assets/7a22eaa6-241f-4404-9143-0a00afdd3174)

The application consists of two main components:

1. **Embedding Creation and Storage**:
   - Processes a collection of 8 PDF files containing registered trademark details and extracts vector embeddings.
   - Stores the embeddings in a pickle file for efficient retrieval.

2. **Streamlit Application**:
   - A user-friendly interface for performing similarity searches on the stored embeddings.
   - Identifies company names similar to the queried name and further analyzes these results using a language model (LLM).

## Features

- **Google Generative AI**: Converts the company names to vector embeddings.
- **Similarity Search**: Uses FAISS to perform fast similarity searches on the stored vector embeddings.
- **LLM Analysis**: Analyzes the most similar results using a language model to provide deeper insights into potential infringement issues.
- **Interactive Interface**: A Streamlit-based application allows users to easily input queries and view results.
- **RAG and Chaining**: The LLM uses Retrieval-Augmented Generation (RAG) and chaining techniques to generate the most accurate and relevant results.

## How It Works

1. **Data Preparation**: 
   - PDFs containing trademark details are processed to extract text and create embeddings.
   - The embeddings are saved in a pickle file for future use.

2. **Similarity Search**:
   - The Streamlit app allows users to enter a company name.
   - The system searches for similar names based on embeddings and returns the closest matches.

3. **Analysis**:
   - The most similar company names are analyzed using Google Generative AI. The LLM utilizes RAG and chaining methods to detect potential legal issues, considering spelling and pronunciation similarities.

## Setup

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [LangChain](https://langchain.readthedocs.io/)
- [FAISS](https://python.langchain.com/v0.2/docs/integrations/vectorstores/faiss/)
- [Google Generative AI](https://ai.google/)

### Installation

1. Clone the repository:

       git clone https://github.com/deepmbhatt/Trademark-Infringement-Detection-AI.git

2. Install dependencies:

        pip install -r requirements.txt

3. Start the Streamlit application:

        streamlit run legal_app.py

   
## Usage
- **Embedding Creation**: Run create_embeddings.ipynb to process the PDF files and generate the pickle file with vector embeddings.
- **Streamlit App**: Use legal_app.py to launch the web interface for searching and analyzing potential trademark infringements.

## Project Structure 
├── create_embeddings.ipynb   # Script to create and store vector embeddings

├── company_data.pickle       # Pickle file for company data and details

├── legal_app.py              # Streamlit application for similarity search and analysis

├── data/                     # Directory containing the PDF files

├── faiss_index/              # Directory to store the vector embeddings using FAISS (Embeddings of just the name of companies)

├── requirements.txt          # Python dependencies

└── README.md                 # Project documentation

## Future Work
- Integrate additional AI models for more accurate pronunciation similarity detection.
- Enhance the user interface for better user experience.
- Expand the database to include international trademarks.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Working:

- Search results for the company name: Koler
![image](https://github.com/user-attachments/assets/ca928f9c-d1f2-4146-8672-e4f4dbfe34f3)
![image](https://github.com/user-attachments/assets/a8123511-59eb-4261-8b4c-3aefeb2ee01a)

- Search results for company name: Laxmi
![image](https://github.com/user-attachments/assets/c5dbb8a6-8ffc-4c8f-9dbf-07da01fa2cca)
![image](https://github.com/user-attachments/assets/56095b40-998c-406c-b6fb-c6f80dba1689)
![image](https://github.com/user-attachments/assets/322bbee8-dcfa-4bcb-bc39-9b5037d87cfc)




