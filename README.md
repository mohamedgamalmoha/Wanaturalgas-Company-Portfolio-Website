# Wanaturalgas Company Portfolio Website 
The Heating and Air Conditioning website is a comprehensive online platform that provides information, products, and services related to heating and cooling systems. 
The website is designed to cater to the needs of homeowners, businesses, and contractors who are looking for reliable solutions for their HVAC needs.
The website features a user-friendly interface that allows visitors to easily navigate through the different sections. 
The homepage provides an overview of the services offered by the company, including installation, repair, maintenance, and replacement of HVAC systems. Visitors can also find information about the different types of heating and cooling systems available in the market.
In addition to information and services, the Heating and Air Conditioning website also offers a range of products such as air filters, thermostats, humidifiers, and air purifiers. These products are designed to enhance the performance of HVAC systems while improving indoor air quality.


## Features
- Provide information about services
- Contact us page
- Request a service
- Posts 
- Customizable admin dashboard


## Used Techs

- Backend with Django
    - Python 3.8 or later
    - [Django](https://www.djangoproject.com/)
    - Accessible from port `8000` for local development
- Frontend app with HTML, CSS, JavaScript (ES2015)
    -  JavaScript features from [ES2015](https://babeljs.io/docs/learn-es2015/) and beyond, transpiled with 
    - [Bootstrap](https://getbootstrap.com/)


## Usage

Steps should be followed to run project correctly 

1. Clone the repository:
    ```shell
    git clone https://github.com/mohamedgamalmoha/wanaturalgas.git
    ```
2. Install virtual environment package - outside project directory -, then activate it:
    ```shell
    pip install virtualenv
    virtualenv env 
    source env/bin/activate (Linux/Mac)
    env\Scripts\activate (Windows)
    ```
3. Navigate to project directory, then install the requirements of the project template by running:
    ```shell
    cd wanaturalgas
    pip install -r requirements.txt
    ```
4. Apply the migrations to create the database:
    ```shell
    python manage.py migrate
    ```
5. Check everything is being set up correctly:
    ```shell
    python manage.py check
    ```
6. Create a superuser account:
    ```shell
    python manage.py createsuperuser
    ```
7. Run server, then got the local [url](http://127.0.0.1:8000/):
    ```shell
    python manage.py runserver 
    ```

If you faced any problems setting up this project **please** feel free to inform us.


## License

This project is licensed under [MIT License](https://opensource.org/licenses/MIT).
