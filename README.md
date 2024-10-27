# Sentiment Analysis on Patient Feedback Using Python and Power BI
## Overview

This project provides insights into patient satisfaction by analyzing and visualizing sentiment in healthcare feedback. A custom Python script classifies feedback as positive, negative, or neutral without using external libraries. The results are then visualized in Power BI, enabling healthcare providers to track sentiment trends, common themes, and department-wise satisfaction metrics.

## Tech Stack

  Programming Language: Python
  Data Visualization: Power BI
  Data Storage: CSV/Excel
  Development Environment: Power BI Desktop, Python IDE 

  ## link for dataset:
    https://data.cms.gov/provider-data/dataset/dgck-syfz


## steps for using Power BI

1. Open Power BI Desktop

  Start Power BI Desktop on your computer.

2. Import the CSV File

    Go to Home > Get Data > Text/CSV.
    Navigate to your file location: /home/vidi/leetcode/project/sentiment_analysis/patient_feedback_sentiment.csv.
    Select the file and click Open.
    Power BI will show a preview of the data. Click Load to import the data into Power BI.

3. Verify Data Structure

    Once loaded, go to the Data view in Power BI to confirm that all columns are imported correctly, particularly HCAHPS Answer Description, Sentiment Score, and Sentiment Label.

4. Create Visualizations

  Now that the data is in Power BI, you can create different visualizations to analyze the sentiment distribution and patterns in patient feedback.
  A. Sentiment Distribution (Pie Chart or Bar Chart)

  Go to Visualizations and select Pie Chart or Bar Chart.
    Drag Sentiment Label to the Legend field.
    Drag Sentiment Label again to Values (Power BI will automatically count each occurrence).
    This chart will show the proportion of Positive, Negative, and Neutral feedback.

  B. Feedback Length vs. Sentiment Score (Scatter Plot)

  To see if feedback length affects sentiment, calculate the number of words in each feedback entry:
        In Power BI, go to Modeling > New Column.
        Enter a formula like:

  DAX

     WordCount = LEN(TRIM([HCAHPS Answer Description])) - LEN(SUBSTITUTE(TRIM([HCAHPS Answer Description]), " ", "")) + 1

  Now, go to Visualizations and select Scatter Chart.
    Drag WordCount to X-axis and Sentiment Score to Y-axis.
    This chart shows if longer feedback is associated with more positive or negative sentiment scores.

  C. Sentiment Over Time (Line Chart)

   If your dataset has a date column, use it to track sentiment over time.
    Select Line Chart from Visualizations.
    Drag the Date column to the Axis.
    Drag Sentiment Label to Legend.
    Drag Sentiment Label again (Count) or Sentiment Score (Average) to Values.
    This will show sentiment trends over time (for example, monthly changes in feedback sentiment).

  D. Common Themes (Word Cloud)

  Download the Word Cloud custom visual from AppSource:
        In the Visualizations pane, click the three dots (…) > Get more visuals > search for "Word Cloud" and import it.
    Drag HCAHPS Answer Description to Category.
    This will generate a word cloud, showing the most frequently mentioned terms in feedback.

5. Add Interactive Filters

    Use Slicers to add interactivity to your dashboard:
        Sentiment Label Slicer: Add a slicer for Sentiment Label so you can filter by Positive, Negative, or Neutral feedback.
        Date Slicer: If there’s a date column, add a slicer to filter feedback by specific dates or date ranges.

6. Customize and Format Visuals

    Use the Format pane to adjust the appearance of visuals, add data labels, tooltips, and set colors for readability.
    Customize titles and add descriptions to each chart to make the dashboard informative.

7. Save and Publish

    Save your Power BI report.
    If you want to share the report, you can Publish to Power BI Service to manage permissions and share with others.

Example Dashboard Insights

Your Power BI report will enable a variety of insights, including:

  Overall Sentiment Distribution (e.g., percentages of Positive, Negative, and Neutral feedback)
    Sentiment Trends Over Time
    Common Themes in Feedback (through Word Cloud)
    Feedback Length vs. Sentiment Analysis (scatter plot for additional insights)

These steps provide a comprehensive view of patient feedback and sentiment, useful for data-driven improvements in healthcare experiences.


