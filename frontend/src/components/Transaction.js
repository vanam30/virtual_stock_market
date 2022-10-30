import store from "../store.js";
import {useState} from "react"

function Transaction(){

    
    const [transactions, update_transactions] = useState(store.getState().transaction);
    store.subscribe(()=>{
        update_transactions(store.getState().transaction);
    });

    return (
        <table className="table">
            <thead>
            <tr>
                <th scope="col">Seller</th>
                <th scope="col">Buyer</th>
                <th scope="col">Quantity</th>
                <th scope="col">Price</th>
            </tr>
            </thead>
            <tbody style={{ overflow: "scroll !important", height: "40px !important" }}>
                {
                    transactions.map((transact) => {
                        return <tr key={transact.id}><td>{transact.seller}</td><td>{transact.buyer}</td><td>{transact.quantity}</td><td>{transact.price}</td></tr>
                    })
                }
            </tbody>
        </table>
    );
}

export default Transaction;