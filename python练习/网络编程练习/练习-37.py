from multiprocessing import Queue
q = Queue(4)
q.put("a")
q.put("b")
q.put()