from playwright.sync_api import sync_playwright

def execute_rpa(invoice):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()
        print("Abriendo formulario...", flush=True)
        page.goto(
            "http://localhost:5000/rpa-demo"
        )
        print("Llenando datos...", flush=True)
        page.fill(
            "#invoice_number",
            invoice.invoice_number or ""
        )

        page.fill(
            "#supplier",
            invoice.supplier.name
            if invoice.supplier
            else ""
        )

        page.fill(
            "#nit",
            invoice.nit or ""
        )

        page.fill(
            "#subtotal",
            str(invoice.subtotal or "")
        )

        page.fill(
            "#tax",
            str(invoice.tax or "")
        )

        page.fill(
            "#total",
            str(invoice.total or "")
        )

        page.click("#save_btn")

        page.wait_for_selector(
            "#success"
        )
        print("RPA completado", flush=True)

        browser.close()

