# KisanSetu – Farm-to-market website (React + Vite)

A front-end only prototype of the flowchart. **No API is used** – all data is demo data in `src/data/mockData.js`.

## Run it
```bash
npm install
npm run dev        # open the link shown (usually http://localhost:5173)
```
Demo OTP for every registration: **1234**

## Flowchart → file map
| Flowchart box                                   | File |
|-------------------------------------------------|------|
| Open App                                        | `src/pages/Splash.jsx` |
| Select language                                 | `src/pages/LanguageSelect.jsx` |
| Select user type                                | `src/pages/UserTypeSelect.jsx` |
| Location + Registration & verification          | `src/pages/Register.jsx` (fields in `mockData.js`) |
| Farmer / FPO-FPC dashboard (all 8 boxes)        | `src/pages/farmer/*` |
| Transport provider flow                         | `src/pages/transport/TransportDashboard.jsx` |
| Buyer flow (search → offer → deal → payment)    | `src/pages/buyer/*` |
| Lots: Market lot (sell) / Buyer lot (buy) / Storage lot (store) | `src/pages/farmer/CreateLot.jsx` (chooser) → `MarketLot.jsx`, `BuyLot.jsx`, `StorageLot.jsx` |
| Payment & transaction history (all roles)       | `src/components/Transactions.jsx` |
| Dispute / report a dispute (farmer, buyer)      | `src/components/DisputeCenter.jsx` |

## How it works (easy to debug)
* `App.jsx` is a tiny state machine: `splash → language → userType → register → dashboard`.
* Each dashboard keeps its data in `useState` and passes it down as props.
* Every "action" (accept offer, book transport, pay…) is a small function at the top of the dashboard file – replace it with an API call later.
* All colours and fonts are CSS variables at the top of `src/styles.css`.
