
let lastid = 0;

let newstate={};

function reducer(state={users:[],actions: [],buyPending: [], sellPending:[], transaction: [], marketPrices: []}, action) {
newstate.actions = [...state.actions, action];
  switch (action.type) {
    case "change_market_price":
        newstate.users = [...state.users];
        newstate.marketPrices = [...state.marketPrices, action.payload.market_price];
        newstate.transaction = [...state.transaction];
        newstate.buyPending = [...state.buyPending];
        newstate.sellPending = [...state.sellPending];
        return newstate;
    case "userAdded":
        newstate.marketPrices = [...state.marketPrices];
        newstate.users = [...state.users, {id: action.payload.id, name: action.payload.name, stocks: action.payload.stocks, fiat: action.payload.fiat}];
        newstate.transaction = [...state.transaction];
        newstate.buyPending = [...state.buyPending];
        newstate.sellPending = [...state.sellPending];
        return newstate;
    case 'add_pending_buy':
        newstate.marketPrices = [...state.marketPrices];
        newstate.users = [...state.users];
        newstate.buyPending = [...state.buyPending, action.payload];
        newstate.sellPending = [...state.sellPending];
        newstate.transaction = [...state.transaction];
        return newstate;
    case 'add_pending_sell':
        newstate.marketPrices = [...state.marketPrices]
        newstate.users = [...state.users];
        newstate.sellPending = [...state.sellPending, action.payload];
        newstate.buyPending = [...state.buyPending];
        newstate.transaction = [...state.transaction];
        return newstate;
    case 'remove_pending_buy':
        newstate.buyPending = state.buyPending.filter((u)=>{return u.id != action.payload.id});
        newstate.marketPrices = [...state.marketPrices];
        newstate.users = [...state.users];
        newstate.sellPending = [...state.sellPending];
        newstate.transaction = [...state.transaction];
        return newstate;
    case 'remove_pending_sell':
        newstate.sellPending = state.sellPending.filter((u)=>{return u.id != action.payload.id});
        newstate.marketPrices = [...state.marketPrices];
        newstate.users = [...state.users];
        newstate.buyPending = [...state.buyPending];
        newstate.transaction = [...state.transaction];
        return newstate;
    case 'update_pending_buy':
        newstate.buyPending = state.buyPending.map((u)=>{if(u.id == action.payload.id){u.quantity = action.payload.quantity;} return u;});
        newstate.marketPrices = [...state.marketPrices];
        newstate.users = [...state.users];
        newstate.sellPending = [...state.sellPending];
        newstate.transaction = [...state.transaction];
        return newstate;
    case 'update_pending_sell':
        newstate.sellPending = state.sellPending.map((u)=>{if(u.id == action.payload.id){u.quantity = action.payload.quantity;} return u;});
        newstate.marketPrices = [...state.marketPrices];
        newstate.users = [...state.users];
        newstate.buyPending = [...state.buyPending];
        newstate.transaction = [...state.transaction];
        return newstate;
    case 'add_transaction':
        newstate.transaction = [...state.transaction, action.payload];
        newstate.marketPrices = [...state.marketPrices];
        newstate.users = [...state.users];
        newstate.buyPending = [...state.buyPending];
        newstate.sellPending = [...state.sellPending];
        return newstate;
    case 'update_user':
        newstate.users = state.users.map((u)=>{if(u.name == action.payload.name){u.stocks = action.payload.stocks; u.fiat = action.payload.fiat;} return u;});
        newstate.marketPrices = [...state.marketPrices];
        newstate.transaction = [...state.transaction];
        newstate.buyPending = [...state.buyPending];
        newstate.sellPending = [...state.sellPending];
        return newstate;
    default:
      return state;
  }
}

export default reducer;