import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

import Login from "../pages/Login";
import Categories from "../pages/Categories";
import Questions from "../pages/Questions";
import Dashboard from "../Dashboard";
import TelegramConfig from "../pages/TelegramConfig";

export default function AppRoutes() {

    return (
        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<Login />}
                />

                <Route
                    path="/categories"
                    element={<Categories />}
                />

                <Route
                    path="/questions"
                    element={<Questions />}
                />

                <Route
                    path="/dashboard"
                    element={<Dashboard />}
                />

                <Route
                    path="/telegram"
                    element={<TelegramConfig />}
                />

            </Routes>

        </BrowserRouter>
    );
}