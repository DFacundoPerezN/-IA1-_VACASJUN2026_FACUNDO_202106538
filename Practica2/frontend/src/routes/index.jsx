import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

import Login from "../pages/Login";
import Categories from "../pages/Categories";

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

            </Routes>

        </BrowserRouter>
    );
}