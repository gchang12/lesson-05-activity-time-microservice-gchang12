git init
heroku create
pip install gunicorn psycopg2
pip freeze > requirements.txt
echo "web: gunicorn main:app" > Procfile
git add .; git commit -a -m "Initial commit"
git push heroku main
heroku open
