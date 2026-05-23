from PIL import Image, ImageDraw, ImageFont

# =========================
# SHOPPING CART STORAGE
# =========================

shopping_cart = {}

# =========================
# ADD PRODUCT FUNCTION
# =========================

def add_product(product_name, unit_price, quantity_purchased):

    shopping_cart[product_name] = {
        'unit_price': unit_price,
        'quantity_purchased': quantity_purchased
    }

# =========================
# CALCULATE CART TOTAL
# =========================

def calculate_cart_total():

    cart_total = 0

    for product_name in shopping_cart:

        unit_price = shopping_cart[product_name]['unit_price']

        quantity_purchased = shopping_cart[product_name]['quantity_purchased']

        cart_total += unit_price * quantity_purchased

    return cart_total

# =========================
# APPLY DISCOUNT
# =========================

def apply_discount(cart_total):

    if cart_total > 500:
        return cart_total * 0.9

    return cart_total

# =========================
# CALCULATE SALES TAX
# =========================

def calculate_sales_tax(discounted_total):

    return discounted_total * 0.075

# =========================
# CALCULATE FINAL TOTAL
# =========================

def calculate_final_total(discounted_total):

    return round(discounted_total * 1.075, 2)

# =========================
# USER INPUT LOOP
# =========================

while True:

    product_name = input('Enter product name: ')

    if product_name.lower() == 'done':
        break

    unit_price = float(input('Enter unit price: '))

    quantity_purchased = int(input('Enter quantity: '))

    add_product(
        product_name,
        unit_price,
        quantity_purchased
    )

# =========================
# PRINT RECEIPT
# =========================

def print_receipt():

    print('\n====== RECEIPT ======')

    receipt_lines = ["====== RECEIPT ======"]

    # Financial calculations
    cart_total = calculate_cart_total()

    discounted_total = apply_discount(cart_total)

    sales_tax = calculate_sales_tax(discounted_total)

    final_total = calculate_final_total(discounted_total)

    # Print products
    for product_name, product_details in shopping_cart.items():

        unit_price = product_details['unit_price']

        quantity_purchased = product_details['quantity_purchased']

        item_total = unit_price * quantity_purchased

        receipt_line = (
            f"{product_name.upper()} | "
            f"${unit_price} x {quantity_purchased} "
            f"= ${round(item_total, 2)}"
        )

        print(receipt_line)

        receipt_lines.append(receipt_line)

    # Summary section
    summary_lines = [

        f"Subtotal: ${round(cart_total, 2)}",

        f"Discounted Total: ${round(discounted_total, 2)}",

        f"Sales Tax (7.5%): ${round(sales_tax, 2)}",

        f"Final Total: ${round(final_total, 2)}"
    ]

    # Print summary
    for line in summary_lines:

        print(line)

        receipt_lines.append(line)

    print('======================')

    # Save receipt image
    save_receipt(receipt_lines)

# =========================
# SAVE RECEIPT IMAGE
# =========================

def save_receipt(receipt_lines):

    transaction_description = input(
        '\nEnter transaction description: '
    )

    filename = f"{transaction_description}.png"

    width = 600

    line_height = 35

    padding = 20

    height = (
        len(receipt_lines) * line_height
    ) + (padding * 2)

    # Create image
    image = Image.new(
        'RGB',
        (width, height),
        'white'
    )

    draw = ImageDraw.Draw(image)

    # Load font safely
    try:
        font = ImageFont.truetype(
            'arial.ttf',
            18
        )

    except:

        font = ImageFont.load_default()

    # Starting Y position
    y_position = padding

    # Draw receipt lines
    for line in receipt_lines:

        draw.text(
            (20, y_position),
            line,
            fill='black',
            font=font
        )

        y_position += line_height

    # Save image
    image.save(filename)

    print(f'\nReceipt saved as {filename}')

# =========================
# RUN PROGRAM
# =========================

print_receipt()