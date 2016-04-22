##### on this page

- Django Channels info
- Setup notes
- Initial work

---


### Django Channels info

- [Django Channels documentation](http://channels.readthedocs.org/en/latest/index.html)
- [email-queue tutorial](https://www.wordfugue.com/using-django-channels-email-sending-queue/)
- [Channel example projects](https://github.com/andrewgodwin/channels-examples) -- projects use docker
- [pro-channels blogger](https://brejoc.com/django-channels-are-a-game-changer/)

---


### Setup

- [project to-do reference](https://gist.github.com/birkin/04a0a124d49be02e3d58)

- `√` means set up locally; `√√` means set up on dev-server, too

- √√ create stuff directory

        $ mkdir ./dj_channels_exploration_stuff
        $ cd ./dj_channels_exploration_stuff

- √√ install virtualenv

        $ virtualenv --python=/usr/bin/python2.7 --prompt=[env27_chnl_expl] --no-site-packages ./env27_chnl_expl

- √√ upgrade pip

        $ source ./env27_chnl_expl/bin/activate
        $ pip install --upgrade pip
        Downloading/unpacking pip from https://pypi.python.org/packages/py2.py3/p/pip/pip-8.1.1-py2.py3-none-any.whl#md5=22db7b6a517a09c29d54a76650f170eb
          Downloading pip-8.1.1-py2.py3-none-any.whl (1.2MB): 1.2MB downloaded
        Installing collected packages: pip
          Found existing installation: pip 1.5.2
            Uninstalling pip:
              Successfully uninstalled pip
        Successfully installed pip
        Cleaning up...

- √x install django project-template

        $ git clone https://github.com/birkin/django_template_project.git ./chnl_expl_project
        $ rm -rf ./chnl_expl_project/.git

- √x customize template
    - app_x -> email_app  (other experimental apps will be added later)
    - django_template_project -> chnl_expl_project
    - env_min -> env27_chnl_expl

- √x create github project

- √x create sublime project

- √√ update env from requirements

- √√ make log dir
    - √√ add log to system's logrotate
    - √x add dir to sublime project

- √√ make settings dir and env_settings.sh file
    - √x add settings directory to sublime project
    - √ update env_settings.sh file
    - √ update env's activate.py and activate_this.py

- √√ add db

- √ add django-media-directory

- √ make git-pull script (w/set-permissions) & run it
    - √ try a python ./manage.py check

- √ run python ./manage.py migrate to create tables

- √ run python ./manage.py createsuperuser for the admin user prompt

- √ run python ./manage.py runserver host:port, and hit host/port at hello-world url

- √ add session-clearance crontab entry

- √ update passenger-config

---


### Initial work...

- start going through [email-queue tutorial](https://www.wordfugue.com/using-django-channels-email-sending-queue/)

---
