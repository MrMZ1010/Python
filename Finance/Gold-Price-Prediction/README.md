# Gold Price Prediction

This project aims to predict gold prices using historical data and a linear regression model.

## Table of Contents

- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [Feature Engineering](#feature-engineering)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Results](#results)
- [Usage](#usage)

## Introduction

In this project, we predict gold prices using historical data fetched from Yahoo Finance. The prediction is made using a linear regression model.

## Data Collection

We use the Yahoo Finance API to collect historical gold prices for the past four years.

## Feature Engineering

For simplicity, the model uses the previous day's closing price as the feature to predict the next day's closing price.

## Model Training and Evaluation

The data is split into training and testing sets, and a linear regression model is trained and evaluated. Key metrics include Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R^2 Score.

## Results

The results of the model are visualized using a scatter plot of the actual vs. predicted prices.
![Result](result.png)

