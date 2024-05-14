from flask import Flask
from flask import request
app = Flask(__name__)

def is_int(s):
    try: 
        int(s)
    except:
        return False
    else:
        return True

@app.get('/')
def calc_exe():
  try:
    op = request.args.get('op')
    arg_x = request.args.get('x')
    arg_y = request.args.get('y')


    if not is_int(arg_x):
      raise Exception("Query param `x` is not an int")
    if not is_int(arg_y):
      raise Exception("Query param `y` is not an int")

    x = int(arg_x)
    y = int(arg_y)

    if op == "plus":
      return f"{x + y}"
    elif op == "mult":
      return f"{x * y}"
    else:
      raise Exception("Query param `op` should be set to either `plus` or `mult`")  
  except Exception as err:
    return f"Unexpected error: {err}", 500

  


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)