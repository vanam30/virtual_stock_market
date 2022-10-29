import React, { useState } from 'react';
import Plot from 'react-plotly.js';
import store from "../store";

function Graph(){
    console.log(store);
    function fetch_data(){
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // Typical action to be performed when the document is ready:
                console.log(xhttp.responseText);
            }
        };
        xhttp.open("GET", "http://127.0.0.1:8000/", true);
        xhttp.send();
    }
    const [plot_data, update_data] = useState([
        {
            x: [1, 2, 3],
            y: [2, 6, 3],
            type: 'scatter',
            mode: 'lines+points',
            marker: {color: 'red'},
        },
    ]);
    return (
        <Plot
            data={plot_data}
            layout={{width: 320, height: 320, title: 'A Fancy Plot'}}
        />
    );
}

export default Graph;