# 🎫 Sistema de Tickets Digital

Sistema de turnos digital para negocios con alta afluencia de clientes. Los clientes escanean un código QR y obtienen automáticamente su número de turno.

## 🌟 Características

- ✅ Asignación automática de tickets del 1 al 100
- 🔄 Reinicio automático después del ticket 100
- 📱 Código QR para que los clientes escaneen con su celular
- ⏰ Muestra la hora exacta en que el cliente solicitó su turno
- 💾 Persistencia de datos (el contador no se pierde al reiniciar)
- 🖥️ Panel de control para el dueño del negocio
- 📊 Visualización del último ticket asignado en tiempo real

## 📋 Requisitos

- Python 3.7 o superior
- Conexión a internet (para instalar dependencias)

## 🚀 Instalación

1. **Descarga o clona el proyecto** en tu computadora

2. **Abre una terminal** en la carpeta del proyecto

3. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

## ▶️ Cómo Ejecutar

1. **Inicia el servidor:**
```bash
python app.py
```

2. **Abre tu navegador** y ve a:
```
http://localhost:5000
```

3. **Verás el panel de control** donde podrás:
   - Ver el último ticket asignado
   - Generar el código QR
   - Imprimir el código QR
   - Descargar el código QR
   - Reiniciar el contador si es necesario

## 📱 Cómo Usar

### Para el Dueño del Negocio:

1. Ejecuta la aplicación en tu computadora
2. Entra a `http://localhost:5000` en tu navegador
3. Imprime el código QR que aparece en la pantalla
4. Coloca el código QR impreso en un lugar visible de tu negocio
5. Deja la aplicación corriendo mientras atiendas clientes

### Para los Clientes:

1. El cliente llega a tu negocio
2. Escanea el código QR con la cámara de su celular
3. Se le asigna automáticamente el siguiente número
4. Ve su número de turno y la hora de llegada en su celular
5. Espera hasta que lo llames por su número

## 🌐 Configuración para Internet (Opcional)

Si quieres que el sistema funcione desde internet y no solo desde tu red local:

1. **Opción fácil - Ngrok (Recomendado para pruebas):**
   - Descarga ngrok desde https://ngrok.com/
   - Ejecuta: `ngrok http 5000`
   - Usa la URL que te proporciona ngrok
   - Actualiza la línea 71 en `app.py` con tu URL de ngrok

2. **Opción profesional - Hosting:**
   - Sube tu aplicación a servicios como:
     - Heroku (gratis/pago)
     - PythonAnywhere (gratis/pago)
     - DigitalOcean (pago)
     - AWS (pago)
   - Actualiza la línea 71 en `app.py` con tu URL pública

### Cambiar la URL del QR:

Abre `app.py` y busca la línea 71:
```python
url = 'http://localhost:5000/ticket'
```

Cámbiala por tu URL pública:
```python
url = 'https://tu-dominio.com/ticket'
```

## 🔧 Funciones Adicionales

### Reiniciar el Contador Manualmente:
- En el panel de control hay un botón "Reiniciar Contador"
- Útil si quieres empezar desde 0 en cualquier momento

### Ver el Ticket Actual:
- El panel de control se actualiza automáticamente cada 2 segundos
- Muestra el último número asignado

## 📂 Estructura del Proyecto

```
ticket-system/
│
├── app.py                  # Aplicación Flask principal
├── requirements.txt        # Dependencias del proyecto
├── ticket_state.json      # Estado del contador (se crea automáticamente)
├── README.md              # Este archivo
│
└── templates/
    ├── index.html         # Panel de control (para el dueño)
    └── ticket.html        # Página del ticket (para clientes)
```

## 🛠️ Solución de Problemas

### El servidor no inicia:
- Verifica que Python esté instalado: `python --version`
- Verifica que las dependencias estén instaladas: `pip list`
- Asegúrate de que el puerto 5000 no esté ocupado

### El código QR no funciona:
- Si estás en tu red local, asegúrate de que tu celular esté en la misma red WiFi
- Si quieres acceso desde internet, configura ngrok u otro servicio de túnel
- Verifica que la URL en `app.py` (línea 71) sea correcta

### El contador se resetea al cerrar el programa:
- Esto NO debería pasar, el estado se guarda en `ticket_state.json`
- No borres el archivo `ticket_state.json` si quieres mantener el contador

## 💡 Consejos

1. **Imprime el QR en buena calidad** - Asegúrate de que sea grande y claro
2. **Colócalo en un lugar visible** - Los clientes deben verlo al entrar
3. **Agrega instrucciones** - Puedes poner un cartel que diga "Escanea para tu turno"
4. **Mantén el servidor corriendo** - No cierres la terminal mientras uses el sistema
5. **Haz respaldo** - Si necesitas, puedes copiar `ticket_state.json` para guardar el estado

## 📞 Soporte

Si tienes problemas o preguntas:
- Revisa este README completo
- Verifica que todas las dependencias estén instaladas
- Asegúrate de que el servidor esté corriendo

## 📝 Notas

- El sistema reinicia automáticamente después del ticket 100
- Cada ticket muestra la fecha y hora exacta de asignación
- El sistema es seguro para múltiples accesos simultáneos
- Los datos persisten incluso si reinicias el servidor

¡Disfruta de tu sistema de tickets digital y ahorra en papel! 🎉


