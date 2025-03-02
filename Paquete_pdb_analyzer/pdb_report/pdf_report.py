from fpdf import FPDF

def create_pdf(prot_pdb, plot_name):
    """Genera un reporte PDF con el gráfico de Ramachandran."""
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, f'Report for {prot_pdb}', align='C', ln=True)

        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', align='C')

    pdf = PDF()
    pdf.add_page()
    pdf.image(plot_name, x=10, y=30, w=190)
    pdf.output(f'{prot_pdb}_report.pdf')
