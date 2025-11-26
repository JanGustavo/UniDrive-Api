from app import create_app, db
from app.models import Item

app = create_app()

# console context para facilitar debugging
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Item': Item}

if __name__ == '__main__':
    app.run(debug=True)
