import pandas as pd
import requests
import logging
from flask import Flask
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

app= Flask(__name__)

def extract():
    """
    Download a CSV file from a given URL and save it locally.

    Returns:
        str: JSON representation of the extracted data.

    Raises:
        Exception: If there is an error downloading the CSV file.
    """
    url = "https://storage.googleapis.com/the_public_bucket/wine-clustering.csv"
    file_path = "data/raw_wine.csv"

    # Get request to download the CSV file
    logging.info("Downloading CSV file from URL: '%s'", url)
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open the local file in binary write mode
        with open(file_path, 'wb') as f:
            # Write the content data from the response into the local file
            f.write(response.content)
        logging.info("CSV file downloaded successfully. Saving it to '%s'.", file_path)
        data = pd.read_csv(file_path)
        return data.to_json(orient='records')
    else:
        error_msg = "Error downloading the CSV file. Status code: {}".format(response.status_code)
        logging.error(error_msg)
        raise Exception(error_msg)

def feature_selection(df):
    """
    Perform feature selection on the input DataFrame.

    Args:
        df: A JSON representation of the input DataFrame.

    Returns:
        A JSON representation of the dataframe with the selected features.

    """
    df = pd.read_json(df)
    X = df[['Alcohol', 'Total_Phenols', 'Flavanoids', 'Proanthocyanins', 'OD280', 'Proline']]
    logging.info("Feature selection completed.")
    return X.to_json(orient='records')

def standarize_data(X):
    """
    Standardize the input DataFrame.

    Args:
        X: A JSON representation of the input DataFrame with the features selected.

    Returns:
        A JSON representation of the standardized data.

    """
    X = pd.read_json(X)
    numeric_data = X.select_dtypes(include=['float64', 'int64']) # Standardize data
    scaled_data = StandardScaler().fit_transform(numeric_data)
    scaled_df = pd.DataFrame(scaled_data, columns=numeric_data.columns)
    # Change the df to Json
    scaled_json = scaled_df.to_json(orient='records')

    logging.info("Data has been standardized.")
    return scaled_json

def kmeans(scaled_json):
    """
    Perform K-means clustering on the scaled data and save the labeled data to a CSV file.

    Args:
        scaled_json: A JSON representation of the scaled data.

    Returns:
        A JSON representation of the labeled data.

    """
    scaled_data = pd.read_json(scaled_json)
    kmeans = KMeans(n_clusters=3, algorithm='elkan')
    kmeans.fit(scaled_data) 
    cluster_labels = kmeans.labels_

    df = pd.read_csv('data/raw_wine.csv')
    df['Cultivar'] = cluster_labels
    mapping = {0:1, 1:2, 2:3}
    df['Cultivar'] = df['Cultivar'].map(mapping)

    df.to_csv('data/data_labeled.csv', index=False)
    logging.info("K-means clustering completed. Labeled data saved to 'data_labeled.csv'.")

    return df.to_json(orient='records')

def cluster_1():
    """
    Extract data belonging to cluster 1 from the labeled data.

    Returns:
        A JSON representation of the data belonging to cluster 1.

    """
    df = pd.read_csv('data/data_labeled.csv')
    df = df[df['Cultivar'] == 1]
    logging.info("Data extraction for cluster 1 completed.")
    return df.to_json(orient='records')

def cluster_2():
    """
    Extract data belonging to cluster 1 from the labeled data.

    Returns:
        A JSON representation of the data belonging to cluster 2.

    """
    df = pd.read_csv('data/data_labeled.csv')
    df = df[df['Cultivar'] == 2]
    logging.info("Data extraction for cluster 1 completed.")
    return df.to_json(orient='records')

def cluster_3():
    """
    Extract data belonging to cluster 1 from the labeled data.

    Returns:
        A JSON representation of the data belonging to cluster 3.

    """

    df = pd.read_csv('data/data_labeled.csv')
    df = df[df['Cultivar'] == 3]
    logging.info("Data extraction for cluster 1 completed.")
    return df.to_json(orient='records')

def get_attributes_range(df):
    """
    Get the range of attributes from the input DataFrame.

    Args:
        A JSON representation of the input DataFrame.

    Returns:
        dict: A dictionary containing the range (min and max) of each attribute.

    """
    df = pd.read_json(df)
    description = df.describe()

    dict = {}
    for column in description.columns:
        min_value = description[column]['min']
        max_value = description[column]['max']
        dict[column] = {'min': min_value, 'max': max_value}
        
    logging.info("Attributes range calculated.")
    return dict

@app.route('/', methods=['GET'])
def clustered_data():
    extraction = extract()
    features = feature_selection(extraction)
    standarize = standarize_data(features)
    df = kmeans(standarize)
    return df

@app.route('/ranges', methods=['GET'])
def ranges():
    extraction = extract()
    ranges = get_attributes_range(extraction)
    return ranges

@app.route('/cluster1', methods=['GET'])
def cluster1():
    response = cluster_1()
    return response

@app.route('/cluster2', methods=['GET'])
def cluster2():
    response = cluster_2()
    return response

@app.route('/cluster3', methods=['GET'])
def cluster3():
    response = cluster_3()
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')