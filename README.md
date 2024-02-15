# Wine_Clustering

### Description

> *This project aim to implement a clustering algorythm (’K-Means’) in order to get valuable insights, data comes from Kaggle and is related to chemical composition of wines. For more information on the clustering and what it represents, I suggest reviewing the notebook.*

### Tools

Before getting started keep in mind the tools used to develop this project were the following:

- [Python](https://www.python.org/)
- [Postgres](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjCuc_81a2EAxWASTABHR4zDVoQFnoECAcQAQ&url=https%3A%2F%2Fwww.postgresql.org%2F&usg=AOvVaw0He1mmeTUi_lhXjiRGJtzr&opi=89978449)
- [SQLAlchemy](https://www.sqlalchemy.org)
- [Flask](https://flask.palletsprojects.com)
- [Docker](https://www.docker.com)
- [Power Bi](https://powerbi.microsoft.com)

### Running the Docker Container

1. **Clone the Github repository**
2. **Open Docker Desktop**, if you don’t have it, go [here](https://www.docker.com/products/docker-desktop/) 
3. **Run the following command to build and run the Docker container**
    
    ```docker
    docker-compose up --build
    ```
    
4. **At this point the API should be running and accesible at port 5000**

### How to use the API

There are different ways to test an API, you can use tools such as [Postman](https://www.postman.com) where you testing can be done without even write a line of code, but, if you prefer to make the requests using Python, here’s some examples:

### Getting all the records properly labeled  (’/’)

> *The following code will return you a JSON with all the data, if an error occurs make sure you do not have any service running on the port 5000* 

```python
import requests

url = 'http://localhost:5000/'

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print("Error:", e)
```

### Getting the ranges of each attribute  (’/ranges’)

> *The following code will return you a dictionary with the min and max value from each attribute*

```python
import requests

url = 'http://localhost:5000/ranges'

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print("Error:", e)
```

### Getting the cluster 1  (’/cluster1’)

> *The following code will provide you with a JSON containing all the data associated with cluster 1*

```python
import requests

url = 'http://localhost:5000/cluster1'

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print("Error:", e)
```

### Getting the cluster 2  (’/cluster2’)

```python
import requests

url = 'http://localhost:5000/cluster2'

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print("Error:", e)
```

### Getting the cluster 3  (’/cluster3’)

```python
import requests

url = 'http://localhost:5000/cluster3'

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print("Error:", e)
```

### Contact

If you have any questions or suggestions, feel free to contact me at [lapiceroazul@proton.me](mailto:lapiceroazul@proton.me)