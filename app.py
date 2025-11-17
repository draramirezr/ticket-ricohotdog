from flask import Flask, render_template, jsonify, send_file, request
import qrcode
from datetime import datetime
import json
import os
from io import BytesIO
import threading

app = Flask(__name__)

# Archivo para guardar el estado del ticket
TICKET_FILE = 'ticket_state.json'
lock = threading.Lock()

def load_ticket_state():
    """Carga el estado actual del ticket desde el archivo"""
    if os.path.exists(TICKET_FILE):
        with open(TICKET_FILE, 'r') as f:
            return json.load(f)
    return {'current_ticket': 0}

def save_ticket_state(state):
    """Guarda el estado del ticket en el archivo"""
    with open(TICKET_FILE, 'w') as f:
        json.dump(state, f)

def get_next_ticket():
    """Obtiene el siguiente número de ticket (1-100, con reinicio)"""
    with lock:
        state = load_ticket_state()
        current = state['current_ticket']
        
        # Incrementar y reiniciar si llega a 100
        next_ticket = (current % 100) + 1
        
        state['current_ticket'] = next_ticket
        save_ticket_state(state)
        
        return next_ticket

@app.route('/')
def index():
    """Página principal - para el dueño del negocio"""
    return render_template('index.html')

@app.route('/ticket')
def get_ticket():
    """Página que asigna el ticket al cliente"""
    ticket_number = get_next_ticket()
    current_time = datetime.now().strftime('%I:%M:%S %p')
    current_date = datetime.now().strftime('%d/%m/%Y')
    
    return render_template('ticket.html', 
                         ticket_number=ticket_number,
                         time=current_time,
                         date=current_date)

@app.route('/api/current')
def current_ticket():
    """API para obtener el ticket actual"""
    state = load_ticket_state()
    return jsonify(state)

@app.route('/api/assign')
def assign_ticket():
    """API para asignar un ticket manualmente desde el panel de control"""
    ticket_number = get_next_ticket()
    current_time = datetime.now().strftime('%I:%M:%S %p')
    
    return jsonify({
        'ticket_number': ticket_number,
        'time': current_time,
        'message': 'Ticket asignado exitosamente'
    })

@app.route('/api/reset')
def reset_tickets():
    """API para resetear el contador (opcional)"""
    with lock:
        save_ticket_state({'current_ticket': 0})
    return jsonify({'message': 'Contador reseteado', 'current_ticket': 0})

@app.route('/qr')
def generate_qr():
    """Genera el código QR para imprimir"""
    # URL dinámica - funciona tanto en local como en producción
    base_url = request.host_url.rstrip('/')
    url = f'{base_url}/ticket'
    
    # Crear código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar en memoria
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    # Crear archivo de estado si no existe
    if not os.path.exists(TICKET_FILE):
        save_ticket_state({'current_ticket': 0})
    
    # Obtener puerto de las variables de entorno (para Railway)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

