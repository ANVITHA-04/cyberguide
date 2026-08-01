import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import Threats from "./pages/Threats";
import Network from "./pages/Network";
import System from "./pages/System";
import Settings from "./pages/Settings";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Dashboard />} />
        <Route path="/login" element={<Login />} />
        <Route path="/network" element={<Network />} />
        <Route path="/threats" element={<Threats />} />
        <Route path="/system" element={<System />} />
        <Route path="/settings" element={<Settings />} />

      </Routes>

    </BrowserRouter>

  );

}

export default App;