from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Diretório onde as imagens serão armazenadas
UPLOAD_FOLDER = 'imagens'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    # Verifique se o diretório de upload existe
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Obtenha os dados da imagem a partir do request.data
    image_data = request.data

    # Verifique se os dados da imagem não estão vazios
    if not image_data:
        return jsonify({'error': 'Dados da imagem vazios'}), 400
    
    # Nome da imagem
    image_name = get_next_available_name(app.config['UPLOAD_FOLDER'])
    
    # Verifique se um arquivo foi enviado
    with open(os.path.join(app.config['UPLOAD_FOLDER'], image_name), 'wb') as image_file:
        image_file.write(image_data)
        
    return jsonify({'message': 'Imagem enviada com sucesso'})

def get_next_available_name(directory):
    i = 1
    while True:
        image_name = f'f{i}.png'
        if not os.path.exists(os.path.join(directory, image_name)):
            return image_name
        i += 1

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)