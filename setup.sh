
echo "Installing django version 1.7"
pip install django==1.7

echo "Installing jsonfield django-Geojson dependency"
pip install jsonfield

echo "Installing django-geojson"
pip install django-geojson

echo "Installing django-leaflet" 
pip install django-leaflet

echo "Installing djangorestframework"
pip install djangorestframework

cd shuttle

python manage.py migrate

echo "Enter the Username ,email and password for your django app"
python manage.py createsuperuser
