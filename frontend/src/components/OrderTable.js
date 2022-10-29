function OrderTable(props){
    return (
        <table>
            <thead>
            <tr>
                <th scope="col">Price</th>
                <th scope="col">Quantity</th>
            </tr>
            </thead>
            <tbody>
                {
                    props.buyPending.map((order) => {
                        return <tr key={order.id}><td>{order.price}</td><td>{order.quantity}</td></tr>
                    })
                }
            </tbody>
        </table>
    );
}

export default OrderTable;