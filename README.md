Brand Sentiment Intelligence System (Tesla) 

A full-stack project that collects and analyzes public sentiment about a brand (in my case I've chosen Tesla because of recent commotion) across **YouTube**, **Reddit**, and **News** sources. Built with **Python**, **PostgreSQL**, **VADER**, and visualized in **Power BI**.

Features
- YouTube Data Collection via API
- Reddit Comments & Post Mining
- News Article Aggregation via NewsAPI
- Sentiment Analysis using NLTK VADER
- PostgreSQL database storage
- Professional Power BI Dashboard

Dashboard Overview
- [Sentiment Overview Dashboard] (visualizations/Screenshot (836).png)

Project Overview & Key Findings (Tesla Case Study)
This project explores public sentiment around Tesla by collecting and analyzing real-world data from YouTube, Reddit, and News sources. Using APIs, the system pulls relevant content such as video comments and descriptions, social discussions, and news headlines, and applies VADER sentiment analysis to assess the tone of public opinion. The processed data is stored in a PostgreSQL database and visualized through interactive dashboards in Power BI.

Key Findings:
YouTube: Sentiment was generally positive, especially around Tesla product launches, EV innovations, and Elon Musk's public appearances. Videos with strong engagement (likes/views) typically had high sentiment scores.

Reddit: Sentiment was more mixed and leaned more towards a neutral sentiment, reflecting deep community discussions. Subreddits like r/technology and r/WallStreetBets had polarized views—positive around tech advancements but critical of Tesla stock volatility and Musk’s tweets.

News: Articles showed a neutral-to-slightly-negative sentiment overall. While coverage praised Tesla’s market leadership, it also highlighted controversies like recalls, safety investigations, and leadership behavior.

Patterns Observed:
Reddit comments had higher emotional variance than news or YouTube.

News sentiment was most stable, while Reddit fluctuated most in tone.

Overall sentiment across all platforms leaned positive with spikes of negativity linked to specific events (e.g., recall announcements or Twitter controversies).



