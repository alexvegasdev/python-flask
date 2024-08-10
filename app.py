from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        datos = {
            'nombre': request.form['nombre'],
            'gmail': request.form['gmail'],
            'telefono': request.form['telefono'],
            'tipo_prestamo': request.form['tipo_prestamo'],
            'monto': request.form['monto'],

            'fecha_inicio': request.form['fecha_inicio'],
            'fecha_fin': request.form['fecha_fin'],
            'acepto_condiciones': 'acepto' in request.form
        }
        # Procesa los datos aquí
        print(datos)
    
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
