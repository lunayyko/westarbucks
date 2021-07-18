#클라우드에 올리지 않는, 키를 보관하는 곳

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'westarbucks_db',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1', #데이터베이스의 IP주소, 이건 각자의 컴퓨터
        'PORT': '3306',
    }
}

SECRET_KEY ='_9^=58g2r*r(6@q7ugn!fxg-!fo48$7af9i4yn9-1$+bw(i5eq'