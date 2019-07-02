import click
from logger import grep_manager


@click.command()
@click.option('--topic', default='', help='topic name')
@click.option('--brokers', default='', help='localhost:9092,localhost:9093')
@click.option('--regex', default='', help='in case you are not familiar with regex, you can use free text like usual')
def run_grep_command(topic, brokers, regex):
	"""
	:param str topic:
	:param str brokers:
	:param str regex:
	:rtype: None
	"""
	grep_manager.search_messages_in_parallel(
		topic=topic,
		brokers=brokers,
		regex=regex,
	)


if __name__ == '__main__':
	run_grep_command()
