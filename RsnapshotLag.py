#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

# By @megazoll (Vyacheslav Salakhutdinov).
class RsnapshotLag:
	def __init__(self, agentConfig, checkLogger, rawConfig):
		self.agentConfig = agentConfig
		self.checkLogger = checkLogger
		self.rawConfig = rawConfig

	def run(self):
		data = {
			'minutes': 0
		}

		f = open('/var/cache/rsnapshot/last_backup', 'r')

		d1 = datetime.strptime(f.read().strip(), '%Y-%m-%d %H:%M:%S')
		d2 = datetime.utcnow()

		data['minutes'] = int((d2 - d1).seconds / 60)

		return data

if __name__ == '__main__':
	o = Backup(None, None, None)
	print(o.run())
