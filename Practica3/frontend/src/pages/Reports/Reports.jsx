function Reports() {

    const downloadCsv = () => {

        window.open(
            import.meta.env.VITE_API_URL+"/reports/invoices/csv",
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