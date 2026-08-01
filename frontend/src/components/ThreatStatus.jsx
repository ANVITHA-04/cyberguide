function ThreatStatus({ system }) {
    return (
        <div className="threat-status">

            <h2>Threat Status</h2>

            <div className="threat-grid">

                <div className="threat-item">
                    <span>Prediction</span>
                    <strong>{system.threat_prediction || "--"}</strong>
                </div>

                <div className="threat-item">
                    <span>Severity</span>
                    <strong>{system.severity || "--"}</strong>
                </div>

                <div className="threat-item">
                    <span>Confidence</span>
                    <strong>
                        {system.confidence
                            ? `${system.confidence}%`
                            : "--"}
                    </strong>
                </div>

            </div>

        </div>
    );
}

export default ThreatStatus;