function Userrow(prop){
    return(
        <tr key={prop.id}>
            <td>{prop.name}</td>
            <td>{prop.stocks}</td>
            <td>{prop.fiat}</td>
        </tr>
    );
}

export default Userrow;