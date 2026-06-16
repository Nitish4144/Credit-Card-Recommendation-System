interface Props {
    title: string;
    value: string;
}
    export default function AnalyticsCard({title,value}:Props){
    return (
        <div className = "big-white p-5 rounded shadow">
            <h3 className="test-grey-500">
                {title}
            </h3>

            <p className="text-2x1 font-bold">
                {value}
            </p>
        </div>

    );
}