from indeed import get_jobs as get_indeed_jobs
from stackover import get_jobs as get_stackover_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
stackover_jobs = get_stackover_jobs()

jobs = stackover_jobs + indeed_jobs
save_to_file(jobs)
