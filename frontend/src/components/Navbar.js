// import DensityLogo from '../images/density.jpeg';
import Actions from "./Actions";
import store from "../store";

import { useState } from "react";

export default function Navbar() {
    const [prices,update_prices] = useState(store.getState().marketPrices);

    store.subscribe(()=>{
        update_prices(store.getState().marketPrices);
    });
    return (
        <div>
            <nav className="navbar navbar-dark bg-dark">
                <div className="container-fluid">
                    <div className="navbar-brand" href="#">
                    Current Market Price:&nbsp;
                    {
                        prices.length > 0 ? prices[prices.length-1].price:"NA"
                    }
                    </div>
                    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
                        Notifications
                    </button>
                    <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="staticBackdropLabel">Actions</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <Actions />
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            </div>
                            </div>
                        </div>
                    </div>
                </div>
            </nav>
        </div>
    );
}