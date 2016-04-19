##### overview

- coming

---


### Django Channels info

- [Django Channels documentation](http://channels.readthedocs.org/en/latest/index.html)
- [email-queue tutorial](https://www.wordfugue.com/using-django-channels-email-sending-queue/)
- [Channel example projects](https://github.com/andrewgodwin/channels-examples) -- projects use docker
- [pro-channels blogger](https://brejoc.com/django-channels-are-a-game-changer/)


### Setup

- [project to-do reference](https://gist.github.com/birkin/04a0a124d49be02e3d58)

- √ create stuff directory

        $ mkdir ./dj_channels_exploration_stuff
        $ cd ./dj_channels_exploration_stuff

- √ install virtualenv

        $ virtualenv --python=/usr/bin/python2.7 --prompt=[env27_chnl_expl] --no-site-packages ./env27_chnl_expl

- √ upgrade pip

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

- √ install django project-template

        $ git clone https://github.com/birkin/django_template_project.git ./chnl_expl_project
        $ rm -rf ./chnl_expl_project/.git

- √ customize template
    - app_x -> email_app  (other experimental apps will be added later)
    - django_template_project -> chnl_expl_project
    - env_min -> env27_chnl_expl

- create github project

- add setting file

- get intro references

---
