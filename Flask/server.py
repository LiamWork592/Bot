import logging

from flask import Flask, render_template

console = logging.getLogger('console')
console.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/Clickable/')
def my_link():
  print ('I got clicked!')

  return 'Click.'

def hello():
logger.error('Error logged from Python')
logger.warning('Warning logged from Python')
logger.info('Info logged from Python')
logger.debug('Debug logged from Python')
logger.debug({'foo': ['bar', 'baz']})
return "Hello World!"


if __name__ == '__main__':
  app.run(debug=True)