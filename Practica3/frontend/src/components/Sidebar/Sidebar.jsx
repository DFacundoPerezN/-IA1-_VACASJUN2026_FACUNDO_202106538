import { Link } from "react-router-dom";

function Sidebar() {

    return (
        <div className="sidebar">

            <h2>Invoice OCR</h2>

            <nav>

                <Link to="/dashboard">
                    Dashboard
                </Link>
                <br></br>
                <Link to="/invoices">
                    Facturas
                </Link>
                <br></br>
                <Link to="/suppliers">
                    Proveedores
                </Link>
                <br></br>
                <Link to="/logs">
                    Bitácora
                </Link>
                <br></br>
                <Link to="/reports">
                    Reportes
                </Link>

            </nav>

        </div>
    );
}

export default Sidebar;