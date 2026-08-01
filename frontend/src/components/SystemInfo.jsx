function SystemInfo({ system }) {
    return (
        <div className="system-info">

            <h2>System Information</h2>

            <div className="info-grid">

                <div className="info-item">
                    <span>Hostname</span>
                    <strong>{system.hostname || "--"}</strong>
                </div>

                <div className="info-item">
                    <span>Operating System</span>
                    <strong>{system.operating_system || "--"}</strong>
                </div>

                <div className="info-item">
                    <span>Processor</span>
                    <strong>{system.processor || "--"}</strong>
                </div>

                <div className="info-item">
                    <span>Boot Time</span>
                    <strong>{system.boot_time || "--"}</strong>
                </div>

            </div>

        </div>
    );
}

export default SystemInfo;