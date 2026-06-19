interface Props {
    title: string;
    value: string;
}

export default function AnalyticsCard({
    title,
    value
}: Props) {

    return (
        <div className="analytics-card">

            <h3 className="analytics-card-title">
                {title}
            </h3>

            <p className="analytics-card-value">
                {value}
            </p>

        </div>
    );
}
