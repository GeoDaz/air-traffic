const Table = ({ data, headers }) => {
    console.log(data);
    return (
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    {headers.map((h, index) => (
                        <th scope="col" key={index}>
                            {h}
                        </th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {data.map((row, index) => (
                    <tr>
                        <th scope="row">{index + 1}</th>
                        {row.map((col, index) => (
                                <td>{col}</td>
                        ))}
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default Table;
