
import multiprocessing
workers = multiprocessing.cpu_count()*2+1
bind='unix:app.sock'
umask=0o007
reload=True
accesslog = '_'
errorlog='_'