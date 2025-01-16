import os

from flask import Flask, render_template


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def index():
    # map_filename = 'maps/map.html'

    # try:
    #     is_empty = os.stat(map_filename).st_size == 0
    #     return render_template(map_filename) if not is_empty else render_template('issues.html')
    # except FileNotFoundError:
    #     print("File doesn't exists!!!")
    #     return render_template('issues.html')
    return render_template('maps/map.html')

@app.route('/zen_OcwEuEd7DfwwOym0krptopa4c2t49LfvcByCb35EbK9qo8jrKUmeHk7WxK1sREOb.html')
def zen_verification():
    return render_template('zen_OcwEuEd7DfwwOym0krptopa4c2t49LfvcByCb35EbK9qo8jrKUmeHk7WxK1sREOb.html') 


@app.route('/yandex_c3364dcd2302406c.html')
def yandex_verification():
    return render_template('yandex_c3364dcd2302406c.html') 


# @app.errorhandler(503)
# def internal_error(error):
#     return render_template('issues.html'), 503


# @app.errorhandler(503)
# def internal_error(error):
#     return render_template('issues.html'), 503


# @app.errorhandler(500)
# def internal_error(error):
#     return render_template('issues.html'), 500


# @app.errorhandler(500)
# def internal_error(error):
#     return render_template('issues.html'), 500


if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(host='0.0.0.0', port=5000, debug=False)
