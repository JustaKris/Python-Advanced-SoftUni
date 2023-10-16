import json
from canvas import app, tk
from helpers import base_path, clean_screen, os
from PIL import Image, ImageTk


def update_user(username, product_id):
    with open(base_path + "/db/users.txt", "r+", newline="\n") as file:
        users = [json.loads(user.strip()) for user in file]
        for user in users:
            if user['username'] == username:
                user['products'].append(product_id)
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(user) + "\n" for user in users])
                return


def update_product(product_id):
    print(base_path)
    with open(base_path + "/db/products.txt", "r+") as file:
        products = [json.loads(product.strip()) for product in file]
        for product in products:
            if product["id"] == product_id:
                product['count'] -= 1
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(product) + '\n' for product in products])
                return


def buy_product(product_id):
    clean_screen()

    with open(base_path + "/db/current_user.txt") as file:
        username = file.read()
    if username is not None:
        update_user(username, product_id)
        update_product(product_id)

    render_products_screen()


def render_products_screen():
    clean_screen()

    with open(base_path + "/db/current_user.txt") as f:
        username = f.read()
    # with open("db/users.txt") as f:
    #     users = [json.loads(u.strip()) for u in f]
    #     for user in users:
    #         if user['username'] == username:
    with open(base_path + "/db/products.txt") as f:
        products = [json.loads(product.strip()) for product in f]
        for i, product in enumerate(products):
            row = i // 4 * 4
            column = i % 4
            tk.Label(app, text=product['name']).grid(row=row, column=column)

            img = Image.open(os.path.join(base_path, "db/images", product['img_path'])).resize((100, 100))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(image=photo_image)
            image_label.image = photo_image
            image_label.grid(row=row + 1, column=column)

            tk.Label(app, text=product['count']).grid(row=row + 2, column=column)
            tk.Button(app,
                      text=f"Buy {product['id']}",
                      command=lambda p=product["id"]: buy_product(p)
                      ).grid(row=row + 3, column=column)
