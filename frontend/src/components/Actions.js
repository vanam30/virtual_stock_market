import store from "../store.js";
import {useState} from "react"

function Actions(){
    const [transactions, update_transactions] = useState(store.getState().actions);

    store.subscribe(()=>{
        update_transactions(store.getState().actions);
    });


    return (
        <table className="table">
            <thead>
            </thead>
            <tbody>
                {
                    transactions.map((transact,id) => {
                        return <tr key={id}><td>{transact.type}</td></tr>
                    })
                }
            </tbody>
        </table>
    );
}

export default Actions;