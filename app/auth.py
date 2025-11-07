from flask import request, jsonify

def require_token(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token != "Bearer secrettoken123":
            return jsonify({"error":"Unauthorized"}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper