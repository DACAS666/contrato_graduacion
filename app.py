from flask import Flask, request, render_template, send_file
from fpdf import FPDF
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    buyer_name = request.form['buyerName']
    item_description = request.form['itemDescription']
    price = request.form['price']
    signature = request.form['signature']

    # Convert signature from base64
    signature_data = base64.b64decode(signature.split(',')[1])
    signature_image = BytesIO(signature_data)

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, 'Contrato de Compra', ln=True, align='C')
    pdf.ln(20)
    pdf.set_font('Arial', '', 12)
    pdf.cell(40, 10, f'Nombre del Comprador: {buyer_name}')
    pdf.ln(10)
    pdf.cell(40, 10, f'Descripción del Artículo: {item_description}')
    pdf.ln(10)
    pdf.cell(40, 10, f'Precio: {price}')
    pdf.ln(20)
    pdf.cell(40, 10, 'Firma:')
    pdf.image(signature_image, x=10, y=pdf.get_y(), w=60, h=30)

    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return send_file(pdf_output, attachment_filename='contract.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
