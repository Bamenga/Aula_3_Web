from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calcular_imc():
    resultado = None
    classificacao = None
    
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            
            # Calcula o IMC
            imc = peso / (altura ** 2)
            
            # Classifica o IMC
            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif 18.5 <= imc < 25:
                classificacao = "Peso normal"
            elif 25 <= imc < 30:
                classificacao = "Sobrepeso"
            elif 30 <= imc < 35:
                classificacao = "Obesidade Grau I"
            elif 35 <= imc < 40:
                classificacao = "Obesidade Grau II"
            else:
                classificacao = "Obesidade Grau III"
            
            resultado = f"Seu IMC é {imc:.2f} - {classificacao}"
        
        except ValueError:
            resultado = "Por favor, insira valores válidos"
    
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)