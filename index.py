from flask import Flask,render_template,flash,request,redirect,url_for,abort
import whois
import dns
import dns.resolver
import builtwith


app = Flask(__name__)
app.secret_key = b'ToolBoxFootPrinting'


""" INDEX """

@app.route('/')
def index():
    return render_template("index.html")



""" WHOIS FOOTPRINTING """

@app.route('/whois',methods=['GET','POST'])
def whoist():
    try:
        sitio_whois = ""
        if request.method == 'POST':
            sitio = request.form['sitio']
            if not sitio:
                flash("ingrese un dominio")
            else:
                sitio_whois = whois.whois(sitio)
    except Exception as e:
        print(e)
    return render_template("whois.html",sitio =sitio_whois)



""" DNS FOOTPRINTING """

@app.route('/dns',methods=['GET','POST'])
def footprinting_dns():
    dominio = None
    dominios = dict()
    if request.method == 'POST':
        dominio = request.form['dominio']
        if not dominio:
            flash("ingrese un dominio")
        else:
            MX = dns.resolver.query(dominio,'MX')
            NS = dns.resolver.query(dominio,'NS')
            A_IPV4 = dns.resolver.query(dominio, 'A')
            dominios = {"Servidores de Correo (MX)":MX,
                        "Servidores de Nombre (NS)":NS,
                        "Registros para direcciones IPV4 (A)":A_IPV4}
            
      
    return render_template("dns.html",dominios = dominios,dominio = dominio)


""" CONSTRUCTED """

@app.route('/constructed',methods=['GET','POST'])
def constructed():
    resolver = ''
    if request.method == 'POST':
        url = request.form['url']
        if not url or url == " ":
            flash('Ingrese una URL')
        else:
            resolver = builtwith.parse(url)
           
    return render_template("constructed.html", resolver = resolver)



app.run(debug=True,port=4444)