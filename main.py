"""
Ponto de entrada principal para a Vercel e outros servidores WSGI.
Exporta a variável top-level `app`, `application` e `handler`.
"""
from web_app import app

# Exportações padrão exigidas pela Vercel
application = app
handler = app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
