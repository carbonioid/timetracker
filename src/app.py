import traceback
from flask import Flask, Response
from backend.timetracker.app import timetracker_bp
from backend.diary.app import diary_bp
import sys

app = Flask(__name__)
app.register_blueprint(timetracker_bp, url_prefix='/timetracker')
app.register_blueprint(diary_bp, url_prefix='/diary')

@app.errorhandler(Exception)
def handle(e):
    print(f'Error occured: {e}')
    traceback.print_exception(e)
    return Response(response=f'Something went wrong: {e}', status=500)

if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = 8000

app.run(port=port, host="0.0.0.0")
