# Agri-Input Imitation Control System Architcture

# Project File Structure

```
imitation-control
|   .env
|   README.md
|   requirements.txt
|   run.py
|   wsgi.py
|   
+---app
|   |   extensions.py
|   |   forms.py
|   |   models.py
|   |   __init__.py
|   |   
|   +---blueprints
|   |   +---auth
|   |   |   |   forms.py
|   |   |   |   models.py
|   |   |   |   routes.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---static
|   |   |   +---templates
|   |   |   |       login.html
|   |   |   |       register.html
|   |   |   |       
|   |   |   \---__pycache__
|   |   |           routes.cpython-313.pyc
|   |   |           __init__.cpython-313.pyc
|   |   |           
|   |   +---dashboard
|   |   |   |   forms.py
|   |   |   |   models.py
|   |   |   |   routes.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---static
|   |   |   \---templates
|   |   |           dashboard.html
|   |   |           products.html
|   |   |           profile.html
|   |   |           reports.html
|   |   |           upload.html
|   |   |           
|   |   \---shop
|   |       |   forms.py
|   |       |   models.py
|   |       |   routes.py
|   |       |   __init__.py
|   |       |   
|   |       +---static
|   |       \---templates
|   |               cart.html
|   |               checkout.html
|   |               review.html
|   |               shop_shelf.html
|   |               
|   \---__pycache__
|           extensions.cpython-313.pyc
|           __init__.cpython-312.pyc
|           __init__.cpython-313.pyc
|           
+---config
|   |   config.py
|   |   __init__.py
|   |   
|   \---__pycache__
|           config.cpython-313.pyc
|           __init__.cpython-313.pyc
|           
+---instance
|       config.py
|       
+---static
+---templates
|       base.html
|       index.html
```

## Technology Stack Specification


### Core Infrastructure

- **Flask**: Web infrastructure server
- **Bootsrap**: Framework for styling
- **MongoDB**: Data Storage and database functionality
- **Gemini AI**: Customised assiatant for Farmers

### Authentication and Authorization

- **WTForms**: Forms and form validation
- **Flask-Login**: Authentication and authorization
- **Flask-mail**: Email functionality
