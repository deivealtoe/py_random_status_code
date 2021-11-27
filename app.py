from flask import Flask
from random import choice

app = Flask(__name__)

statusCodes = {
    101: "Switching Protocols - This code is sent in response to an Upgrade request header from the client and indicates the protocol the server is switching to.",
    200: "Ok - The request succeeded. The result meaning of 'success' depends on the HTTP method: GET: The resource has been fetched and transmitted in the message body. HEAD: The representation headers are included in the response without any message body. PUT or POST: The resource describing the result of the action is transmitted in the message body. TRACE: The message body contains the request message as received by the server",
    201: "Created - The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests.",
    202: "Accepted - The request has been received but not yet acted upon. It is noncommittal, since there is no way in HTTP to later send an asynchronous response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for batch processing.",
    203: "Non-Authoritative Information - This response code means the returned metadata is not exactly the same as is available from the origin server, but is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the 200 OK response is preferred to this status.",
    204: "No Content - There is no content to send for this request, but the headers may be useful. The user agent may update its cached headers for this resource with the new ones.",
    205: "Reset Content - Tells the user agent to reset the document which sent this request.",
    206: "Partial Content - This response code is used when the Range header is sent from the client to request only part of a resource.",
    207: "Multi-Status (WebDAV) - Conveys information about multiple resources, for situations where multiple status codes might be appropriate.",
    208: "Already Reported (WebDAV) - Used inside a <dav:propstat> response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection.",
    300: "Multiple Choice - The request has more than one possible response. The user agent or user should choose one of them. (There is no standardized way of choosing one of the responses, but HTML links to the possibilities are recommended so the user can pick.)",
    400: "Bad Request - The server could not understand the request due to invalid syntax.",
    401: "Unauthorized - Although the HTTP standard specifies 'unauthorized', semantically this response means 'unauthenticated'. That is, the client must authenticate itself to get the requested response.",
    403: "Forbidden - The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server.",
    404: "Not Found - The server can not find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web.",
    500: "Internal Server Error - The server has encountered a situation it does not know how to handle.",
    501: "Not Implemented - The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD."
}

def get_random_status_code_with_message():
    entry_list = list(statusCodes.items())
    random_entry = choice(entry_list)
    return random_entry

def get_status_code(random_entry):
    return random_entry[0]

def get_message(random_entry):
    message = f'{random_entry[0]} - {random_entry[1]}'
    return message

@app.route("/")
def root():
    random_entry = get_random_status_code_with_message()

    status_code = get_status_code(random_entry)
    message = get_message(random_entry)

    print(status_code)

    return message, status_code

if __name__ == '__main__':
    app.run()
