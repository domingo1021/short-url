from flask import request, jsonify
from functools import wraps
from pydantic import ValidationError
import inspect


def validate_request(dto_class):
    """
    Decorator that validates the incoming JSON request body against a specified Pydantic data transfer object (DTO) class.

    Args:
        dto_class (Type): A Pydantic model class used to validate the incoming request data.

    Returns:
        Function: A wrapper function that performs validation before passing control to the original function.

    Usage:
        @validate_request(MyDTOClass)
        def my_route_handler(dto):
            # Your endpoint logic here, using the validated `dto`
    """
    
    def decorator(f):
        """
        Inner decorator function that wraps the original endpoint function.

        Args:
            f (Function): The original Flask route handler function.

        Returns:
            Function: A wrapped version of the original function with request validation.
        """
        
        @wraps(f)
        async def wrapper(*args, **kwargs):
            """
            Wrapper function that attempts to validate the request data using the DTO class.

            If the validation succeeds, the original function is called with the validated DTO instance.
            If validation fails, an appropriate HTTP error response is returned.

            Args:
                *args: Positional arguments for the original function.
                **kwargs: Keyword arguments for the original function.

            Returns:
                Response: The Flask response object, either from the original function or an error response.
            """
            try:
                dto = dto_class(**request.json)
                
                if inspect.iscoroutinefunction(f):
                    return await f(dto, *args, **kwargs)
                
                return f(dto, *args, **kwargs)
            
            except ValidationError as e:
                return jsonify({"error": e.errors()}), 400
            
            except Exception as e:
                return jsonify({"error": str(e)}), 500
            
        return wrapper
    
    return decorator