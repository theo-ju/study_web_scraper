import requests
from bs4 import BeautifulSoup

limit = 50
base_url = 'https://kr.indeed.com'
url = f'{base_url}/jobs?q=python&limit={limit}'


# def extract_indeed_pages():
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "html.parser")
#     pagination = soup.find('div', {'class': 'pagination'})
#
#     links = pagination.find_all('a')
#
#     pages = []
#
#     for link in links[:-1]:
#         pages.append(int(link.find('span').string))
#
#     max_page = pages[-1]
#
#     return max_page


def extract_indeed_jobs(last_page):
    extracted_jobs = []

    for page in range(last_page):
        print(f'Extracting Page {page + 1}..... ')
        res = requests.get(f'{url}&start={page*limit}')
        soup = BeautifulSoup(res.text, "html.parser")
        job_cards = soup.find('div', {'id': 'mosaic-provider-jobcards'})
        jobs = job_cards.find_all('a')

        cards = []
        for job in jobs:
            if 'class' in job.attrs:
                if 'tapItem' in job.attrs['class']:
                    cards.append(job)

        for card in cards:
            extracted_job = {}

            # Job ID
            job_id = card['id'].split('_')[1]
            extracted_job['job_id'] = job_id

            # Job Title
            job_title = card.find('h2', {'class': 'jobTitle'})

            if len(job_title.find_all('span')) > 1:
                # print(len(job_title.find_all('span')), job_title, job_title.string)
                # print(job_title.find_all('span')[len(job_title.find_all('span')) - 1].string)
                job_title = job_title.find_all('span')[len(job_title.find_all('span')) - 1].string
            else:
                # print(job_title.string)
                # print(len(job_title.find_all('span')), job_title, job_title.string)
                job_title = job_title.string

            extracted_job['job_title'] = job_title

            # Company Name

            if card.find('span', {'class': 'companyName'}) is not None:
                company_name = card.find('span', {'class': 'companyName'}).string

            else:
                company_name = None

            extracted_job['company_name'] = company_name

            # Company Location
            company_location = card.find('div', {'class': 'companyLocation'})

            if company_location.string is None:
                if company_location.find('span', {'class': 'remote-bullet'}) is not None:
                    company_location = f'{company_location.contents[0]} / 원격근무'

                else:
                    company_location = company_location.contents[0]

            else:
                company_location = company_location.string

            extracted_job['company_location'] = company_location

            # Link
            job_link = f'{base_url}/viewjob?jk={job_id}'
            extracted_job['job_link'] = job_link

            extracted_jobs.append(extracted_job)

    return extracted_jobs


def get_jobs(last_page = 1):
    jobs = extract_indeed_jobs(last_page)

    return jobs

