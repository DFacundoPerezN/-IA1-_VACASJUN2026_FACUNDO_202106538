import {
    BrowserRouter,
    Routes,
    Route,
    Navigate
} from "react-router-dom";

import Login from "../pages/Login/Login";

import Dashboard from "../pages/Dashboard/Dashboard";
import Invoices from "../pages/Invoices/Invoices";
import Suppliers from "../pages/Suppliers/Suppliers";
import Logs from "../pages/Logs/Logs";
import Reports from "../pages/Reports/Reports";

import ProtectedRoute from "./ProtectedRoute";
import MainLayout from "../layouts/MainLayout";

function AppRoutes() {

    return (
        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={
                        <Navigate to="/login" />
                    }
                />

                <Route
                    path="/login"
                    element={<Login />}
                />

                <Route
                    path="/dashboard"
                    element={
                        <ProtectedRoute>
                            <MainLayout>
                                <Dashboard />
                            </MainLayout>
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/invoices"
                    element={
                        <ProtectedRoute>
                            <MainLayout>
                                <Invoices />
                            </MainLayout>
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/suppliers"
                    element={
                        <ProtectedRoute>
                            <MainLayout>
                                <Suppliers />
                            </MainLayout>
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/logs"
                    element={
                        <ProtectedRoute>
                            <MainLayout>
                                <Logs />
                            </MainLayout>
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/reports"
                    element={
                        <ProtectedRoute>
                            <MainLayout>
                                <Reports />
                            </MainLayout>
                        </ProtectedRoute>
                    }
                />

            </Routes>

        </BrowserRouter>
    );
}

export default AppRoutes;