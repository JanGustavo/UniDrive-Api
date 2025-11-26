from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import Item
from app.forms import ItemForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    items = Item.query.order_by(Item.created_at.desc()).all()
    return render_template('index.html', items=items)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(title=form.title.data, description=form.description.data)
        db.session.add(item)
        db.session.commit()
        flash('Item criado com sucesso.', 'success')
        return redirect(url_for('main.index'))
    return render_template('create.html', form=form)

@bp.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item = Item.query.get_or_404(item_id)
    form = ItemForm(obj=item)
    if form.validate_on_submit():
        item.title = form.title.data
        item.description = form.description.data
        db.session.commit()
        flash('Item atualizado.', 'success')
        return redirect(url_for('main.index'))
    return render_template('edit.html', form=form, item=item)

@bp.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item removido.', 'success')
    return redirect(url_for('main.index'))
