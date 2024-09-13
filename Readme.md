### Public Interface

Here's a description of the public interface for the `Tenant` class:

### Tenant Class

The `Tenant` class provides an interface for interacting with the Sophos API.\
It manages authentication, handles HTTP requests, and includes methods for various HTTP operations.

#### Initialization
##### Without Context Manager

```python
import TenantAPI

client_id = "client_id"
client_secret = "client_secret"

# Initialize Tenant
tenant = TenantAPI.Tenant(client_id, client_secret)

try:
    # Actions Here
    response = tenant.get("/some/endpoint")
finally:
    # Ensure session is closed
    tenant.close()
```
##### With Context Manager

```python
import TenantAPI

client_id = "client_id"
client_secret = "client_secret"

with TenantAPI.Tenant(client_id, client_secret) as tenant:
    # Actions Here
    response = tenant.get("/some/endpoint")
```
### Response

In the `Tenant` class, the methods (`get`, `post`, `patch`, `delete`, `put`) return a dictionary with the following structure:

Here's a concise explanation for the output format:

#### Successful Response

```json
{
    "status": "success",
    "message": "Request successful",
    "data": { ... }  // JSON data from the response
}
```

**Explanation:**
- **`status`**: Indicates that the request was successful.
- **`message`**: A brief description confirming the request was successful.
- **`data`**: Contains the actual response data in JSON format, providing the information requested.

#### Error Response

```json
{
    "status": "error",
    "message": "Request failed",
    "data": "Error details"  // e.g., exception message or a custom error message
}
```

**Explanation:**
- **`status`**: Indicates that the request failed.
- **`message`**: A brief description of the failure.
- **`data`**: Provides details about the error, such as an exception message or a custom error description.

**Usage Context:**
- **Successful Response**: Used when the API request completes successfully and returns the expected data.
- **Error Response**: Used when the API request fails due to issues such as network problems, invalid requests, or server errors.


#### Response Checking

```python
# Example of handling a GET request and processing the response

response = tenant.get("/some_endpoint")

if response["status"] != "success":
    # Handle the error response
    print("Error:", response["message"], response["data"])
else:
    # Handle the successful response
    print("Content retrieved:", response["data"])
```

**Explanation**

- **`response["status"] != "success"`**: Checks if the request failed. If true, it prints the error message and details.
- **`print("Error:", response["message"], response["data"])`**: Displays the error message and the details from the error response.
- **`print("Content retrieved:", response["data"])`**: Prints the data retrieved from the successful response. 



Here is the corrected statement with the updated response format:

### Public Methods

**`get(endpoint, **kwargs)`**\
  **Parameters**:\
    `endpoint`: The API endpoint to send a GET request to.\
    `**kwargs`: Additional keyword arguments to pass to the `requests.get` method.
  **Returns**: A dictionary with `status`, `message`, and `data` (on success) or `status`, `message`, and `data` (on failure).\
The `data` field contains the response data on success or error details on failure.

**`post(endpoint, **kwargs)`**\
  **Parameters**:\
    `endpoint`: The API endpoint to send a POST request to.\
    `**kwargs`: Additional keyword arguments to pass to the `requests.post` method.
  **Returns**: A dictionary with `status`, `message`, and `data` (on success) or `status`, `message`, and `data` (on failure).\
  The `data` field contains the response data on success or error details on failure.

**`patch(endpoint, **kwargs)`**\
  **Parameters**:\
    `endpoint`: The API endpoint to send a PATCH request to.\
    `**kwargs`: Additional keyword arguments to pass to the `requests.patch` method.
  **Returns**: A dictionary with `status`, `message`, and `data` (on success) or `status`, `message`, and `data` (on failure).\
  The `data` field contains the response data on success or error details on failure.

**`delete(endpoint, **kwargs)`**\
  **Parameters**:\
    `endpoint`: The API endpoint to send a DELETE request to.\
    `**kwargs`: Additional keyword arguments to pass to the `requests.delete` method.
  **Returns**: A dictionary with `status`, `message`, and `data` (on success) or `status`, `message`, and `data` (on failure).\
  The `data` field contains the response data on success or error details on failure.

