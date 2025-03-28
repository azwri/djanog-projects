# Starter Django Project

This is a starter project for Django development. It includes a pre-configured virtual environment and the necessary dependencies to get started quickly.

## Features
- Pre-installed **Django** framework.
- Pre-installed **Pillow** library for image processing.
- Ready-to-use virtual environment.

## Getting Started

### 1. Copy the Starter Project
To create a new project based on this starter template, run the following command:
```bash
cp -r _starter_project <new_project_name>
```
Replace `<new_project_name>` with the desired name of your new project.

### 2. Activate the Virtual Environment
Navigate to your new project directory and activate the virtual environment:
```bash
cd <new_project_name>
source venv/bin/activate
```

### 3. Install Additional Dependencies (if needed)
You can install additional Python packages using `pip`:
```bash
pip install <package_name>
```

### 4. Run the Development Server
Start the Django development server to verify everything is working:
```bash
python manage.py runserver
```

## Additional Instructions

### Check `.gitignore`
If your `.gitignore` file is not properly ignoring any files or folders, you can reset your branch to the main branch:
```bash
git branch -M main
```
if error in push run
```
git reset --hard HEAD~1
git config --list
git config user.email 
```

### Customize Your Project
Feel free to modify the project structure, settings, and dependencies to suit your needs.

## Notes
- Ensure you have Python installed on your system.
- Always activate the virtual environment before running any Django commands.

Happy coding!

## Update
- to add tailwind
```
 npm install 
 # or
 npm install tailwindcss @tailwindcss/cli
 # then
 mkdir -p static/tailwind
 touch static/tailwind/input.css
 touch static/tailwind/output.css
 mkdir -p templates/tailwind
 touch templates/tailwind/index.html
 echo '@import "tailwindcss";' > static/tailwind/input.css
```

- add in templates/tailwind/index.html

```
<link href="{% static 'tailwind/output.css' %}" rel="stylesheet">
```

- add in settings.py

```
'DIRS': [BASE_DIR / 'templates'],


STATICFILES_DIRS = [BASE_DIR / "static"]
```

- add in urls.py for static files

```
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

- run to compile

```
  npx @tailwindcss/cli -i ./static/tailwind/input.css -o ./static/tailwind/output.css --watch
```