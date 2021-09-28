import csv


def save_to_file(jobs):
	file = open('jobs.csv', mode='w', newline='', encoding='UTF-8')
	# id, title, company, location, link

	flds = ['job_id', 'job_title', 'company_name', 'company_location', 'job_link']

	writer = csv.DictWriter(file, flds)

	writer.writeheader()

	for job in jobs:
		writer.writerow(job)

	return

