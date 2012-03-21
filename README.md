# Server Density Plugins

Experium's plugins for Server Density monitoring solution.

## Install

The most simplest way to install plugins is to clone this repository to some folder on your machine and create symlink for each needed plugin to sd-agent's plugins directory.

``` bash
$ git clone git@github.com:experium/sd-plugins.git /usr/local/share/sd-plugins
$ ln -s /usr/local/share/sd-plugins/MailQueueSize.py /usr/bin/sd-agent/plugins
```