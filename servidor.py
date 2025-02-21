from flask import Flask,render_template,request,redirect,url_for,flash,jsonify, render_template_string
import views

app = Flask(__name__)
app.secret_key = 'admin123'
app.static_folder = 'static'

@app.route('/')
def index():
    notes = views.index()
    return render_template('index.html', notes=notes)

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')

    result = views.submit(titulo, detalhes)

    if result is True:
        flash('Nota adicionada com sucesso!', 'success')
    else:
        flash(f'Erro ao adicionar nota: {result}', 'danger')

    return redirect('/')

@app.route("/delete_note/<int:note_id>",methods=['GET'])
def delete_note(note_id):

    result = views.delete(note_id)
    if result:
        flash('Note Deleted','warning')
    else:
        flash(f'Erro ao deletar nota: {result}', 'danger')
    return redirect(url_for("index"))

@app.route("/edit_note/<string:note_id>", methods=['POST', 'GET'])
def edit_note(note_id):
    if request.method == 'POST':
        title = request.form['title']
        details = request.form['details']
        
        result = views.update_note(note_id, title, details)
        
        if result is True:
            flash('Usuário atualizado com sucesso!', 'success')
        else:
            flash(f'Erro ao atualizar usuário: {result}', 'danger')

        return redirect(url_for("index"))

    # Aqui você obtém os dados da nota
    data = views.get_note(note_id)

    # Verifique se data não é None
    if data:
        print(data)
        return render_template("edit_note.html", datas=data)
    else:
        flash("Nota não encontrada.", "danger")
        return redirect(url_for("index"))

@app.route("/update_note_order", methods=["POST"])
def update_note_order():
    data = request.json.get("order", [])
    for item in data:
        note_id = item["id"]
        new_position = item["position"]
            
    return jsonify({"message": "Ordem atualizada com sucesso!"})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.secret_key='admin1223'
    app.run(debug=True)