**`put(endpoint, **kwargs)`**\
  **Parameters**:\
    `endpoint`: The API endpoint to send a PUT request to.\
    `**kwargs`: Additional keyword arguments to pass to the `requests.put` method.
  **Returns**: A dictionary with `status`, `message`, and `data` (on success) or `status`, `message`, and `data` (on failure).\
  The `data` field contains the response data on success or error details on failure.

**`close()`**\
  **Description**: Closes the session if it's open.

### Usage examples

### Example with Context Manager

```python
import TenantAPI

client_id = "client_id"
client_secret = "client_secret"

with TenantAPI.Tenant(client_id, client_secret) as tenant:
    # GET request
    response = tenant.get("/some/endpoint")
    if response["status"] == "success":
        print("GET Data:", response["data"])
    else:
        print("GET Error:", response["message"], "Details:", response["data"])

    # POST request
    response = tenant.post("/another/endpoint", json={"key": "value"})
    if response["status"] == "success":
        print("POST Data:", response["data"])
    else:
        print("POST Error:", response["message"], "Details:", response["data"])

    # PATCH request
    response = tenant.patch("/update/endpoint", json={"update_key": "new_value"})
    if response["status"] == "success":
        print("PATCH Data:", response["data"])
    else:
        print("PATCH Error:", response["message"], "Details:", response["data"])

    # DELETE request
    response = tenant.delete("/remove/endpoint")
    if response["status"] == "success":
        print("DELETE Data:", response["data"])
    else:
        print("DELETE Error:", response["message"], "Details:", response["data"])

    # PUT request
    response = tenant.put("/replace/endpoint", json={"replace_key": "new_value"})
    if response["status"] == "success":
        print("PUT Data:", response["data"])
    else:
        print("PUT Error:", response["message"], "Details:", response["data"])
```

### Example without Context Manager

```python
import TenantAPI

client_id = "client_id"
client_secret = "client_secret"

# Initialize Tenant
tenant = TenantAPI.Tenant(client_id, client_secret)

try:
    # GET request
    response = tenant.get("/some/endpoint")
    if response["status"] == "success":
        print("GET Data:", response["data"])
    else:
        print("GET Error:", response["message"], "Details:", response["data"])

    # POST request
    response = tenant.post("/another/endpoint", json={"key": "value"})
    if response["status"] == "success":
        print("POST Data:", response["data"])
    else:
        print("POST Error:", response["message"], "Details:", response["data"])

    # PATCH request
    response = tenant.patch("/update/endpoint", json={"update_key": "new_value"})
    if response["status"] == "success":
        print("PATCH Data:", response["data"])
    else:
        print("PATCH Error:", response["message"], "Details:", response["data"])

    # DELETE request
    response = tenant.delete("/remove/endpoint")
    if response["status"] == "success":
        print("DELETE Data:", response["data"])
    else:
        print("DELETE Error:", response["message"], "Details:", response["data"])

    # PUT request
    response = tenant.put("/replace/endpoint", json={"replace_key": "new_value"})
    if response["status"] == "success":
        print("PUT Data:", response["data"])
    else:
        print("PUT Error:", response["message"], "Details:", response["data"])

finally:
    # Ensure session is closed
    tenant.close()
```
---

**Summary**

- **`get(endpoint, **kwargs)`**: Retrieve data from the specified endpoint.
- **`post(endpoint, **kwargs)`**: Send data to the specified endpoint (e.g., for creating resources).
- **`patch(endpoint, **kwargs)`**: Update data at the specified endpoint.
- **`delete(endpoint, **kwargs)`**: Delete the resource at the specified endpoint.
- **`put(endpoint, **kwargs)`**: Replace or create data at the specified endpoint.

Each method returns a dictionary with the following structure:
- **`status`**: Indicates whether the request was successful or resulted in an error.
- **`message`**: Provides a brief description of the status (e.g., "Request successful" or "Request failed").
- **`data`**: Contains the actual response data on success, or error details on failure.
