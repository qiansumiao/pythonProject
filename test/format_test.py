import sys

data = dict(platform=sys.platform, kind='laptop')

print('my %(kind)-8s runs %(platform)8s' % data)

print('my {kind:<8} runs {platform:>8}'.format(**data))

