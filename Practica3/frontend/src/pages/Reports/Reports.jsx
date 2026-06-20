function Reports() {

    const downloadCsv = () => {

        window.open(
            "http://localhost:5000/reports/invoices/csv",
            "_blank"
        );
    };

    return (
        <div>

            <h1>Reportes</h1>

            <button
                onClick={downloadCsv}
            >
                Descargar CSV
            </button>

        </div>
    );
}

export default Reports;