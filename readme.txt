Django Project:
    you can configure both frontend and backend using Django
    you can use pipenv to configure venv for your Django project
    create a Django project using the django-admin cmd and .(to use cur directory)
        - django-admin startproject [projectName] .
        the pipfile consists of dependencies/libraries with version used in the project
        the settings.py file consists of all the configurations that need to be made for
            applications, middlewares, Ip's, Databases etc
        the asgi and wsgi files are mainly used for production based deployment
        the manage.py is a wrapper around Django
            so that you can run your project directory using manage.py by args runserver and port(8000)
        In the Urls.py you can specify(different routes, func reference)
            inside the urlPatterns to performs diff ops based on routes
        once you create the project you get a pre configured admin panel
            to perform cred ops on the models
    once you have created the project you can put multiple apps into that project
        using python manage.py startapp [appName]
        you can import this applications in the urls.py of main project
            and provide a sep path for this application
            also add this app to main projects applications under the settings.py
        you can provide the func implementations under the views.py and export them for use under urls.py
        you can also provide the models and tests for your application
        you can also return/render your templates when request
    you can install django-debug-toolbar using pipenv to provide a interactive design
        for keeping track of the variables and routing
        you should configure this library under the settings.py and turn the debug to True before using
    make sure the you are inside the created venv and the migrations are pushed 
        before re-running the project
    