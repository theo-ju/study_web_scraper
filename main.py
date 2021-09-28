from indeed import get_jobs as get_indeed_jobs
from save import save_to_file


def main():
	i_jobs = get_indeed_jobs(15)
	jobs = i_jobs
	save_to_file(jobs)


if __name__ == '__main__':
	main()


