
function_desc_for_model = {
    "name": "python_executor",
    "description": "Execute python code, and return the result. Ensure to escape special characters. If you would like to get the result, use `result = xxx`.",
    "parameters": {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "The python code to execute"
            },
        },
        "required": ["code"]
    }
}


def call(parameters):
    code = parameters['code']
    try:
        vars = {}
        exec(code, vars)
    except Exception as e:
        return str(e)
    if 'result' in vars:
        return str(vars['result'])
    else:
        return 'Done with no result. If you would like to get the result, use `result = xxx`.'
