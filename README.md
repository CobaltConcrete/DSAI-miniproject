# SC1015 Mini Project: Customer Churn Analysis

## Group Members
- Gan Qing Rong (U2321908E)
- Gracelynn Qwek Kai Xin (U2320019G)
- Denzel Tan Yong Liang (U2321195E)

---

## Project Overview

In this project, we analyse the **BankChurners** dataset to uncover behavioural patterns that lead to customer churn and develop machine learning models that accurately predict at-risk individuals. The dataset comprises 10,000+ records with a rich blend of 15 numerical and 8 categorical features.

Our pipeline includes:
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Feature selection using correlation, F-score, and mutual information
- Model development and evaluation
- Strategic recommendations based on data-driven insights

---

## Marking Criteria Breakdown

### 10% Problem Definition

Churn in banking is costly — it leads to:
- Loss of recurring revenue
- Weakened brand loyalty
- Increased marketing costs for replacements

Understanding **why** customers churn enables banks to proactively retain them.

---

### 10% Data Preparation & Cleaning

Steps taken:
- Dropped columns like `CLIENTNUM` that do not aid modelling
- Verified absence of nulls for data reliability
- Converted `Attrition_Flag` → binary `Churn` column
- Removed outliers using the Interquartile Range (IQR) method

---

### 20% Exploratory Data Analysis

EDA techniques used:
- Categorical analysis (e.g. churn by gender, education)
- Histograms of key numerical variables (Age, Credit Limit)
- `jointplot` to show churners clustered around lower spend ranges and higher utilisation
- Feature importance scoring using:
  - Pearson Correlation
  - ANOVA F-score
  - Mutual Information

Top features:
- `Total_Trans_Ct`
- `Total_Trans_Amt`
- `Avg_Utilization_Ratio`
- `Total_Revolving_Bal`
- `Contacts_Count_12_mon`

---

### 20% Machine Learning Techniques

We trained and compared multiple models:
| Model               | Accuracy | F1 Score | Precision | Recall |
|--------------------|----------|----------|-----------|--------|
| Logistic Regression| 0.7272   | 0.7787   | 0.6551    | 0.9598 |
| Decision Tree       | 0.9275   | 0.7725   | 0.7789    | 0.7662 |
| Random Forest       | 0.9369   | 0.7867   | 0.8632    | 0.7231 |
| AdaBoost            | 0.9383   | 0.8134   | 0.8460    | 0.7833 |
| XGBoost             | 0.9490   | 0.8323   | 0.8804    | 0.7893 |
| SVM (with PCA)      | 0.9272   | 0.8228   | 0.7002    | 0.7561 |
| MLP Neural Network  | 0.9448   | 0.8288   | 0.8261    | 0.8316 |

---

### 20% Insights and Recommendations

Key insights:
- Churners typically transact less (1,000–3,000 range)
- Higher utilisation and shorter tenure correlates with churn

Proposed actions:
1. Financial Education – workshops and credit-rebuilding tools
2. Targeted Retention – cashback/personalised discounts
3. Behaviour Monitoring – early alerts for declining activity
4. Gamified Youth Accounts – increase engagement through family-linked features

---

### 10% Team Presentation
- Embedded HTML-based 3D clustering and SVM visualisations
- Clear articulation of problem, process, and solution

---

### 10% Going Beyond the Course
- Custom 3D KMeans and SVM boundary plots rendered in standalone HTML
- Used mutual information for deeper feature selection
- Applied MLP Neural Network to explore non-linear relationships
