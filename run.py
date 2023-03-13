from app.factory import create_app


if __name__ == '__main__':
    connexion_app = create_app()
    connexion_app.run(port=8000, debug=True)
