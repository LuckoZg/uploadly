from flask import Blueprint, request, render_template, redirect, url_for, flash, send_from_directory, current_app
from werkzeug.utils import secure_filename
from werkzeug.exceptions import NotFound
from .models import FileUpload
from . import db, bcrypt
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        password = request.form.get('password')

        if not file or not password:
            flash('Both file and password are required.', 'danger')
            return redirect(url_for('main.upload'))

        original_filename = secure_filename(file.filename)
        new_upload = FileUpload(
            original_filename=original_filename,
            stored_filename="TEMP",
            password_hash=bcrypt.generate_password_hash(password).decode('utf-8')
        )
        db.session.add(new_upload)
        db.session.commit()

        stored_filename = f"{new_upload.id}_{original_filename}"
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], stored_filename)
        file.save(file_path)

        new_upload.stored_filename = stored_filename
        db.session.commit()

        file_url = url_for('main.get_file', file_id=new_upload.id, _external=True)
        return render_template('upload_success.html', file_url=file_url)

    return render_template('upload_form.html')


@main.route('/get-file/<file_id>', methods=['GET', 'POST'])
def get_file(file_id):
    file = FileUpload.query.get(file_id)
    if not file:
        raise NotFound("File not found.")

    if request.method == 'POST':
        password = request.form.get('password')
        if bcrypt.check_password_hash(file.password_hash, password):
            return send_from_directory(
                os.path.abspath(current_app.config['UPLOAD_FOLDER']),
                file.stored_filename,
                as_attachment=True,
                download_name=file.original_filename
            )
        flash('Incorrect password.', 'danger')

    return render_template('password_prompt.html')