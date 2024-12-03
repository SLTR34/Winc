# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line

from models import *

def search(term):
    return Product.select().where(
        (fn.Lower(Product.name).contains(term.lower())) |
        (fn.Lower(Product.description).contains(term.lower()))
    )

def list_user_products(user_id):
    return Product.select().where(Product.user_id == user_id)

def list_products_per_tag(tag_id):
    return Product.select().join(ProductTag).join(Tag).where(Tag.id == tag_id)

def add_product_to_catalog(user_id, product):
    try:
        with database.atomic():
            user = User.get(User.id == user_id)
            new_product = Product.create(
                name=product["name"],
                description=product["description"],
                price=product["price"],
                quantity=product["quantity"],
                user=user
            )
            if "tags" in product:
                for tag_name in product["tags"]:
                    tag, _ = Tag.get_or_create(name=tag_name)
                    ProductTag.create(product=new_product, tag=tag)
        return True
    except IntegrityError:
        return False

def update_stock(product_id, new_quantity):
    try:
        product = Product.get(Product.id == product_id)
        product.quantity = new_quantity
        product.save()
        return True
    except Product.DoesNotExist:
        return False

def purchase_product(product_id, buyer_id, quantity):
    try:
        with database.atomic():
            product = Product.get(Product.id == product_id)
            buyer = User.get(User.id == buyer_id)
            if product.quantity >= quantity:
                product.quantity -= quantity
                product.save()
                Transaction.create(buyer=buyer, product=product, quantity=quantity)
                return True
            else:
                return False
    except Product.DoesNotExist:
        return False

def remove_product(product_id):
    try:
        product = Product.get(Product.id == product_id)
        product.delete_instance()
        return True
    except Product.DoesNotExist:
        return False

def run_tests():
    # Search for products based on a term
    search_results = search("sweater")
    print("Search Results:")
    for product in search_results:
        print(f"- {product.name}")
    print()

    # View the products of a given user
    user_products = list_user_products(1)
    print("User Products:")
    for product in user_products:
        print(f"- {product.name}")
    print()

    # View all products for a given tag
    tag_products = list_products_per_tag(1)
    print("Tag Products:")
    for product in tag_products:
        print(f"- {product.name}")
    print()

    # Add a product to a user
    product = {
        "name": "Pokemon Cards",
        "description": "Like Ash Ketch'em",
        "price": 4.99,
        "quantity": 10,
        "tags": ["Accessories"]
    }
    added = add_product_to_catalog(2, product)
    if added:
        print("Product added successfully")
    else:
        print("Failed to add product")
    print()

    # Remove a product from a user
    removed = remove_product(2)
    if removed:
        print("Product removed successfully")
    else:
        print("Failed to remove product")
    print()

    # Update the stock quantity of a product
    updated = update_stock(1, 15)
    if updated:
        print("Stock quantity updated successfully")
    else:
        print("Failed to update stock quantity")
    print()

    # Handle a purchase between a buyer and a seller for a given product
    purchased = purchase_product(1, 2, 2)
    if purchased:
        print("Product purchased successfully")
    else:
        print("Failed to purchase product")
    print()


if __name__ == "__main__":
    initialize_database()
    populate_test_database()
    # remove_product(10)
    # run_tests()