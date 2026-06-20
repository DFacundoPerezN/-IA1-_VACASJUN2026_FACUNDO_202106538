import Sidebar from "../components/Sidebar/Sidebar";

function MainLayout({ children }) {

    return (
        <div
            style={{
                display: "flex",
                minHeight: "100vh"
            }}
        >
            <Sidebar />

            <main
                style={{
                    flex: 1,
                    padding: "20px"
                }}
            >
                {children}
            </main>

        </div>
    );
}

export default MainLayout;