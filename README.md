![](https://github.com/abh2050/postgres_repo_creation/blob/main/pic2.jpg)
# University Data Entry Application

This application allows users to add and manage university data using a web interface built with Streamlit. It interfaces with a PostgreSQL database using SQLAlchemy for managing data storage.

![](https://github.com/abh2050/postgres_repo_creation/blob/main/pic.png)
## Database Table Creation and Data Insertion

https://univdataentry.streamlit.app/

### `create_table` Function
This function dynamically generates a SQL `CREATE TABLE` statement based on the structure of a pandas DataFrame. It sets appropriate SQL data types for each column and handles auto-incrementing primary keys for specified columns.

### `generate_insert_statements` Function
Generates a series of `INSERT INTO` statements to populate a SQL table with data from a pandas DataFrame. Each row of the DataFrame is converted into a corresponding SQL insert statement, ensuring that the data types are appropriately handled for SQL execution.

### Usage Example
```python
import pandas as pd

# Example DataFrame
data = {
    'id': [1, 2],
    'name': ['University A', 'University B'],
    'enrollment': [1500, 3000],
    'location': ['City X', 'City Y']
}
df = pd.DataFrame(data)

# Create SQL table
table_name = 'university'
create_table_sql = create_table(df, table_name)
print(create_table_sql)

# Generate SQL insert statements
insert_statements = generate_insert_statements(df, table_name)
for statement in insert_statements:
    print(statement)
## Database Table: `univ`

This table is designed to store data related to universities. It is hosted on Supabase and structured as follows:

### Table Schema

| Column Name          | Description | Data Type            | Format   |
|----------------------|-------------|----------------------|----------|
| `id`                 | Primary key, usually auto-incrementing | `bigint` | `int8`   |
| `university_name`    | Name of the university | `text`         | `text`   |
| `city`               | City where the university is located | `text`   | `text`   |
| `state`              | State where the university is located | `text`   | `text`   |
| `country`            | Country where the university is located | `text`   | `text`   |
| `founded`            | Year the university was founded | `bigint`     | `int8`   |
| `number_of_students` | Total number of students enrolled | `bigint`   | `int8`   |
| `tuition_fee`        | Tuition fee amount | `double precision` | `float8` |
| `academic_programs`  | Descriptions of academic programs offered | `text` | `text`   |
| `rankings`           | Ranking information of the university | `bigint` | `int8`   |

### Data Handling and Operations

- **Creating the Table**: The table should reflect the structure described above. If creating the table programmatically, adjustments for data types and primary keys (e.g., using `SERIAL` for `id`) should be considered.
- **Inserting Data**: Utilize functions such as `generate_insert_statements` to batch insert data into this table from a pandas DataFrame.
- **Data Retrieval and Updates**: Standard SQL queries can be used for retrieving and updating records in this table.
- **Database Management and Security**: Secure management of database credentials and access is crucial, especially when using cloud-hosted platforms like Supabase. Supabase is an open-source alternative to Firebase, providing developers with a suite of tools to rapidly build and scale their applications. It offers a combination of tools and services that mirror Firebase's capabilities but leverages PostgreSQL as its backend database, which allows for more complex queries and relational data structures.

### Example Usage

The table is utilized in web applications for managing university data, allowing users to input and modify records which are then reflected in the database. This setup is ideal for administrative portals where regular data updates are necessary.

## Features

- **Data Entry Form**: Enter details about universities including name, city, state, country, founding year, number of students, tuition fees, academic programs, and rankings.
- **Database Integration**: Utilizes SQLAlchemy for ORM with PostgreSQL for robust data storage.
- **Session Management**: Manages database sessions to ensure data integrity and connection efficiency.

## How to Run Locally

### Prerequisites

- Python 3.6+
- PostgreSQL database
- Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

### Database Setup

- **For Local Database:**
  - Ensure you have PostgreSQL installed and create a database named `abhi_db`.
  - Modify the `DATABASE_URL` in the script to your local database settings, e.g., `postgresql://postgres:your_password@localhost/abhi_db`.

- **For Remote Database:**
  - Set up your remote PostgreSQL instance and ensure you have the credentials.
  - Replace the `DATABASE_URL` with your remote database URL and credentials.
  - Optionally, store your database password in `pass.txt` and modify the script to read from it if you prefer not to hardcode passwords.

### Running the Application

To start the application, execute:

```
streamlit run your_script_name.py
```

Navigate to `http://localhost:8501` in your web browser to use the app.

## Deployment

The application is deployed on Streamlit Sharing. Access it here:

[University Data Entry App](https://univdataentry.streamlit.app/)



## License

This project is open source and available under the [MIT License](LICENSE).

## Author

- Your Name

Feel free to extend or modify the application as needed. Contributions are welcome!
