# Indian Startups Funding Dashboard

Welcome to the Startup Funding Dashboard project! This project is designed to provide comprehensive insights into the funding landscape of Indian startups from January 2015 to January 2020. Leveraging powerful data analysis and visualization tools, this dashboard offers detailed views from both company and investor perspectives, as well as general trends and patterns in the startup ecosystem.

## Overview

The Startup Funding Dashboard is built using the following technologies:
- **Numpy**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Streamlit**

The app is divided into three main sections, each offering a unique perspective on the startup funding data:

1. **General Analysis**
2. **Startup POV **
3. **Investor POV **

## Features

### 1. General Analysis
This section provides a high-level overview of the startup funding trends, including:
- **MoM Chart**: Monthly total and count of funding events.
- **Summary Cards**: Total, maximum, and average funding amounts for funded startups.
- **Sector Analysis**: Pie chart showing top sectors by funding count and sum.
- **Type of Funding**: Distribution of different types of funding.
- **City-wise Funding**: Analysis of funding distribution across different cities.
- **Top Startups**: Year-wise and overall top startups based on funding.
- **Top Investors**: List of top investors based on their funding activities.
- **Funding Heatmap**: Heatmap showcasing funding activities over time.

### 2. Startup POV
This section offers detailed insights from the perspective of startups, including:
- **Company Details**: Information about the company, including name, founders, industry, sub-industry, and location.
- **Funding Rounds**: Detailed information about funding rounds, including stage, investors, and date.
- **Similar Companies**: Identification of companies similar to the selected startup.

### 3. Investor POV
This section provides detailed insights from the perspective of investors, including:
- **Investor Details**: Information about the investor, including name, recent investments, and biggest investments.
- **Investment Patterns**: Analysis of the sectors, stages, and cities where the investor generally invests, displayed as pie charts.
- **YoY Investment Graph**: Year-over-year investment trends for the investor.
- **Similar Investors**: Identification of investors similar to the selected investor.

## Getting Started

To run the dashboard locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/dilkushsingh/Indian-Startups-Funding-Dashboard.git
    cd Indian-Startups-Funding-Dashboard
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Launch the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. Open your browser and navigate to `http://localhost:8501` to view the dashboard.

## Data Source

The dataset used in this project contains information on Indian startup funding from January 2015 to January 2020. The data includes details such as company names, founders, industries, sub-industries, locations, funding rounds, investors, and funding amounts.

## Contributing

Contributions to this project are welcome! If you have any ideas, suggestions, or improvements, please feel free to submit a pull request or open an issue on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Explore the funding landscape of Indian startups with the Startup Funding Dashboard and gain valuable insights to make informed decisions. Happy analyzing!
