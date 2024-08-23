from flask import Flask, render_template_string, jsonify
import boto3

app = Flask(_name_)

# Inicializar el cliente de boto3
s3 = boto3.client('s3')

@app.route('/buckets/json')
def list_buckets_json():
    # Obtener la lista de buckets
    response = s3.list_buckets()
    buckets = response['Buckets']
    
    # Devolver los buckets en formato JSON
    return jsonify(buckets)

@app.route('/buckets/html')
def list_buckets_html():
    # Obtener la lista de buckets
    response = s3.list_buckets()
    buckets = response['Buckets']

    # Definir una plantilla HTML simple que utilice datos JSON
    html_template = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Lista de Buckets en S3</title>
        <script>
          // Función para obtener y mostrar los buckets en la página
          function fetchBuckets() {
            fetch('/buckets/json')
              .then(response => response.json())
              .then(data => {
                const bucketList = document.getElementById('bucket-list');
                data.forEach(bucket => {
                  const li = document.createElement('li');
                  li.textContent = bucket.Name;
                  bucketList.appendChild(li);
                });
              });
          }

          // Llamar a la función cuando la página se haya cargado
          window.onload = fetchBuckets;
        </script>
      </head>
      <body>
        <div class="container">
          <h1>Lista de Buckets en S3</h1>
          <ul id="bucket-list"></ul>
        </div>
      </body>
    </html>
    """

    # Renderizar la plantilla HTML
    return render_template_string(html_template)

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0')