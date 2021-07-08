import queue
import threading
import os
import urllib3

target = "google.com"
directory = "users"
filters = ".jpg"

os.chdir(directory)

web_paths = queue.Queue

for r,d,f in os.walk("."):
    for files in f:
        remote_path = "%s%s" % (r,files)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(files)[1] not in filters:
            web_paths.put(remote_path)

def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = "%s%s" % (target, path)

        request = urllib3.request(url)

try:
    response = urllib3.open(request)
    connect = response.read()

    print("[%d] => %s" % (response.code, path))
    response.close()

except urllib3.exceptions.NewConnectionError as error:
    print("failed ")
    pass

for i in range(threads):
    print("spawing thread: %d" % i)
    t = threading.Thread(target=test_remote)
    t.start()