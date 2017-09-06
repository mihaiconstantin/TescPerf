import click
from datetime import datetime
from tescstorage import StoreCsv
from tescworkers import LinkWorker, PaperDataWorker


# Datetime object.
date = datetime.today()


@click.command()
@click.option('--start', default=date.year - 1, help='The year to start collecting papers from.')
@click.option('--end', default=date.year, help='The year to stop collecting papers at.')
@click.option('--search', default='^title:"experience sampling" OR abstract:"experience sampling"', help='Your search terms (i.e., advanced queries are supported, see "example.com" for details).')
def cli(start, end, search):
	'''Scraps the http://pure.uvt.nl database for TESC performance indicators.'''

	# Collect the links on all pages.
	LinkWorker.extract_all_links(start, end, search)

	# Collect the data for each paper link that is an article.
	PaperDataWorker.extract_all_paper_data(LinkWorker.all_links)

	# Save a .csv file with the results
	storage = StoreCsv(PaperDataWorker.all_papers, path = 'data')
	storage.save()
