# Delivery Parcel Management System

## Objective

The objective of this project is to develop a delivery parcel management system that tracks and manages parcels from reception to delivery using dummy data. The system will enable users to add, update, track, and report on parcel status and provide real-time updates on long-running tasks, such as bulk parcel processing.

## Technologies Used

1. **HTML/CSS**: For structuring and styling the user interface of the application.
2. **JavaScript**: To implement dynamic features and client-side logic.
3. **Bootstrap**: For designing responsive and modern web layouts quickly.
4. **jQuery**: To simplify HTML document manipulation, event handling, and AJAX interactions.
5. **Python**: For server-side logic and interaction with the database.
6. **Django**: A lightweight web framework to handle HTTP requests and deliver web pages.
7. **SocketIO**: To enable real-time bidirectional communication between web clients and servers.
8. **Pandas**: For handling bulk data operations and transformations.
9. **MySQL**: To store and manage application data like user and parcel information.

## Project Breakdown

### 1. Database Setup

- **Design a MySQL database** for storing users, parcels, and transaction logs.
- **Implement secure user authentication** and role-based access control.

### 2. Backend Development

- **Configure the Django server** and API routes for parcel data operations.
- **Integrate SocketIO** for real-time progress updates.

### 3. Frontend Development

- **Use HTML, CSS, and Bootstrap** to build the user interface.
- **Implement JavaScript and jQuery** for dynamic content updates and API communication.
- **Set up real-time communication** with SocketIO (e.g., showing loaders for backend running tasks like processing parcels).
- **Design Section**:
  - **Use of Template Dashboard for UI Design**: Utilize the Sneat Bootstrap HTML Admin Template to provide themes and styles for a cohesive look.
  - **Single Page Application (SPA)**: Implement the main functionalities on a single page to simplify user interaction. This template will aid in quickly setting up a professional-looking dashboard.
  - **Multiple Pages**: Optionally, add more pages if necessary to separate detailed functionalities.

### 4. Data Processing

- **Use Pandas** for data manipulation during bulk operations or reports.

### 5. Documentation

- **Document the setup process**, API usage, and general system operations.

## Setup and Installation

### Prerequisites

- Python 3.x
- Django
- MySQL
- Git
- A web browser

### Clone the Repository

1. Clone the GitHub repository to your local machine:

    ```bash
    git clone https://github.com/your-username/delivery-parcel-management-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd delivery-parcel-management-system
    ```

### Create a Virtual Environment

1. Create a virtual environment:

    ```bash
    python -m venv env
    ```

2. Activate the virtual environment:

    - **On Windows:**

        ```bash
        .\env\Scripts\activate
        ```

    - **On macOS/Linux:**

        ```bash
        source env/bin/activate
        ```

### Install Dependencies

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1. Create the MySQL database and user, and update the database settings in `settings.py`.

2. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

3. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

### Running the Project

1. Start the development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to:

    ```
    http://127.0.0.1:8000/
    ```

## Login 

To enable login on another system, you can pre-configure user accounts directly in the database or use a script to create users. Ensure that the authentication system is set up to allow these pre-configured users to log in.

### Steps to Login Without Registration

1. **Pre-configure Users**: Add user details directly to the database using Django admin or a custom script.
2. **Use Admin Credentials**: Log in using admin credentials if admin access is enabled.

## API Endpoints

- **Home**: `GET /` - Displays dashboard with parcel statistics.
- **Add Parcel**: `GET /add/` (Form) and `POST /add/` (Submit) - Add a new parcel.
- **Track Parcel**: `GET /track/` (Form) and `POST /track/` (Submit) - Track a parcel by ID.
- **Generate Report**: `GET /generate_report/` - Download a CSV report of parcels.
- **List Parcels**: `GET /list/` - List all parcels.
- **Update Parcel**: `GET /update/<uuid:parcel_id>/` (Form) and `POST /update/<uuid:parcel_id>/` (Submit) - Update parcel details.
- **Profile**: `GET /profile/` - View or update user profile.



## Contact

For any questions or inquiries, please contact [pooja84413@gmail.com](mailto:your-pooja84413@gmail.com).
