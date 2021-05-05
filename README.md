# Setup

プロジェクトディレクトリの新規作成
```
mkdir <directory-name> & cd $_
```

python version の変更
```
pyenv versions 
pyenv local 3.8.2
```

仮想環境構構築
```
python -m venv venv
source venv/bin/activate
```

バージョン確認
```
python -V
```

Django のインストール
```
pip install Django==3.1
pip install django-cors-headers==3.4.0
pip install djangorestframework==3.11.1
pip install djangorestframework-simplejwt==4.6.0
pip install djoser==2.0.3

pip install python-decouple
pip install dj-database-url
pip install dj_static
```

仮想環境停止
```
deactivate
```

以下、Pycharmで実施
```
django-admin startproject <project-name> .
django-admin startapp <app-name>
```

migration
```
python manage.py makemigrations
python manage.py migrate
```