from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Sample in-memory storage for orders
orders = []

# Route to display the order form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submissions
@app.route('/submit_order', methods=['POST'])
def submit_order():
    somsa_qty = int(request.form.get('somsa', 0))
    rasgulla_qty = int(request.form.get('rasgulla', 0))
    chicken_qty = float(request.form.get('chicken', 0))
    sandwich_qty = int(request.form.get('sandwich', 0))
    nescafe_qty = int(request.form.get('nescafe', 0))
    burger_qty = int(request.form.get('burger', 0))

    # Calculate total cost
    total_cost = (somsa_qty * 9) + (rasgulla_qty * 10) + (chicken_qty * 200) + (sandwich_qty * 20) + (nescafe_qty * 15) + (burger_qty * 20)

    # Store the order
    order = {
        'somsa': somsa_qty,
        'rasgulla': rasgulla_qty,
        'chicken': chicken_qty,
        'sandwich': sandwich_qty,
        'nescafe': nescafe_qty,
        'burger': burger_qty,
        'total_cost': total_cost
    }
    orders.append(order)

    return redirect(url_for('order_history'))

# Route to display order history
@app.route('/orders')
def order_history():
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
    