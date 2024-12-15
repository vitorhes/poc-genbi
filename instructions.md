### Updated PRD: Analytics Chatbot with Clean Architecture

---

## **Project Title: Analytics Chatbot**

---

### **1. Objective**
Develop an analytics chatbot that allows users to query metadata, execute SQL statements, and generate visualizations from data cataloged in AWS Glue. The system will follow **Clean Architecture** principles to ensure maintainability, testability, and scalability.

---

### **2. Key Features**
1. **Metadata Analysis**  
   - Fetch and display schema information and metadata for tables stored in AWS Glue.

2. **SQL Execution**  
   - Translate natural language prompts into SQL queries and execute them using AWS Athena.

3. **Chart Generation**  
   - Generate and display visual charts based on query results.

4. **Asynchronous Workflow**  
   - Process user prompts asynchronously and return results efficiently.

---

### **3. Scope of Work**
The project will include:
1. A **front-end** chat interface.
2. A **Python-based back-end** system that follows Clean Architecture principles.
3. Integration with AWS Glue, Athena, S3, and an LLM API for natural language processing.

---

### **4. Functional Requirements**
#### **Front-End**
1. **Chat Interface**  
   - Display input box for user prompts and output area for results (text or charts).
   - Use a modern JavaScript framework (React, Vue, Angular) to implement the UI.

2. **API Integration**  
   - `POST /createPromptRequest`: Send user prompts to the back-end.
   - `GET /fetchResult/:request_id`: Poll to check the status or retrieve results.

3. **Chart Visualization**  
   - Integrate a charting library (e.g., Chart.js, D3.js) to display visual results.

#### **Back-End**
1. **API Gateway**
   - Expose REST endpoints:
     - `POST /createPromptRequest`: Create a new prompt request.
     - `GET /fetchResult/:request_id`: Fetch the status or result of a request.

2. **DynamoDB**
   - Store user prompts and their statuses:
     - `request_id`: Unique identifier for the request.
     - `human_prompt`: User's natural language input.
     - `status`: Current state (`PENDING`, `IN_PROGRESS`, `PROCESSED`).
     - `result_url`: S3 URL for the processed result.

3. **Features (Clean Architecture)**
   - **Prompt Handling**  
     - `create_prompt_request`: Handle input from users, generate a `request_id`, and save it in DynamoDB with status `PENDING`.
   - **Prompt Processing**  
     - Process `PENDING` requests by:
       - Translating the user input to SQL using an LLM API.
       - Fetching metadata from Glue (if required).
       - Executing SQL in Athena and saving the results in S3.
       - Updating the request status to `PROCESSED`.
   - **Result Retrieval**  
     - Retrieve the status or result URL for a given `request_id`.

4. **Integration Points**
   - **LLM API**: Process user input to generate SQL queries.
   - **Glue Data Catalog**: Fetch metadata about tables.
   - **Athena**: Execute SQL queries and save results.
   - **S3**: Store query results and charts.

---

### **5. Non-Functional Requirements**
1. **Clean Architecture Principles**
   - Use feature-based folder structure to isolate business logic, interface adapters, and frameworks.
   - Keep logic testable and decoupled from AWS-specific implementations.

---

### **6. Workflow Details**
#### **Front-End Workflow**
1. User sends a query (e.g., "What were the sales in Q3?").
2. The query is sent via `POST /createPromptRequest`.
3. The front-end receives a `request_id` and polls `GET /fetchResult/:request_id` for updates.
4. When the status is `PROCESSED`, the results (text or charts) are displayed.

#### **Back-End Workflow**
1. **Prompt Request Creation**  
   - `create_prompt_request` receives the user query and generates a `request_id`.
   - Saves the request in DynamoDB with status `PENDING`.

2. **Prompt Processing**  
   - A DynamoDB stream triggers processing:
     1. Use LLM API to convert the user query into SQL.
     2. Fetch metadata from Glue if necessary.
     3. Execute SQL in Athena and save the results in S3.
     4. Update DynamoDB with status `PROCESSED` and the result URL.

3. **Fetch Results**  
   - When the front-end polls `fetch_result`, check the status in DynamoDB.
   - If `PROCESSED`, return the S3 URL; otherwise, return the current status.

---

### **7. Data Model**
#### **DynamoDB Table: `PromptRequests`**
| **Attribute**      | **Type**    | **Description**                           |
|--------------------|-------------|-------------------------------------------|
| `request_id`       | String (PK) | Unique ID for the request.                |
| `human_prompt`     | String      | User input.                               |
| `status`           | String      | Request status (`PENDING`, `IN_PROGRESS`, `PROCESSED`). |
| `result_url`       | String      | S3 URL for the result or chart.           |
| `user_id`       | String      | S3 URL for the result or chart.           |
---

### **8. Folder Structure**

```
analytics-chatbot/
├── front-end/
│   ├── public/
│   ├── src/
│   │   ├── components/        # Chat interface components
│   │   ├── services/          # API integration services
│   │   ├── styles/            # CSS/SCSS files
│   │   ├── App.js             # Main app logic
│   │   ├── index.js           # Front-end entry point
│   └── package.json           # Front-end dependencies
│
├── back-end/
│   ├── features/
│   │   ├── create_prompt_request/
│   │   │   ├── presentation/   # API Gateway handlers
│   │   │   ├── usecases/      # Core business logic
│   │   │   ├── infrastructure/# DynamoDB interaction
│   │   │   ├── tests/         # Unit tests for this feature
│   │   ├── process_prompt/
│   │   │   ├── presentation/   # DynamoDB Stream handler
│   │   │   ├── usecases/      # Core processing logic
│   │   │   ├── infrastructure/# Glue, Athena, and S3 interaction
│   │   │   ├── tests/         # Unit tests for this feature
│   │   ├── fetch_result/
│   │       ├── presentation/   # API Gateway handler
│   │       ├── usecases/      # Logic for fetching results
│   │       ├── infrastructure/# DynamoDB interaction
│   │       ├── tests/         # Unit tests for this feature
│
├── infra/
│   ├── dynamodb/              # DynamoDB table setup scripts
│   ├── s3/                    # S3 bucket setup
│   ├── iam/                   # IAM roles and permissions
│   ├── cloudformation/        # Infrastructure templates
│
├── tests/
│   ├── unit/                  # Unit tests
│   ├── integration/           # Integration tests
│   ├── e2e/                   # End-to-end tests
│
├── README.md
├── requirements.txt           # Python dependencies
└── .gitignore
```

