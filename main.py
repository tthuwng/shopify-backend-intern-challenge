from flask import Flask, render_template, request, url_for, flash, redirect, abort
import sqlite3, os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SECRET_KEY'] = 'acc0ebdf6901f5f8fd9de9f94112ef95fc88195ec5e9e548'
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def get_db_connection():
  conn = sqlite3.connect('database.db')
  conn.row_factory = sqlite3.Row
  return conn


def get_inventory(inventory_id):
    conn = get_db_connection()
    inventory = conn.execute('SELECT * FROM inventories WHERE id = ?',
                        (inventory_id,)).fetchone()
    conn.close()
    if inventory is None:
        abort(404)
    return inventory

def isFloat(element):
    try:
        if float(element) > 0:
            return True
        return False
    except ValueError:
        return False


@app.route('/upload/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    inventory = get_inventory(id)

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']

        image = request.files['image']
        imagename = inventory[4]
        if image.filename != '':
          
          if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
          imagename = filename
        
        

        if not name:
            flash('Name is required!')

        elif not description:
            flash('description is required!')
        elif not price:
            flash('Price is required!')
        
        elif not isFloat(price):
            flash('Price must be positive!')
        elif stock and not stock.isdigit():
            flash('Stock must be positive!')
        # elif not image:
        #     flash('Image is required!')

        else:
          
          

          conn = get_db_connection()
          conn.execute('UPDATE inventories SET name = ?, description = ?, price = ?, image = ?, stock = ?'
                        ' WHERE id = ?',
                        (name, description, float(price), imagename, int(stock), id))
          conn.commit()
          conn.close()
          return redirect(url_for('index'))
    return render_template('edit.html', inventory=inventory)

@app.route('/create/', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    stock = request.form['stock']
    image = request.files['image']
    
    if image.filename == '':
      flash('No selected image')
    elif not name:
      flash('Name is required!')
    elif not description:
      flash('Description is required!')
    elif not price:
      flash('Price is required!')
    elif not isFloat(price):
      flash('Price must be positive!')
    elif stock and not stock.isdigit():
      flash('Stock must be positive!')
    elif not image:
      flash('Image is required!')


    else:
      if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      imagename = filename

      conn = get_db_connection()
      price = float(price)
      stock = int(stock)
      conn.execute('INSERT INTO inventories (name, description, price, image, stock) VALUES (?, ?, ?, ?, ?)', (name, description, price, imagename, stock))
      conn.commit()
      conn.close()
      return redirect(url_for('index'))
  return render_template('create.html')
 
@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    inventory = get_inventory(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM inventories WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(inventory['name']))
    return redirect(url_for('index'))



def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def index():
  conn = get_db_connection()
  inventories = conn.execute('SELECT * FROM inventories').fetchall()
  conn.close()
  return render_template('index.html', inventories=inventories)
