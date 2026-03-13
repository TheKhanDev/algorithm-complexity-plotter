import numpy as np
import matplotlib.pyplot as plt
import math

def plot_functions():
    # Define n values for plotting (smooth curve)
    n_smooth = np.linspace(1, 10, 1000)
    
    # Define the specific n values from the table
    n_table = [1, 8, 64, 512]
    
    # Define the functions
    def log_n(x):
        return np.log2(x)  # Using log base 2 as per the table
    
    def n_func(x):
        return x
    
    def n_log_n(x):
        return x * np.log2(x)
    
    def n_squared(x):
        return x**2
    
    def n_cubed(x):
        return x**3
    
    def two_pow_n(x):
        return 2**x
    
    def n_pow_n(x):
        return x**x
    
    # Additional functions (my choice)
    def sqrt_n(x):
        return np.sqrt(x)
    
    def n_log_squared(x):
        return x * (np.log2(x))**2
    
    def factorial_approx(x):
        # Using Stirling's approximation for factorial
        return np.sqrt(2 * np.pi * x) * (x / np.e)**x
    
    # Create the plot
    plt.figure(figsize=(14, 8))
    
    # Plot smooth curves
    functions = [
        (log_n, 'log n', 'blue'),
        (n_func, 'n', 'red'),
        (n_log_n, 'n log n', 'green'),
        (n_squared, 'n²', 'orange'),
        (n_cubed, 'n³', 'purple'),
        (two_pow_n, '2ⁿ', 'brown'),
        (n_pow_n, 'nⁿ', 'pink'),
        # Additional functions
        (sqrt_n, '√n', 'cyan'),
        (n_log_squared, 'n log² n', 'magenta'),
        (factorial_approx, 'n! (approx)', 'gray')
    ]
    
    for func, label, color in functions:
        try:
            y_smooth = [func(x) for x in n_smooth]
            plt.plot(n_smooth, y_smooth, label=label, color=color, alpha=0.7)
        except (OverflowError, RuntimeWarning):
            # Skip functions that cause numerical issues for large n
            continue
    
    # Add markers for table values
    for func, label, color in functions:
        try:
            y_table = [func(x) for x in n_table]
            # Handle "very large" and "extremely large" cases
            y_table_plot = []
            for val in y_table:
                if val > 1e8:
                    y_table_plot.append(1e8)  # Cap at 10^8 for plotting
                else:
                    y_table_plot.append(val)
            plt.scatter(n_table, y_table_plot, color=color, s=50, alpha=0.5)
        except (OverflowError, TypeError):
            continue
    
    plt.xlabel('n', fontsize=12)
    plt.ylabel('f(n)', fontsize=12)
    plt.title('Comparison of Function Growth Rates', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper left')
    plt.yscale('log')  # Using log scale to better show differences
    plt.xscale('log')  # Using log scale for x-axis as well
    
    # Add text annotation for table values
    table_text = "Table Values:\n"
    headers = ["n"] + [str(n) for n in n_table]
    table_text += " | ".join(headers) + "\n" + "-" * 40 + "\n"
    
    for func_name, values in [
        ("log n", [0, 3, 6, 9]),
        ("n", [1, 8, 64, 512]),
        ("n log n", [0, 24, 384, 4608]),
        ("n²", [1, 64, 4096, 262144]),
        ("n³", [1, 512, 262144, 134217728]),
        ("2ⁿ", [2, 256, "very large", "extremely large"]),
        ("nⁿ", [1, 16777216, "extremely large", "extremely large"])
    ]:
        row = [func_name] + [str(v) for v in values]
        table_text += " | ".join(row) + "\n"
    
    plt.figtext(0.15, 0.02, table_text, fontsize=8, 
                bbox=dict(facecolor='white', alpha=0.8),
                verticalalignment='bottom')
    
    plt.tight_layout()
    plt.show()
    
    # Create a second plot showing only the slower-growing functions
    plt.figure(figsize=(14, 6))
    
    slower_functions = [
        (log_n, 'log n', 'blue'),
        (sqrt_n, '√n', 'cyan'),
        (n_func, 'n', 'red'),
        (n_log_n, 'n log n', 'green'),
        (n_log_squared, 'n log² n', 'magenta')
    ]
    
    n_small = np.linspace(1, 100, 1000)
    
    for func, label, color in slower_functions:
        y_small = [func(x) for x in n_small]
        plt.plot(n_small, y_small, label=label, color=color, linewidth=2)
    
    plt.xlabel('n', fontsize=12)
    plt.ylabel('f(n)', fontsize=12)
    plt.title('Slower-Growing Functions (n ≤ 100)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_functions()