Here’s a **step-by-step guide** to implement the **Analytics Chatbot** with **Clean Architecture**, ensuring that the back-end uses **PynamoDB** for DynamoDB interactions and **API Gateway** for REST endpoints.

---

### **1. Project Initialization**

1. **Set Up the Project**:
   - Create a Python project directory: `analytics-chatbot-backend`.
   - Set up a virtual environment and install necessary dependencies:
     - `pynamodb` for DynamoDB interaction.
     - `boto3` for AWS service integration.
     - Any necessary libraries for testing and logging (e.g., `pytest`, `loguru`).

2. **Define Folder Structure**:
   - Use a feature-based folder structure with Clean Architecture principles:
     ```
     analytics-chatbot/
     ├── features/
     │   ├── create_prompt_request/
     │   │   ├── domain/          # Business logic interfaces and entities
     │   │   ├── usecases/        # Core use case for creating requests
     │   │   ├── infrastructure/  # PynamoDB implementation for DynamoDB
     │   │   ├── presentation/    # Handlers for API Gateway
     │   │   └── tests/           # Unit tests for create_prompt_request
     │   ├── process_prompt/
     │   │   ├── domain/
     │   │   ├── usecases/
     │   │   ├── infrastructure/
     │   │   ├── presentation/
     │   │   └── tests/
     │   ├── fetch_result/
     │       ├── domain/
     │       ├── usecases/
     │       ├── infrastructure/
     │       ├── presentation/
     │       └── tests/
     ├── infra/                   # AWS configurations (IAM, S3, etc.)
     ├── shared/                  # Shared utilities or entities
     ├── tests/                   # End-to-end and integration tests
     ├── README.md
     ├── requirements.txt
     └── .gitignore
     ```

---

### **2. Feature: Create Prompt Request**

#### **2.1 Domain Layer**
1. Define the entity for a `PromptRequest`:
   - Attributes: `request_id`, `human_prompt`, `status`, `result_url`, `user_id`.

2. Create an interface for the repository:
   - Specify methods for creating and saving requests.

#### **2.2 Application Layer**
1. Implement the core use case for creating a prompt request:
   - Accept user input (e.g., `prompt`).
   - Generate a unique `request_id`.
   - Validate the input and ensure all required fields are present.
   - Pass the data to the repository for persistence.

#### **2.3 Infrastructure Layer**
1. Implement the repository using **PynamoDB**:
   - Define a PynamoDB model for the `PromptRequests` table.
   - Implement methods to save prompt requests to DynamoDB.

#### **2.4 Presentation Layer**
1. Define an API Gateway handler:
   - Map the incoming request to the use case.
   - Parse the body for `prompt` and `user_id`.
   - Return the `request_id` upon successful creation.

#### **2.5 Testing**
1. Write unit tests for the:
   - Entity logic (validations, default values).
   - Use case for request creation.
   - PynamoDB repository (mock AWS DynamoDB responses).

---

### **3. Feature: Process Prompt**

#### **3.1 Domain Layer**
1. Define the contract for a **translator service**:
   - Specify a method to translate natural language prompts into SQL.
2. Define the contract for an **Athena query executor**:
   - Specify methods for executing SQL queries and retrieving results.

#### **3.2 Use Case Layer**
1. Implement the use case for processing a prompt:
   - Check the status of the `PromptRequest` in DynamoDB.
   - Use the translator service to convert the prompt to SQL.
   - Query the AWS Glue Data Catalog for metadata if necessary.
   - Execute the SQL query in Athena.
   - Save the query results to an S3 bucket.
   - Update the `PromptRequest` with `PROCESSED` status and the S3 result URL.

#### **3.3 Infrastructure Layer**
1. Implement the translator service:
   - Integrate with the external LLM API for SQL generation.
   - Handle errors or edge cases for unsupported queries.

2. Implement the Athena executor:
   - Use `boto3` to submit SQL queries to Athena.
   - Configure the output location in S3 for results.

3. Integrate the process with DynamoDB Streams:
   - Use a Lambda function to trigger prompt processing when a new record is inserted into the `PromptRequests` table.

#### **3.4 Presentation Layer**
1. Ensure the handler for processing is decoupled from DynamoDB Streams:
   - Create an adapter to extract stream data and pass it to the use case.

#### **3.5 Testing**
1. Mock DynamoDB Streams and S3 responses.
2. Write unit tests for:
   - Translating prompts to SQL.
   - Query execution and result storage.
   - DynamoDB updates after processing.

---

### **4. Feature: Fetch Results**

#### **4.1 Domain Layer**
1. Define a contract for the repository to fetch request details by `request_id`.

#### **4.2 Use Case Layer**
1. Implement the use case for fetching request results:
   - Query the repository for the `PromptRequest` by `request_id`.
   - Return the status or `result_url` based on the current state.

#### **4.3 Infrastructure Layer**
1. Implement the repository method to fetch records using PynamoDB:
   - Handle `DoesNotExist` exceptions for missing records.

#### **4.4 Presentation Layer**
1. Define an API Gateway handler:
   - Extract the `request_id` from the path parameters.
   - Call the use case to fetch the result or status.
   - Return the response to the user.

#### **4.5 Testing**
1. Write unit tests for:
   - Fetching records from DynamoDB.
   - Handling missing or invalid `request_id`.

---
