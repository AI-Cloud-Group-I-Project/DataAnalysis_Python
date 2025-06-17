import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name = "get_number")
@app.route(route="get_number")
def get_number(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        number = req_body.get("number")

        if number is None:
            raise ValueError("Missing Number")

        result = int(number) + 1
        response = {'result': result}

        return func.HttpResponse (
            json.dumps(response),
            mimetype = "application/json",
            status_code = 200
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype = "application/json",
            status_code = 400
        )
