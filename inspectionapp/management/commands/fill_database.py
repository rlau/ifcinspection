from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from inspectionapp.models import House

	help = 'Initializes database with house data'

	def handle(self, *args, **options):
		abbrs = ['AEP', 'ADP', 'ASP', 'BTP', 'CP', 'DKE', 'DTD', 'DU', 
		'KS', 'LCA', 'ND', 'PBE', 'PDT', 'PKS', 'PKT', 'PLP', 'SAE', 'SPE', 'SC',
		'SN', 'TEP', 'TC', 'TDC', 'TX', 'ZBT', 'ZP']
		point_name = ['isaacs', 'aheifetz', 'imgorodi', 'laverdi', 'rradway',
		'asnoakes', 'colella', 'izunna', 'alowayed', 'porrson', 'eshirley',
		'cvilanil', 'eugeneoh', 'pheyse93', 'tkamath1', 'akessler', 'lsegall', 'rarobins',
		'mwburr888', 'acadams', 'nrivera', 'daksel', 'adamyala', 'epace', 'jaffea', 'dalext']

		if len(abbrs) != len(point_name):
			raise CommandError('Nonmatching lists')

		for i in range(len(abbrs)):
			user = User.objects.create_user(user=abbrs[i], password=point_name[i])
			user.save()

		house_names = ['Alpha Epsilon Pi', 'Alpha Delta Phi', 'Alpha Sigma Phi', 'Beta Theta Pi',
		'Chi Phi', 'Delta Tau Delta', 'Delta Upsilon', 'Kappa Sigma', 'Lambda Chi Alpha', 
		'Nu Delta', 'Phi Beta Epsilon', 'Phi Delta Theta', 'Phi Kappa Sigma', 'Phi Kappa Theta',
		'Pi Lambda Phi', 'Sigma Phi Epsilon', 'Sigma Chi', 'Sigma Nu', 'Tau Epsilon Phi',
		'Theta Chi', 'Theta Delta Chi', 'Theta Xi', 'Zeta Beta Tau', 'Zeta Psi']

		assignments = [('ZBT', 'SAE'), ('ZP', 'TDC'), ('None', 'None'), ('None', 'None'),
		('PKT', 'TEP'), ('KS', 'PBE'), ('ND', 'PLP'), ('SPE', 'TC'), ('DKE','PBE'),
		('PDT', 'TX'), ('DTD', 'PLP'), ('KS', 'DKE'), ('LCA', 'TX'), ('PSK', 'SN'),
		('ND', 'DTD'), ('ZBT', 'SAE'), ('DU', 'TC'), ('None', 'None'), ('PSK', 'PKS'), ('CP', 'PKT'),
		('DU', 'SPE'), ('ZP', 'ADP'), ('LCA', 'PDT'), ('AEP', 'SAE'), ('ADP', 'TDC')]



