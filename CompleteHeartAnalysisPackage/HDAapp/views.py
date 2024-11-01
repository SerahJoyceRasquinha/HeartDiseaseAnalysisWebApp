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
    import numpy as np
    file_path = settings.EXCEL_FILE_PATH
    df = pd.read_csv(file_path)

    # Define resting BP ranges for normal individuals based on age and gender
    normal_bp_ranges = {
        (20, 29): {'M': (70, 112), 'F': (68, 108)},
        (30, 39): {'M': (70, 118), 'F': (68, 112)},
        (40, 49): {'M': (77, 122), 'F': (77, 118)},
        (50, 59): {'M': (77, 128), 'F': (77, 122)},
        (60, 69): {'M': (69, 132), 'F': (68, 128)},
        (70, 80): {'M': (69, 138), 'F': (68, 132)}
    }
    
    abnormal_bp_thresholds = {
        (20, 29): {'M': 130, 'F': 120},
        (30, 39): {'M': 135, 'F': 125},
        (40, 49): {'M': 145, 'F': 135},
        (50, 59): {'M': 155, 'F': 145},
        (60, 69): {'M': 165, 'F': 155},
        (70, 80): {'M': 175, 'F': 165}
    }

    def categorize_bp(row):
        age, gender, bp = row['age'], row['gender'], row['restingBP']
        for age_range, ranges in normal_bp_ranges.items():
            if age_range[0] <= age <= age_range[1]:
                if gender in ranges:  # Ensure gender exists in the range
                    if bp <= ranges[gender][1]:  # Use upper bound for normal range
                        return 'normal'
                    elif bp >= abnormal_bp_thresholds[age_range].get(gender, float('inf')):  # Check abnormal threshold
                        return 'abnormal'
        return 'normal'

    df['bp_category'] = df.apply(categorize_bp, axis=1)

    # Group data by age ranges and gender, counting normal/abnormal values
    df['age_group'] = pd.cut(df['age'], bins=[20, 30, 40, 50, 60, 70, 80], right=False, labels=['20-30', '30-40', '40-50', '50-60', '60-70', '70-80'])
    grouped_data = df.groupby(['age_group', 'gender', 'bp_category']).size().unstack(fill_value=0).reset_index()

    # Transform data into a JSON format compatible with Chart.js
    chart_data = grouped_data.to_dict(orient='records')
    return render(request, 'HDAapp/restingBP.html', {'chart_data': chart_data})

