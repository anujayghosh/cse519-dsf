# NYC Business Cultural Significance Scorer - Data Science Project

## Overview
This project develops a scientific methodology to quantify the cultural significance of businesses in New York City. The system assigns significance scores to businesses by considering multiple factors including cultural relevance, historical importance, and community engagement. The project aims to help identify and preserve culturally significant independent businesses that may be at risk of being replaced by chain establishments.

## Key Features
- **Comprehensive Scoring System** that evaluates businesses based on:
  - Rating scores from customer reviews
  - Business distinctiveness ("chainness" score)
  - Neighborhood walkability
  - Cultural sentiment from reviews
  - Economic factors
  - Historical presence

- **Data Sources**
  - Yelp Fusion API
  - County Business Patterns dataset
  - Walkability scores
  - Cultural sentiment analysis
  - Employment and economic data

## Methodology

### 1. Rating Score
Combines both average ratings and number of reviews to create a balanced metric of business performance and popularity.

### 2. Chainness Score
Evaluates business distinctiveness by analyzing:
- Chain count (number of outlets)
- Chain type (Independent/Local/National)
- Geographic distribution of chain locations

### 3. Cultural Sentiment Score
Analyzes review text content using:
- Sentiment analysis
- Cultural keyword detection
- Community impact metrics

### 4. Economic Factor Score
Incorporates:
- Employee counts per establishment
- Average employee pay
- Revenue per establishment

### 5. Walkability Score
Measures pedestrian friendliness using:
- Block length
- Intersection density
- Population density

## Key Findings

- Independent businesses consistently achieve higher significance scores compared to chain establishments
- Lower Manhattan shows clusters of highly significant places
- Geographic patterns show independent businesses tend to locate along shorelines while chains prefer inland locations
- Walkability scores correlate positively with economic indicators

## Validation
The scoring system has been validated against:
- Secret NYC's top libraries list
- Timeout's list of culturally significant restaurants
- Known national chain establishments

## Technologies Used
- Python for data analysis
- TextBlob for sentiment analysis
- Principal Component Analysis (PCA) for dimensionality reduction
- Gaussian Mixture Model (GMM) for clustering
- Various similarity matching algorithms (Cosine, Jaccard, Levenshtein, Fuzzy)

## Future Work
- Implement crowdsourcing for community-driven scoring
- Develop methods to identify culturally significant chain locations
- Refine metrics for distinguishing between branches of the same chain
- Expand analysis to other boroughs beyond Manhattan
