from rest_framework.request import Request


def get_client_ip(request: Request) -> str:
    """Get the client IP address from the request."""
    return request.META.get("REMOTE_ADDR")
