def application(env,start_response):
    status = "200 OK"
    headers = [
        ("Content_Type", "text/plain")
    ]
    start_response(status, headers)
    return "Never give up"
