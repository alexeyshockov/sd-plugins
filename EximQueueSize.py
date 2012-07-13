#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

class EximQueueSize:
	def __init__(self, agentConfig, checkLogger, rawConfig):
		self.agentConfig = agentConfig
		self.checkLogger = checkLogger
		self.rawConfig = rawConfig

	def run(self):
		data = {
			'requests': 0
		}

		p = subprocess.Popen(('/usr/sbin/exim', '-bpc'), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		stdout, stderr = p.communicate()
		p.wait()

		data['requests'] = int(stdout)

		return data

if __name__ == '__main__':
	o = MailQueueSize(None, None, None)
	print(o.run())
