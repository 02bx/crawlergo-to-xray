import requests
import datetime
import logging
from flask import Flask, request

app = Flask(__name__)


def push_ftqq(plugin,vuln_class,content):
    # TODO：自行修改配置参数
    resp = requests.post("https://sc.ftqq.com/YOURSCKEY.send",
                  data={"text": plugin+"/"+vuln_class, "desp": content})
    if resp.json()["errno"] != 0:
        raise ValueError("push ftqq failed, %s" % resp.text)

@app.route('/webhook', methods=['POST'])
def xray_webhook():
    vuln = request.json
    # 因为还会收到 https://chaitin.github.io/xray/#/api/statistic 的数据
    if "vuln_class" not in vuln:
        return "ok"
    content = """##

url: {url}

插件: {plugin}

漏洞类型: {vuln_class}

发现时间: {create_time}

""".format(url=vuln["target"]["url"], plugin=vuln["plugin"],
           vuln_class=vuln["vuln_class"] or "Default",
           create_time=str(datetime.datetime.fromtimestamp(vuln["create_time"] / 1000)))
    try:
        push_ftqq(vuln["plugin"],vuln["vuln_class"] or "Default",content)
    except Exception as e:
        logging.exception(e)
    return 'ok'


if __name__ == '__main__':
    app.run()

