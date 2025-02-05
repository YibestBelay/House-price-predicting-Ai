import pandas as pd

def load_data(file_path: str):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: The loaded dataset.
    """
    try:
        # Load the dataset into a pandas DataFrame
        data = pd.read_csv(file_path)

        # Display the first few rows of the dataset
        print("Dataset Preview:")
        print(data.head())

        # Check for missing values
        print("\nMissing Values:")
        print(data.isnull().sum())

        # Return the dataset
        return data

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace this path with the actual path to your dataset
    file_path = "data/HousingData.csv"
    dataset = load_data(file_path)
