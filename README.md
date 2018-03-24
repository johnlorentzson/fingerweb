# fingerweb

A web app that might replace finger.{txt,json}.
The first usefull thing it might do is handle service-specific passwords
for some other web apps.

## Local development

To run in development mode, first make sure you have a (virtual) env with
the required packages installed:

```
pip install -r requirements.txt
```

In development mode, a sqlite database is used.  It is created by applying
the migrations:

```
./manage.py migrate
```

Then the server can be started:

```
./manage.py runserver
```

## Production build

A image is built and published to Docker Hub at `stacken/fingerweb:tag` where
tag is `latest` for the master branch, and otherwise the branch name.

https://hub.docker.com/r/stacken/fingerweb/

After a merge to master, `stacken/fingerweb:latest` will be built and a webhook
will restart the production image.