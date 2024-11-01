from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from django.conf import settings
import json

# View for the homepage
def homepage(request):
    return render(request, 'HDAapp/Homepage.html')  # Serve the HTML file

# View for the intro page
def intro_page(request):
    return render(request, 'HDAapp/intro.html')

def fastbs(request):
        # Load data from the file path
    file_path = settings.EXCEL_FILE_PATH
    df = pd.read_csv(file_path)  # Modify to read_excel if needed for .xlsx files

    # Group data by age, gender, and exercise angina
    grouped_data = (
        df.groupby(['age', 'gender', 'fastingbloodsugar'])
        .size()
        .unstack(fill_value=0)  # Fill missing values with 0
        .reset_index()
    )

    # Transform the data into a JSON-compatible format for Chart.js
    chart_data = grouped_data.to_dict(orient='records')
    return render(request, 'HDAapp/fastbs.html', {'chart_data': chart_data})

def chestpain(request):
    file_path = settings.EXCEL_FILE_PATH
    df = pd.read_csv(file_path)  # Modify to read_excel if needed for .xlsx files

    # Group data by age, gender, and chest pain
    grouped_data = (
        df.groupby(['age', 'gender', 'chestpain'])
        .size()
        .unstack(fill_value=0)  # Fill missing values with 0
        .reset_index()
    )

    # Ensure we have all the chestpain columns (0, 1, 2, 3), even if they don't exist for some age/gender
    for i in range(4):
        if i not in grouped_data.columns:
            grouped_data[i] = 0

    # Transform the data into a JSON-compatible format for Chart.js
    chart_data = grouped_data.to_dict(orient='records')
    return render(request, 'HDAapp/chestpain.html', {'chart_data': chart_data})

def exang(request):
    # Load data from the file path
    file_path = settings.EXCEL_FILE_PATH
    df = pd.read_csv(file_path)  # Modify to read_excel if needed for .xlsx files

    # Group data by age, gender, and exercise angina
    grouped_data = (
        df.groupby(['age', 'gender', 'exerciseangia'])
        .size()
        .unstack(fill_value=0)  # Fill missing values with 0
        .reset_index()
    )

    # Transform the data into a JSON-compatible format for Chart.js
    chart_data = grouped_data.to_dict(orient='records')
    return render(request, 'HDAapp/exang.html', {'chart_data': chart_data})


def restingelectro(request):
    file_path = settings.EXCEL_FILE_PATH
    df = pd.read_csv(file_path)  # Modify to read_excel if needed for .xlsx files

    # Group data by age, gender, and restingrelectro
    grouped_data = (
        df.groupby(['age', 'gender', 'restingrelectro'])
        .size()
        .unstack(fill_value=0)  # Fill missing values with 0
        .reset_index()
    )

    # Ensure that all three possible restingrelectro values (0, 1, 2) exist
    for i in range(3):  # 0, 1, and 2
        if i not in grouped_data.columns:
            grouped_data[i] = 0

    # Transform the data into a JSON-compatible format for Chart.js
    chart_data = grouped_data.to_dict(orient='records')
    return render(request, 'HDAapp/restingelectro.html', {'chart_data': chart_data})

def slope(request):
    file_path = settings.EXCEL_FILE_PATH
    df = pd.read_csv(file_path)  # Modify to read_excel if needed for .xlsx files

    # Group data by age, gender, and chest pain
    grouped_data = (
        df.groupby(['age', 'gender', 'slope'])
        .size()
        .unstack(fill_value=0)  # Fill missing values with 0
        .reset_index()
    )

    # Ensure we have all the chestpain columns (0, 1, 2, 3), even if they don't exist for some age/gender
    for i in range(4):
        if i not in grouped_data.columns:
            grouped_data[i] = 0

    # Transform the data into a JSON-compatible format for Chart.js
    chart_data = grouped_data.to_dict(orient='records')
    return render(request, 'HDAapp/slope.html', {'chart_data': chart_data})

def bloodves(request):
    file_path = settings.EXCEL_FILE_PATH
    df = pd.read_csv(file_path)  # Modify to read_excel if needed for .xlsx files

    # Group data by age, gender, and chest pain
    grouped_data = (
        df.groupby(['age', 'gender', 'noofmajorvessels'])
        .size()
        .unstack(fill_value=0)  # Fill missing values with 0
        .reset_index()
    )

    # Ensure we have all the chestpain columns (0, 1, 2, 3), even if they don't exist for some age/gender
    for i in range(4):
        if i not in grouped_data.columns:
            grouped_data[i] = 0

    # Transform the data into a JSON-compatible format for Chart.js
    chart_data = grouped_data.to_dict(orient='records')
    return render(request, 'HDAapp/bloodv.html', {'chart_data': chart_data})


def restingBP(request):
    file_path = settings.EXCEL_FILE_PATH
    df = pd.read_csv(file_path)

    # Send only essential fields to the frontend
    data = df[['age', 'gender', 'restingBP']].to_dict(orient='records')
    data_json = json.dumps(data)  # Convert data to JSON
    return render(request, 'HDAapp/restingBP.html', {'data_json': data_json})

