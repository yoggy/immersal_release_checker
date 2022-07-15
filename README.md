# immersal_release_checker.py

```
$ cd ~
$ mkdir work
$ cd work
$ git clone https://github.com/yoggy/immersal_release_checker.git
$ cd immersal_release_checker
$ cp config.yaml.sample config.yaml
$ vi config.yaml

    # create & set slack webhook url
    slack_webhook_url: https://hooks.slack.com/services/xxxxxxxxxx/xxxxxxxx

$ python3 immersal_release_checker.py
$ python3 immersal_release_checker.py

$ crontab -e

    0 */6 * * * python3 /home/pi/work/immersal_release_checker/immersal_release_checker.py >/dev/null 2>&1

```

## Copyright and license
Copyright (c) 2022 yoggy

Released under the [MIT license](LICENSE)

