from . import Request


def get(url, params=None, *, data=None, headers=None, cookies=None, files=None, auth=None,
        timeout=None, allow_redirects=True, proxies=None, hooks=None,
        stream=None, verify=None, cert=None, json=None) -> Request:
    ...


def options(url, params=None, *, data=None, headers=None, cookies=None, files=None, auth=None,
            timeout=None, allow_redirects=True, proxies=None, hooks=None,
            stream=None, verify=None, cert=None, json=None) -> Request:
    ...


def head(url, params=None, *, data=None, headers=None, cookies=None, files=None, auth=None,
         timeout=None, allow_redirects=True, proxies=None, hooks=None,
         stream=None, verify=None, cert=None, json=None) -> Request:
    ...


def post(url, params=None, *, data=None, headers=None, cookies=None, files=None, auth=None,
         timeout=None, allow_redirects=True, proxies=None, hooks=None,
         stream=None, verify=None, cert=None, json=None) -> Request:
    ...


def put(url, params=None, *, data=None, headers=None, cookies=None, files=None, auth=None,
        timeout=None, allow_redirects=True, proxies=None, hooks=None,
        stream=None, verify=None, cert=None, json=None) -> Request:
    ...


def patch(url, params=None, *, data=None, headers=None, cookies=None, files=None, auth=None,
          timeout=None, allow_redirects=True, proxies=None, hooks=None,
          stream=None, verify=None, cert=None, json=None) -> Request:
    ...


def delete(url, params=None, *, data=None, headers=None, cookies=None, files=None, auth=None,
           timeout=None, allow_redirects=True, proxies=None, hooks=None,
           stream=None, verify=None, cert=None, json=None) -> Request:
    ...
