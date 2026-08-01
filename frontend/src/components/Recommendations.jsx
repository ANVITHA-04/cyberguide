function Recommendations({ system }) {

    const recommendations = system.recommendations || [];

    return (
        <div className="recommendations">

            <h2>AI Recommendations</h2>

            {
                recommendations.length > 0 ? (

                    <ul>

                        {recommendations.map((item, index) => (

                            <li key={index}>
                                {item}
                            </li>

                        ))}

                    </ul>

                ) : (

                    <p>No recommendations available.</p>

                )
            }

        </div>
    );
}

export default Recommendations;