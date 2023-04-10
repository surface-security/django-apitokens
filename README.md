# django-apitokens

Generate tokens compatible with Django Restframework (`drf`) from your Django Admin view:
- Create new tokens at will (after being generated, they no longer can be reversed, since only a digest is stored in the database).
- Add expirity dates (supports time and date)
- Remove tokens when you no longer need them.

## My Token view

![Screenshot 2023-03-21 at 14 47 02](https://user-images.githubusercontent.com/7786556/226643622-893b631d-d353-4833-8def-78f61ea77561.png)


## Add token view

![Screenshot 2023-03-21 at 14 47 19](https://user-images.githubusercontent.com/7786556/226643580-ac761fd7-91a9-4c5c-898b-4cc1daf9d812.png)


# Install

- Install the python package: `pip install django-apitokens` 
- Add `apitokens` to your Django installed apps:

```python
# In your settings.py
INSTALLED_APPS = [
    ...
    'apitokens',
]
```

If you are not using `knox` already, you will need to add it to the `INSTALLED_APPS` list too.

- Ensure you are using `knox` `TokenAuthentication` class:

```python
# In your settings.py
REST_FRAMEWORK = {
    ...,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'knox.auth.TokenAuthentication',
        ...,
    ),
    ...,
}
```

- You are set to use tokens generated through this app as a way to login with the DRF framework.

## Django Surface Theme

If you are using [`django-surface-theme`](https://github.com/surface-security/django-surface-theme) as your project theme, you can add an entry to the user menu like the below:

![Screenshot 2023-04-10 at 22 02 03](https://user-images.githubusercontent.com/7786556/230999091-00439ccf-bb8a-4d1d-a541-9a5a0cf6f330.png)

To do so, in your app template's directory (create one if it does not exist):
- Create a `templates` directory inside your project root (in this case, `testapp`). Ensure this folder, if you opt for another structure, is in the `settings.py` template configuration list.
- Create a `includes` directory inside the template's folder
- Create a `navigation.html` file inside the `includes` directory, with the following code:

```
{% block menu_options %}
<div class="dropdown-divider"></div>
<a class="dropdown-item" href="{% url 'admin:auth_user_change' request.user.pk %}">Profile</a>
<a class="dropdown-item" href="{% url 'admin:apitokens_mytoken_changelist' %}">API Tokens</a>
{% endblock %}
```

A structure example and code is provided in the `testapp` of this repository, **although it will not work because this app is not using the `django-surface-theme` (for wider compatibility).

# Contributing

To contribute code to this app, ensure you're following the [community guidelines](https://github.com/surface-security/guidelines#contributing)
