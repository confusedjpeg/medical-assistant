# medical-assistant/medical-assistant/README.md

# Medical Assistant Application

This project is a web-based application designed to assist users in managing their medications and symptoms. It utilizes machine learning to recommend appropriate medicines based on user-inputted symptoms, particularly for common ailments such as fever, rash, and nausea.

## Features

- User-friendly interface with large buttons and minimalistic design for dementia-friendly usability.
- Input current medicines and symptoms to receive recommendations.
- Integration with APIs like NIH Drug Interaction API, DrugBank, and OpenFDA for accurate medicine data.
- Machine learning model to predict suitable medicines based on symptoms.

## Project Structure

```
medical-assistant
├── src
│   ├── api                # API functions for drug interactions and medicine data
│   ├── ml                 # Machine learning model and training scripts
│   ├── templates          # HTML templates for the web application
│   ├── static             # Static files such as CSS
│   ├── app.py             # Main entry point of the application
│   ├── database.py        # Database connection and queries
│   └── config.py          # Configuration settings
├── tests                  # Unit tests for the application
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables
├── .gitignore             # Git ignore file
└── README.md              # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd medical-assistant
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables in the `.env` file.

5. Run the application:
   ```
   python src/app.py
   ```

## Usage

- Navigate to the homepage to input your current medicines and symptoms.
- The application will analyze the input and provide recommendations based on the machine learning model.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.