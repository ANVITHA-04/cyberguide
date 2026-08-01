from flask import Blueprint, jsonify

from monitoring.network_monitor import (
    get_network_connections,
    get_open_ports
)


network = Blueprint("network", __name__)


@network.route("/connections")
def connections():

    data = get_network_connections()

    return jsonify(data), 200



@network.route("/ports")
def ports():

    data = get_open_ports()

    return jsonify(data), 200