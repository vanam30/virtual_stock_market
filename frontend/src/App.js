import "./App.css";
import axios from "axios";
import { useEffect, useState } from "react";

const USER_URL = "http://127.0.0.1:8000/user";

const App = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios
      .get(USER_URL)
      .then((res) => {
        console.log(res.data);
        setUsers(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);
  return (
    <div className="App">
      <table className="table">
        <thead>
          <tr>
            <th scope="col">Username</th>
            <th scope="col">Stock</th>
            <th scope="col">Fiat</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => {
            return (
              <tr key={user.id}>
                <td>{user.name}</td>
                <td>{user.stocks}</td>
                <td>{user.fiat}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default App;
