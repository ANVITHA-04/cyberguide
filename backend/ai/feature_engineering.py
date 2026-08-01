def extract_network_features(connection):

    features = {}

    # Connection status
    features["is_established"] = (
        1 if connection["status"] == "ESTABLISHED"
        else 0
    )

    # Check remote connection
    features["has_remote"] = (
        1 if connection["remote_address"]
        else 0
    )

    # Port analysis
    if connection["local_address"]:

        port = int(
            connection["local_address"].split(":")[-1]
        )

        features["port"] = port

    else:

        features["port"] = 0


    return features