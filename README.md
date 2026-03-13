# Function Growth Rate Visualizer

A Python visualization tool that plots and compares the growth rates of mathematical functions commonly used in algorithm analysis.

## 📊 Functions Included

### From the original table:
- log n
- n
- n log n
- n²
- n³
- 2ⁿ
- nⁿ

### Additional functions:
- √n (square root)
- n log² n
- n! (factorial approximation using Stirling's formula)

## 🎯 Features

- Dual plots: Full view (log-log scale) and zoomed view (n ≤ 100)
- Markers at specific n values (1, 8, 64, 512) from the original table
- Handles overflow for extremely large values
- Table data displayed as text annotation
- Clear color-coded legends

## 📷 Preview

![Function Growth Plot](<img width="824" height="388" alt="function" src="https://github.com/user-attachments/assets/64fb53b9-440e-466d-9eec-392a47076e05" />)

## 🚀 Usage

1. Clone the repository
2. Install requirements:
   ```bash
   pip install numpy matplotlib
