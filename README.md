# Mins (Movies Insights)  

## Description  
**Mins** is a Movie Review API built using **Django** and **Django REST Framework (DRF)**. This API allows users to manage movie reviews through actions such as adding, updating, deleting, and viewing reviews. It also encourages interactions through features like commenting and liking reviews.  

## Core Features  
- **User Registration and Authentication**: Secure user authentication and management.  
- **Filtering, Searching, and Sorting**: Easily find movies, reviews, and comments based on various parameters.  
- **Movie Rating**: Users can rate movies through reviews.  
- **Engagement Features**: Commenting and liking functionalities for reviews.  
- **Permissions and Role Management**: Enforces strict permission checks for different user roles and actions.  

## API Endpoints  

### **Users**  
- **Authentication**:  
  - `POST /register/` - User registration  
  - `POST /login/` - User login  
  - `POST /logout/` - User logout  
- **Profile Management**:  
  - `GET /profile/` - View user profile  
  - `PUT /profile/` - Update user profile  

### **Movies**
- **General Actions**:
   - `GET /movies/` - Retrieve a list of movies  
  - `GET /movies/<slug>/` - Retrieve a specific movie
- **Staff-Only Actions**:
  - `POST /movies/` - Create a movie    
  - `PUT /movies/<slug>/` - Update a movie  
  - `DELETE /movies/<slug>/` - Delete a movie  

### **Reviews**  
- **General Actions**:  
  - `POST /reviews/` - Create a review  
  - `GET /reviews/` - Retrieve a list of reviews  
  - `GET /reviews/<slug>/` - Retrieve a specific review  
- **Restricted Actions**:  
  - `PUT /reviews/<slug>/` - Update a review (author only)  
  - `DELETE /reviews/<slug>/` - Delete a review (author only)  

### **Comments**  
- **General Actions**:  
  - `POST /comments/` - Add a comment to a review  
  - `GET /comments/` - Retrieve a list of comments  
- **Restricted Actions**:  
  - `PUT /comments/<slug>/` - Update a comment (author only)  
  - `DELETE /comments/<slug>/` - Delete a comment (author only)  
etc
## Tools and Libraries  
The following tools and libraries are used in this project:  
- **Django**: A high-level Python web framework for rapid development.  
- **Django REST Framework (DRF)**: A toolkit for building Web APIs.  
- **Pillow (11.0.0)**: An image processing library.  
- **PyJWT (2.10.1)**: A library for handling JSON Web Tokens.  
- **Django REST Framework SimpleJWT (5.3.1)**: A JWT authentication library for DRF.  

## Getting Started  

### Prerequisites  
- Python 3.9+  
- Pip (Python package manager)  

### Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/mins-api.git  
   cd mins-api  
   ```  
2. Create a virtual environment and activate it:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  
3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
4. Run database migrations:  
   ```bash  
   python manage.py migrate  
   ```  
5. Start the development server:  
   ```bash  
   python manage.py runserver  
   ```  

### Usage  
- Access the API at `http://127.0.0.1:8000/api/`.  
- Use tools like **Postman** or **cURL** to test the endpoints.  

## Contributing  
Contributions are welcome! Please fork the repository and submit a pull request for any changes.  

## License  
This project is licensed under the [MIT License](LICENSE).  

