
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd

# =========================
# Load dataset and model results
# =========================

try:
    combined_df = pd.read_csv('cleaned_air_quality_data.csv')
except:
    combined_df = None

try:
    model_results = pd.read_csv('model_results.csv')
except:
    model_results = None

# =========================
# GUI Window
# =========================

root = tk.Tk()
root.title('Beijing Air Quality Analysis System')
root.geometry('1200x800')

# =========================
# Notebook Tabs
# =========================

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# =========================
# Dataset Section
# =========================

frame_dataset = ttk.Frame(notebook)
notebook.add(frame_dataset, text='Dataset Section')

label_dataset = tk.Label(
    frame_dataset,
    text='Dataset Preview',
    font=('Arial', 16, 'bold')
)
label_dataset.pack(pady=10)

text_dataset = tk.Text(frame_dataset, height=30, width=140)
text_dataset.pack(padx=10, pady=10)

if combined_df is not None:
    text_dataset.insert(tk.END, combined_df.head(20).to_string())
else:
    text_dataset.insert(tk.END, 'cleaned_air_quality_data.csv not found')

# =========================
# Visualization Section
# =========================

frame_visual = ttk.Frame(notebook)
notebook.add(frame_visual, text='Visualization Section')

visual_title = tk.Label(
    frame_visual,
    text='Air Quality Visualizations',
    font=('Arial', 16, 'bold')
)
visual_title.pack(pady=10)

visualizations = {
    'Average PM2.5 Concentration by Station': 'average_PM2_5_concentration_station.png',
    'Yearly Average PM2.5 Trend': 'yearly_pm25_trend.png',
    'Monthly Average PM2.5 Trend': 'monthly_pm25_trend.png',
    'Seasonal Average PM2.5 Comparison': 'seasonal_average_pm2_5_comaprison.png',
    'Relationship Between PM2.5 and Temperature': 'pm25_temperature_relationship.png',
    'NO2 vs O3': 'no2_o3_comaprison.png',
    'Correlation Heatmap': 'correaltion_heatmap.png',
    'Hourly Average PM2.5 Trend': 'pm2_5_hourly_average.png',
    'Hourly PM2.5 Trends by Area and Day Type': 'pm2_5_hourly_trend_area_day.png',
    'Seasonal Hourly PM2.5 Trends': 'season.png',
    'Machine Learning Model Comparison': 'model_comparison.png'
}

selected_graph = tk.StringVar()
selected_graph.set(list(visualizations.keys())[0])

dropdown = ttk.Combobox(
    frame_visual,
    textvariable=selected_graph,
    values=list(visualizations.keys()),
    state='readonly',
    width=50
)

dropdown.pack(pady=10)

image_label = tk.Label(frame_visual)
image_label.pack(pady=20)

image_refs = []

def show_graph(event=None):

    graph_name = selected_graph.get()
    image_path = visualizations[graph_name]

    try:
        img = Image.open(image_path)
        img = img.resize((900, 500))

        photo = ImageTk.PhotoImage(img)

        image_refs.clear()
        image_refs.append(photo)

        image_label.config(image=photo)

    except:
        image_label.config(
            text=f'Image not found: {image_path}',
            image=''
        )

show_graph()

dropdown.bind('<<ComboboxSelected>>', show_graph)

# =========================
# Model Outputs Section
# =========================

frame_model = ttk.Frame(notebook)
notebook.add(frame_model, text='Model Outputs Section')

model_title = tk.Label(
    frame_model,
    text='Machine Learning Model Results',
    font=('Arial', 16, 'bold')
)
model_title.pack(pady=10)

model_text = tk.Text(frame_model, height=30, width=120)
model_text.pack(padx=10, pady=10)

if model_results is not None:
    model_text.insert(tk.END, model_results.to_string(index=False))
else:
    model_text.insert(tk.END, 'model_results.csv not found')

# =========================
# Run Application
# =========================

root.mainloop()
