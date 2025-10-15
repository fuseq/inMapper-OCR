# main.py - Güncellenmiş Hali

from app import create_app
from app.api import register_routes
from flask_cors import CORS # 1. Adım: CORS'u import edin

app = create_app()

# 2. Adım: CORS'u tüm route'lar için uygulamanıza uygulayın
# Bu, tüm alan adlarından gelen isteklere izin verecektir (*).
CORS(app)

register_routes(app)

if __name__ == '__main__':
    # Not: debug=True modunda çalıştırmanız test aşamasında faydalı olabilir.
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000)