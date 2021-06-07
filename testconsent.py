from flask import Flask, jsonify, request,render_template_string

from flask_consent import Consent, ConsentData
app = Flask(__name__)
app.config['CONSENT_FULL_TEMPLATE'] = 'consent.html'
app.config['CONSENT_BANNER_TEMPLATE'] = 'consent_banner.html'
app.config['CONSENT_CONTACT_MAIL'] = 'test@test.test'
app.config['CONSENT_PRIMARY_SERVERNAME'] = 'primary.test'
consent = Consent(app)
consent.add_standard_categories()

@app.route('/')
def test():
    return jsonify(required=request.consent['required'],
                    preferences=request.consent['preferences'],
                    analytics=request.consent['analytics'])

@app.route('/banner')
def banner():
    return render_template_string('''
            <html>
            <head>{{ flask_consent_code() }}</head>
            <body></body>
            </html>
            ''')

if __name__  == '__main__':
	app.run(debug=True)