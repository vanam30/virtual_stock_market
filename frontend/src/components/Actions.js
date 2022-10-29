import store from "../store.js";
import {useState} from "react"

function Actions(){
    const [transactions, update_transactions] = useState(store.getState().actions);

    store.subscribe(()=>{
        update_transactions(store.getState().actions);
    });


    return (
        <div class="toast align-items-center text-bg-primary border-0" role="alert" aria-live="assertive" aria-atomic="true">
            <div className="d-flex">
                <div class="toast-body">
                Hello
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>
    );
}

export default Actions;