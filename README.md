# Medical Data Visualizer

This project visualizes and analyzes medical examination data using Python libraries matplotlib, seaborn, and pandas. The dataset contains patient information such as body measurements, blood test results, and lifestyle choices. The goal is to explore the relationship between cardiac disease and various health indicators.

## Dataset Description

This dataset, stored in `medical_examination.csv`, contains medical examination information for patients. Each row represents a patient, and the columns represent various characteristics and examination results. The main objective of the dataset is to evaluate the presence or absence of cardiovascular disease (`cardio`) in relation to different health factors.

**Considerations:**

*   The `cholesterol` and `gluc` variables are categorized into three levels (1, 2, and 3).
*   The `smoke`, `alco`, `active`, and `cardio` variables are binary, representing "no" with 0 and "yes" with 1.
*   Age is expressed in days.
*   `sex` is 1 for female and 2 for male.
*   `ap_hi` and `ap_lo` represent systolic and diastolic pressures, respectively.

**Possible Analyses:**

This dataset allows for various analyses, such as:

*   Analysis of the correlation between different health factors.
*   Examining the relationship between smoking, alcohol consumption, active or inactive lifestyle, and cardiovascular disease.
*   Relationship between cholesterol and glucose levels with cardiovascular disease.
*   Age and cardiovascular diseases.
*   Weight and height as risk factors.
*   Systolic and diastolic pressure in relation to cardiovascular disease.

This dataset can be used to build predictive models to identify patients at high risk of developing cardiovascular disease.

## Installation

Follow these steps to set up the project:

1.  **Clone the repository:**

    ```bash
    git clone <MY_REPOSITORY_URL>
    cd medical-data-visualizer
    ```

2.  **Install dependencies:**

    Ensure you have Python 3 installed. Then, install the required libraries:

    ```bash
    pip install pandas seaborn matplotlib numpy
    ```

## Usage

1.  **Run the main script:**

    Execute the following command to generate and display the visualizations:

    ```bash
    python src/main.py
    ```

    This will:

    *   Generate a categorical plot saved as `catplot.png`.
    *   Generate a heat map saved as `heatmap.png`.
    *   Display both plots on your screen.

## Output

*   **Categorical Plot (`catplot.png`):** Displays counts of cholesterol, gluc, smoke, alco, active, and overweight outcomes (0 or 1), split by cardio (0 for no disease, 1 for disease).
*   **Heat Map (`heatmap.png`):** Shows the correlation matrix of the cleaned dataset, highlighting relationships between variables.

## Functionality

### `draw_cat_plot()`

*   **Purpose:** Creates a categorical plot to compare feature outcomes between patients with and without cardiovascular disease.
*   **Process:**
    1.  Transforms the DataFrame into a long format for categorical variables using `pd.melt`.
    2.  Uses `seaborn.catplot` to generate a count plot, split by cardio.
*   **Output:** A figure object with the categorical plot.

### `draw_heat_map()`

*   **Purpose:** Generates a heat map of the correlation matrix after data cleaning.
*   **Process:**
    1.  Filters out invalid data (e.g., diastolic pressure > systolic pressure, extreme height/weight values).
    2.  Calculates the correlation matrix.
    3.  Uses `seaborn.heatmap` to visualize correlations.
*   **Output:** A figure object with the heat map.

## Code Structure

*   `medical_data_visualizer.py`: Contains the core logic, including data processing and visualization functions.
*   `main.py`: A script to run and display the visualizations generated by `medical_data_visualizer.py`.
*   `medical_examination.csv`: The dataset file.

## Testing

To test the project:

1.  Ensure `medical_examination.csv` is in the project's root directory.
2.  Run the main script:

    ```bash
    python src/main.py
    ```

3.  Verify the generated `catplot.png` and `heatmap.png` files for accuracy.
4. Optionally, modify `main.py` to add custom tests or additional visualizations.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.