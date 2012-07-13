# Server Density Plugins

Plugins for [Server Density](http://serverdensity.com/) monitoring solution.

## Install

The most simplest way to install plugins is to clone this repository to some folder on your machine and create symlink for each needed plugin to sd-agent's plugins directory.

``` bash
$ git clone git@github.com:alexeyshockov/sd-plugins.git /usr/local/share/sd-agent/plugins/alexeyshockov
$ ln -s /usr/local/share/sd-agent/plugins/alexeyshockov/EximQueueSize.py \
        /usr/bin/sd-agent/plugins/EximQueueSize.py
$ ln -s /usr/local/share/sd-agent/plugins/alexeyshockov/RsnapshotLag.py \
        /usr/bin/sd-agent/plugins/RsnapshotLag.py
```
