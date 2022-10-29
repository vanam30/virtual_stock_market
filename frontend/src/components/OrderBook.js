import { useEffect, useState } from 'react';
import store from '../store';
import {connect} from 'react-redux';
import "../App.css";

function OrderBook(){
    const [buyP, update_buyP] = useState(store.getState().buyPending);
    const [sellP, update_sellP] = useState(store.getState().sellPending);
    
    store.subscribe(() => {
        update_buyP(store.getState().buyPending);
        update_sellP(store.getState().sellPending);
    });
    return(
        <div className='row'>
            <div className='col-6'>
                <table className="table">
                    <thead>
                    <tr>
                        <th scope="col">Price</th>
                        <th scope="col">Quantity</th>
                    </tr>
                    </thead>
                    <tbody>
                        {
                            buyP.map((order) => {
                                return <tr key={order.id}><td>{order.price}</td><td>{order.quantity}</td></tr>
                            })
                        }
                    </tbody>
                </table>
            </div>
            <div className='col-6'>
                <table className="table">
                    <thead>
                    <tr>
                        <th scope="col">Price</th>
                        <th scope="col">Quantity</th>
                    </tr>
                    </thead>
                    <tbody>
                        {
                            sellP.map((order) => {
                                return <tr key={order.id}><td>{order.price}</td><td>{order.quantity}</td></tr>
                            })
                        }
                    </tbody>
                </table>
            </div>
        </div>        
    );
}


export default OrderBook;