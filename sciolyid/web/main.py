import flask
from sentry_sdk import capture_exception

from sciolyid.web.blueprints import upload, user
from sciolyid.web.config import app, logger

app.register_blueprint(user.bp)
app.register_blueprint(upload.bp)


@app.route("/")
def api_index():
    logger.info("index page accessed")
    return "<h1>Hello!</h1><p>This is the index page for the sciolyid internal API.<p>"


@app.errorhandler(403)
def not_allowed(e):
    capture_exception(e)
    return flask.jsonify(error=str(e)), 403


@app.errorhandler(404)
def not_found(e):
    return flask.jsonify(error=str(e)), 404


@app.errorhandler(406)
def input_error(e):
    capture_exception(e)
    return flask.jsonify(error=str(e)), 406


@app.errorhandler(500)
def other_internal_error(e):
    capture_exception(e)
    return flask.jsonify(error=str(e)), 500


@app.errorhandler(503)
def internal_error(e):
    capture_exception(e)
    return flask.jsonify(error=str(e)), 503
