import psutil
import socket



def get_network_connections():

    connections = []

    for conn in psutil.net_connections(kind="inet"):

        connections.append({

            "local_address":
                f"{conn.laddr.ip}:{conn.laddr.port}"
                if conn.laddr else None,

            "remote_address":
                f"{conn.raddr.ip}:{conn.raddr.port}"
                if conn.raddr else None,

            "status": conn.status,

            "pid": conn.pid

        })


    return connections



def get_open_ports():

    ports = []

    for conn in psutil.net_connections(kind="inet"):

        if conn.status == "LISTEN":

            ports.append({

                "port": conn.laddr.port,

                "ip": conn.laddr.ip,

                "pid": conn.pid

            })


    return ports