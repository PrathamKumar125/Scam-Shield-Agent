# Scam Shield Agent

ScamShield is a tool designed to help users identify potential online scams and phishing attempts. It leverages AI agents and multiple API integrations to perform comprehensive analysis of suspicious URLs and provide detailed risk assessments.

## Features

- URL analysis with detailed breakdown of characteristics
- Web content evaluation using FireCrawl API
- Risk level assessment (Low/Medium/High)
- Specific red flag identification
- Recommended user protection actions
- Gradio-based user interface

## Setup

### Prerequisites

- Python 3.8+
- Hugging Face API key
- FireCrawl API key

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd multi-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure API keys:
   Create a `.env` file in the root directory with:
   ```
   HF_API_KEY=your_huggingface_api_key
   FIRECRAWL_API_KEY=your_firecrawl_api_key
   ```

## Usage

Run the application:
```bash
python app.py
```

This will start the Gradio interface where you can:
1. Enter a description of your concerns
2. Input a suspicious URL
3. Click "Process submission" to receive a detailed analysis

## Project Structure

- `app.py`: Main application with Gradio UI and agent setup
- `firecrawler.py`: Tool for website scraping using FireCrawl API
- `rag.py`: Retrieval Augmented Generation system for knowledge base queries
- `requirements.txt`: Project dependencies

## Components

### CodeAgent

The core of ScamShield is built on `smolagents`' CodeAgent, which orchestrates:
- URL content retrieval
- Pattern matching against known scam indicators
- Generation of comprehensive analysis reports

### Tools

- **FireCrawlTool**: Scrapes website content for analysis
- **RetrieverTool**: Uses semantic search to retrieve relevant information from a knowledge base

## Dependencies

Main libraries:
- smolagents
- firecrawl-py
- langchain
- gradio
- huggingface_hub
- datasets

